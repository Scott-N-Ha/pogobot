from datetime import datetime, timedelta

import asyncpg
import discord
import handlers.helpers as H
import handlers.raid_handler as RH

GET_CATEGORY_BY_GUILD_ID = """
    SELECT * FROM raid_lobby_category WHERE (guild_id = $1) LIMIT 1;
"""
async def get_raid_lobby_category_by_guild_id(bot, guild_id):
    connection = await bot.acquire()
    try:
        category_data = await connection.fetchrow(GET_CATEGORY_BY_GUILD_ID,
                                                  int(guild_id))
    except asyncpg.PostgresError as error:
        print("[!] Error retreiving raid lobby category data. [{}]".format(error))
        return
    finally:
        await bot.pool.release(connection)

    #category_id = category_data.get("category_id")
    if not category_data:
        print("[!] Error retreiving raid lobby category data. [{}]".format("No category found. Passing."))
        return False

    return category_data


GET_LOBBY_BY_USER_ID = """
    SELECT * FROM raid_lobby_user_map WHERE (host_user_id = $1);
"""
async def get_lobby_channel_for_user_by_id(bot, user_id):
    connection = await bot.acquire()
    try:
        lobby_data = await connection.fetchrow(GET_LOBBY_BY_USER_ID,
                                               int(user_id))
    except asyncpg.PostgresError as error:
        print("[!] Error retreiving raid lobby data. [{}]".format(error))
        return
    finally:
        await bot.pool.release(connection)

    if not lobby_data:
        return
    lobby_channel_id = lobby_data.get("lobby_channel_id")

    #guild_id = lobby_data.get("guild_id")

    lobby = bot.get_channel(int(lobby_channel_id))
    if not lobby:
        guild = bot.get_guild(lobby_data.get("guild_id"))
        try:
            lobby = await bot.fetch_channel(int(lobby_channel_id))
        except discord.DiscordException:
            return False

    return lobby

GET_LOBBY_BY_LOBBY_ID = """
    SELECT * FROM raid_lobby_user_map WHERE (lobby_channel_id = $1);
"""
async def get_lobby_channel_by_lobby_id(bot, channel_id):
    connection = await bot.acquire()
    try:
        lobby_data = await connection.fetchrow(GET_LOBBY_BY_LOBBY_ID,
                                               int(channel_id))
    except asyncpg.PostgresError as error:
        print("[!] Error retreiving raid lobby data. [{}]".format(error))
        return
    finally:
        await bot.pool.release(connection)
    if not lobby_data:
        return False

    lobby_channel_id = lobby_data.get("lobby_channel_id")

    lobby = bot.get_channel(int(lobby_channel_id))
    if not lobby:
        return False

    return lobby

GET_RELEVANT_LOBBY_BY_TIME_AND_USERS = """
    SELECT * FROM raid_lobby_user_map
    WHERE (user_count < user_limit)
    ORDER BY posted_at;
"""
async def get_latest_lobby_data_by_timestamp(bot):
    connection = await bot.acquire()
    results = await connection.fetch(GET_RELEVANT_LOBBY_BY_TIME_AND_USERS)
    await bot.release(connection)

    return results

async def log_message_in_raid_lobby_channel(bot, message, raid_lobby_channel):
    author = message.author
    category_data = await get_raid_lobby_category_by_guild_id(bot, message.guild.id)
    log_channel_id = category_data.get("log_channel_id")
    log_channel = bot.get_channel(int(log_channel_id))

    new_embed = discord.Embed(title="Logged Message", url=message.jump_url, description=message.content)
    new_embed.set_author(name=author.display_name, icon_url=author.avatar_url)
    new_embed.set_footer(text="User ID: {}".format(author.id))
    await log_channel.send(" ", embed=new_embed)
# async def set_up_management_channel(ctx, bot):
#     channel = ctx.channel
#     if not channel.category_id:
#         embed = discord.Embed(title="Error", description="This channel is not in a category. A category is necessary to set up a raid lobby system. Create a category and place a channel in there, then run this command again.", color=0xff8c00)
#         ctx.send(" ",embed=embed, delete_after=15)
#         return False

#     category_id = channel.category_id



#async def user_lobby_management_reaction_handle(ctx, bot):

# async def set_up_lobby_log_channel(ctx, bot):
#     channel = ctx.channel
#     if not channel.category_id:
#         embed = discord.Embed(title="Error", description="This channel is not in a category. A category is necessary to set up a raid lobby system. Create a category and place a channel in there, then run this command again.", color=0xff8c00)
#         ctx.send(" ",embed=embed, delete_after=15)
#         return False

#     try:
#         await channel.edit(name="raid-lobby-logs", reason="Establishing log channel for raid lobbies.")
#     except discord.DiscordException as error:
#         print("[*][{}] An error occurred setting up the log channel for a raid category. [{}]".format(ctx.guild.name, error))
#         return False

#     return True

NEW_LOBBY_INSERT = """
INSERT INTO raid_lobby_user_map (lobby_channel_id, host_user_id, raid_message_id, guild_id, posted_at, delete_at, user_count, user_limit, applied_users, notified_users)
VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
"""
async def add_lobby_to_table(bot, lobby_channel_id, host_user_id, raid_id, guild_id, delete_at):
    """Add a raid to the database with all the given data points."""
    cur_time = datetime.now()
    connection = await bot.acquire()
    await connection.execute(NEW_LOBBY_INSERT,
                             int(lobby_channel_id),
                             int(host_user_id),
                             int(raid_id),
                             int(guild_id),
                             cur_time,
                             delete_at,
                             0,
                             5,
                             0,
                             0)
    await bot.release(connection)

async def create_raid_lobby(ctx, bot, raid_message_id, raid_host_member, time_to_remove_lobby):
    guild = ctx.guild
    raid_lobby_category_channel_data = await get_raid_lobby_category_by_guild_id(bot, guild.id)
    if not raid_lobby_category_channel_data:
        return False
    raid_lobby_category_channel_id = raid_lobby_category_channel_data.get("category_id")
    raid_lobby_category_channel = bot.get_channel(int(raid_lobby_category_channel_id))

    mod_role = discord.utils.get(guild.roles, name="Mods")
    raid_moderator_role = discord.utils.get(guild.roles, name="Raid Moderator")
    count = await RH.get_raid_count(bot, ctx, False)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        mod_role: discord.PermissionOverwrite(read_messages=True),
        raid_moderator_role: discord.PermissionOverwrite(read_messages=True),
        raid_host_member: discord.PermissionOverwrite(read_messages=True)
    }
    channel_name = "raid-lobby-{}".format(count)
    reason = "Spawning new raid lobby for [{}]".format(raid_host_member.name)
    try:
        new_raid_lobby = await raid_lobby_category_channel.create_text_channel(channel_name, reason=reason, overwrites=overwrites)
    except discord.DiscordException as error:
        try:
            await ctx.send("Something went wrong when trying to create your raid lobby: [{}]".format(error))
        except discord.DiscordException:
            pass
        print("[!] An error occurred creating a raid lobby. [{}]".format(error))
        return False
    new_embed = discord.Embed(title="Start of Lobby", description="Welcome to your raid lobby. As players apply they will check in and be added here.\n\nAs the host it is your job to ensure you either add everyone, or everyone adds you. Once you have everyone in your friends list, then it is up to you to invite the players who join this lobby into your raid in game.")
    await new_raid_lobby.send("{}".format(raid_host_member.mention), embed=new_embed)
    try:
        await add_lobby_to_table(bot, new_raid_lobby.id, raid_host_member.id, raid_message_id, ctx.guild.id, time_to_remove_lobby)
    except asyncpg.PostgresError as error:
        print("[!] An error occurred adding a lobby to the database. [{}]".format(error))
        await new_raid_lobby.delete()
        return False

    bot.lobby_remove_trigger.set()

    return True

UPDATE_TIME_TO_REMOVE_LOBBY = """
    UPDATE raid_lobby_user_map
    SET delete_at = $1
    WHERE (host_user_id = $2);
"""
async def alter_deletion_time_for_raid_lobby(bot, ctx, message):
    current_time = datetime.now()
    new_delete_time = current_time + timedelta(minutes=15)
    channel = await get_lobby_channel_for_user_by_id(bot, ctx.user_id)

    try:
        if channel:
            new_embed = discord.Embed(title="System Notification", description="This lobby will expire in 15 minutes.")
            await channel.send(" ", embed=new_embed)
    except discord.DiscordException:
        pass

    connection = await bot.acquire()
    await connection.execute(UPDATE_TIME_TO_REMOVE_LOBBY,
                             new_delete_time,
                             int(ctx.user_id))
    await bot.release(connection)

GET_NEXT_LOBBY_TO_REMOVE_QUERY = """
    SELECT * FROM raid_lobby_user_map
    ORDER BY delete_at
    LIMIT 1;
"""
async def get_next_lobby_to_remove(bot):
    connection = await bot.acquire()
    result = await connection.fetchrow(GET_NEXT_LOBBY_TO_REMOVE_QUERY)
    await bot.release(connection)

    return result

UPDATE_APPLICATION_DATA_FOR_USER = """
    UPDATE raid_application_user_map
    SET (raid_message_id = $1)
    WHERE (user_id = $2);
"""
async def update_application_for_user(bot, member, raid_message_id):
    connection = await bot.acquire()
    await connection.execute(UPDATE_APPLICATION_DATA_FOR_USER,
                             int(raid_message_id),
                             int(member.id))
    await bot.release(connection)
    try:
        new_embed = discord.Embed(title="System Notification", description="You have updated your application to the selected raid.")
        await member.send(" ", embed=new_embed)
    except discord.DiscordException:
        pass

REMOVE_APPLICATION_FOR_USER_BY_ID = """
    DELETE FROM raid_application_user_map WHERE (user_id = $1)
    RETURNING raid_message_id;
"""
REDUCE_APPLICANT_COUNT_BY_RAID_ID = """
    UPDATE raid_lobby_user_map
    SET applied_users = applied_users - 1
    WHERE (raid_message_id = $1);
"""
async def remove_application_for_user(bot, member, raid_id):
    connection = await bot.acquire()
    await connection.execute(REMOVE_APPLICATION_FOR_USER_BY_ID, member.id)
    await connection.execute(REDUCE_APPLICANT_COUNT_BY_RAID_ID, raid_id)
    await bot.release(connection)
    try:
        new_embed = discord.Embed(title="System Notification", description="You have withdrawn your application to the selected raid.")
        await member.send(" ", embed=new_embed)
    except discord.DiscordException:
        pass

INSERT_NEW_APPLICATION_DATA = """
    INSERT INTO raid_application_user_map (user_id, raid_message_id, guild_id, is_requesting, speed_bonus_weight, has_been_notified, checked_in)
    VALUES ($1, $2, $3, $4, $5, $6, $7)
"""
UPDATE_LOBBY_APPLICANT_DATA = """
    UPDATE raid_lobby_user_map
    SET applied_users = applied_users + 1
    WHERE (raid_message_id = $1);
"""
async def insert_new_application(bot, user_id, raid_message_id, guild_id, is_requesting, speed_bonus_weight):
    connection = await bot.acquire()
    await connection.execute(INSERT_NEW_APPLICATION_DATA,
                             int(user_id),
                             int(raid_message_id),
                             int(guild_id),
                             is_requesting,
                             speed_bonus_weight,
                             False,
                             False)
    await bot.release(connection)

async def calculate_speed_bonus(bot, message):
    creation_time = message.created_at
    time_difference = (datetime.now() - creation_time)
    return time_difference.total_seconds() / 60 * 100

async def handle_new_application(ctx, bot, member, message, channel):
    raid_data = await RH.retrieve_raid_data_by_message_id(ctx, bot, message.id)
    if not raid_data:
        return False
    pokemon_name = H.get_pokemon_name_from_raid(message)
    host_id = raid_data.get("user_id")

    try:
        if host_id == member.id:
            new_embed = discord.Embed(title="Error", description="You cannot apply to your own raid!")
            await member.send(" ", embed=new_embed)
        else:
            new_embed = discord.Embed(title="System Notification", description="You have applied for the selected raid.\nApplicants will be selected at random based on a weighted system.")
            await member.send(" ", embed=new_embed)
    except discord.Forbidden:
        # Prevents users from applying without ability to send a DM.
        new_embed = discord.Embed(title="Communication Error", description="{}, I cannot DM you. You will not be able to apply for raids until I can.".format(member.mention))
        await channel.send(" ", embed=new_embed, delete_after=15)
        return False

    role = discord.utils.get(member.roles, name=pokemon_name)
    speed_bonus = await calculate_speed_bonus(bot, message)
    await insert_new_application(bot, member.id, message.id, message.guild.id, True if role else False, speed_bonus)
    bot.applicant_trigger.set()

QUERY_APPLICATION_DATA_FOR_USER = """
    SELECT * FROM raid_application_user_map WHERE (user_id = $1);
"""
async def get_applicant_data_for_user(bot, user_id):
    connection = await bot.acquire()
    result = await connection.fetchrow(QUERY_APPLICATION_DATA_FOR_USER, user_id)
    await bot.release(connection)
    return result

async def handle_application_to_raid(bot, ctx, message, channel):
    guild = message.guild
    member = guild.get_member(ctx.user_id)
    result = await get_applicant_data_for_user(bot, ctx.user_id)

    if result:
        applied_to_raid_id = result.get("raid_message_id")
        has_been_notified = result.get("has_been_notified")
        if has_been_notified:
            new_embed = discord.Embed(title="Error", description="You are already locked into a raid. Wait until that raid is complete.")
            await member.send(" ", embed=new_embed)
            return
        raid_message_id = message.id
        if applied_to_raid_id == raid_message_id:
            await remove_application_for_user(bot, member, applied_to_raid_id)
        else:
            await update_application_for_user(bot, member, applied_to_raid_id)
    else:
        await handle_new_application(ctx, bot, member, message, channel)

QUERY_APPLICANT_BY_MESSAGE_ID = """
    SELECT * FROM raid_application_user_map WHERE (activity_check_message_id = $1);
"""
async def get_applicant_data_by_message_id(bot, message_id):
    connection = await bot.acquire()
    result = await connection.fetchrow(QUERY_APPLICANT_BY_MESSAGE_ID, message_id)
    await bot.release(connection)
    return result


GET_USERS_BY_RAID_MESSAGE_ID = """
    SELECT * FROM raid_application_user_map WHERE (raid_message_id = $1);
"""
async def get_applicants_by_raid_id(bot, raid_message_id):
    connection = await bot.acquire()
    results = await connection.fetch(GET_USERS_BY_RAID_MESSAGE_ID, int(raid_message_id))
    await bot.release(connection)

    return results

QUERY_RECENT_PARTICIPATION = """
    SELECT * FROM raid_participation_table WHERE (user_id = $1)
"""
async def calculate_weight(bot, user_data, member):
    connection = await bot.acquire()
    result = await connection.fetchrow(QUERY_RECENT_PARTICIPATION, int(member.id))
    await bot.release(connection)

    recent_participation_weight = 100
    request_bonus_weight = int(user_data.get("is_requesting")) * 100
    speed_bonus_weight = int(user_data.get("speed_bonus_weight"))

    if result:
        last_participation_time = result.get("last_participation_time")
        current_time = datetime.now()
        time_difference = current_time - last_participation_time
        if time_difference.total_seconds() < 3600:
            recent_participation_weight = (time_difference.total_seconds()/3600) * 100

    return recent_participation_weight + request_bonus_weight + speed_bonus_weight

UPDATE_LOBBY_APPLICANT_DATA = """
    UPDATE raid_application_user_map
    SET has_been_notified = true,
        activity_check_message_id = $1
    WHERE (user_id = $2);
"""

async def set_notified_flag(bot, message_id, user_id):
    connection = await bot.acquire()
    await connection.execute(UPDATE_LOBBY_APPLICANT_DATA, int(message_id), int(user_id))
    await bot.release(connection)

INCREMENT_APPLICANT_COUNT = """
    UPDATE raid_lobby_user_map
    SET notified_users = notified_users + 1
    WHERE (lobby_channel_id = $1)
"""
async def increment_notified_users_for_raid_lobby(bot, lobby_id):
    connection = await bot.acquire()
    await connection.execute(INCREMENT_APPLICANT_COUNT, int(lobby_id))
    await bot.release(connection)

async def process_user_list(bot, raid_lobby_data, sorted_users):
    counter = 0
    current_count = raid_lobby_data.get("user_count")
    user_limit = raid_lobby_data.get("user_limit")
    notified_count = raid_lobby_data.get("notified_users")

    total_pending = notified_count + current_count
    current_needed = user_limit - total_pending

    for user in sorted_users:
        if counter > current_needed:
            break
        counter+=1
        member = user["member_object"]
        user_data = user["user_data"]
        new_embed = discord.Embed(title="Activity Check", description="Tap the reaction below to confirm you are present. This message will expire in 30 seconds.")
        message = await member.send(" ", embed=new_embed, delete_after=30)
        await message.add_reaction("⏱️")
        await set_notified_flag(bot, message.id, member.id)
        await increment_notified_users_for_raid_lobby(bot, raid_lobby_data.get("lobby_channel_id"))

QUERY_LOBBY_BY_RAID_ID = """
    SELECT * FROM raid_lobby_user_map WHERE (raid_message_id = $1)
"""
async def get_lobby_data_by_raid_id(bot, raid_id):
    connection = await bot.acquire()
    result = await connection.fetchrow(QUERY_LOBBY_BY_RAID_ID, int(raid_id))
    await bot.release(connection)

    return result

UPDATE_USER_COUNT_FOR_RAID_LOBBY = """
    UPDATE raid_lobby_user_map
    SET user_count = user_count + 1,
        notified_users = notified_users - 1
    WHERE (lobby_channel_id = $1);
"""
async def increment_user_count_for_raid_lobby(bot, lobby_id):
    connection = await bot.acquire()
    result = await connection.execute(UPDATE_USER_COUNT_FOR_RAID_LOBBY, int(lobby_id))
    await bot.release(connection)

UPDATE_CHECKED_IN_FLAG = """
    UPDATE raid_application_user_map
    SET checked_in = true
    WHERE (user_id = $1);
"""
async def set_checked_in_flag(bot, user_id):
    connection = await bot.acquire()
    result = await connection.execute(UPDATE_CHECKED_IN_FLAG, int(user_id))
    await bot.release(connection)

DELETE_RECENT_PARTICIPATION_RECORD = """
    DELETE FROM raid_participation_table WHERE (user_id = $1);
"""
UDPATE_RECENT_PARTICIPATION = """
    INSERT INTO raid_participation_table(user_id, last_participation_time)
    VALUES ($1, $2);
"""
async def set_recent_participation(bot, user_id):
    connection = await bot.acquire()
    await connection.execute(DELETE_RECENT_PARTICIPATION_RECORD, int(user_id))
    await connection.execute(UDPATE_RECENT_PARTICIPATION, int(user_id), datetime.now())
    await bot.release(connection)

async def handle_activity_check_reaction(ctx, bot, message):
    connection = await bot.acquire()
    result = await connection.fetchrow(QUERY_APPLICATION_DATA_FOR_USER, ctx.user_id)
    await bot.release(connection)
    if not result:
        return

    activity_check_message_id = result.get("activity_check_message_id")
    if not message.id == activity_check_message_id:
        return

    raid_message_id = result.get("raid_message_id")

    lobby_data = await get_lobby_data_by_raid_id(bot, raid_message_id)
    if not lobby_data:
        return
    lobby_id = lobby_data.get("lobby_channel_id")
    lobby = bot.get_channel(int(lobby_id))

    guild = lobby.guild
    user_id = ctx.user_id
    member = guild.get_member(int(user_id))
    await set_checked_in_flag(bot, member.id)
    await lobby.set_permissions(member, read_messages=True,
                                        send_messages=True)
    await increment_user_count_for_raid_lobby(bot, lobby_id)
    await set_recent_participation(bot, user_id)
    new_embed = discord.Embed(title="System Notification", description="A user has checked in. They have been pinged for convenience.\n\nThe host has been listed and pinged at the top of this channel.")
    await lobby.send("{}".format(member.mention), embed=new_embed)
    try:
        await message.delete()
    except discord.DiscordException:
        pass

GET_LOBBY_BY_LOBBY_ID = """
    SELECT * FROM raid_lobby_user_map WHERE (lobby_channel_id = $1);
"""
async def get_lobby_data_by_lobby_id(bot, lobby_id):
    connection = await bot.acquire()
    result = await connection.fetchrow(GET_LOBBY_BY_LOBBY_ID, lobby_id)
    await bot.release(connection)

    return result

PURGE_APPLICANTS_FOR_RAID = """
    DELETE FROM raid_application_user_map WHERE (raid_message_id = $1);
"""
async def remove_applicants_for_raid_by_raid_id(bot, raid_id):
    connection = await bot.acquire()
    await connection.execute(PURGE_APPLICANTS_FOR_RAID, raid_id)
    await bot.release(connection)

REMOVE_LOBBY_BY_ID = """
    DELETE FROM raid_lobby_user_map WHERE (lobby_channel_id = $1);
"""
async def remove_lobby_by_lobby_id(bot, lobby_id):
    lobby_data = await get_lobby_data_by_lobby_id(bot, lobby_id)
    raid_id = lobby_data.get("raid_message_id")
    await remove_applicants_for_raid_by_raid_id(bot, raid_id)

    connection = await bot.acquire()
    await connection.execute(REMOVE_LOBBY_BY_ID, lobby_id)
    await bot.release(connection)

SELECT_ALL_LOBBIES = """
    SELECT * FROM raid_lobby_user_map;
"""
async def get_all_lobbies(bot):
    connection = await bot.acquire()
    result = await connection.fetch(SELECT_ALL_LOBBIES)
    await bot.release(connection)

    return result

SELECT_ALL_APPLICATIONS = """
    SELECT * FROM raid_application_user_map;
"""
async def get_all_applications(bot):
    connection = await bot.acquire()
    result = await connection.fetch(SELECT_ALL_APPLICATIONS)
    await bot.release(connection)
    return result

REMOVE_LOG_CHANNEL_BY_ID = """
    DELETE FROM raid_lobby_category WHERE (log_channel_id = $1);
"""
async def check_if_log_channel_and_purge_data(bot, channel_id):
    connection = await bot.acquire()
    result = await connection.execute(REMOVE_LOG_CHANNEL_BY_ID, int(channel_id))
    await bot.release(connection)


async def handle_user_failed_checkin(bot, applicant_data):
    guild_id = applicant_data.get("guild_id")
    guild = bot.get_guild(int(guild_id))

    member = guild.get_member(applicant_data.get("user_id"))
    if not member:
        return False

    await remove_application_for_user(bot, member, applicant_data.get("raid_message_id"))
    new_embed = discord.Embed(title="System Notification", description="You failed to check in and have been removed.")
    try:
        await member.send(" ", embed=new_embed)
    except discord.DiscordException:
        pass