"""Channel registration handling"""
import asyncpg
import discord
import handlers.request_handler as REQH
import handlers.sticky_handler as SH

ADD_RAID_CHANNEL = """
INSERT INTO valid_raid_channels (channel_id, guild_id)
VALUES ($1, $2);
"""
INIT_RAID_COUNTER = """
INSERT INTO guild_raid_counters (guild_id)
VALUES ($1);
"""
async def database_register_raid_channel(bot, ctx, channel_id, guild_id):
    """Registers raid channel within database and initalizes guilds raid counter."""
    connection = await bot.acquire()
    results = None
    try:
        results = await connection.execute(ADD_RAID_CHANNEL,
                                           int(channel_id),
                                           int(guild_id))
    except asyncpg.PostgresError as error:
        print("[!] Error occured registering raid channel. [{}]".format(error))
    try:
        await connection.execute(INIT_RAID_COUNTER,
                                 int(guild_id))
    except asyncpg.PostgresError as error:
        print("[!] Error occured registering raid counter. [{}]".format(error))
    await bot.release(connection)
    if results:
        print("[*][{}][{}] New raid channel registered.".format(ctx.guild.name, channel_id))

async def register_request_channel_handle(ctx, bot):
    channel_id = ctx.channel.id
    guild_id = ctx.guild.id
    try:
        await ctx.message.delete()
    except:
        pass
    await REQH.database_register_request_channel(bot, ctx, channel_id, guild_id)

async def register_raid_channel_handle(ctx, bot):
    channel_id = ctx.channel.id
    guild_id = ctx.guild.id
    try:
        await ctx.message.delete()
    except discord.DiscordException:
        pass
    await database_register_raid_channel(bot, ctx, channel_id, guild_id)
    try:
        await SH.toggle_raid_sticky(bot, ctx, channel_id, guild_id)
    except discord.DiscordException as e:
        print("[!] An error occurred [{}]".format(e))

ADD_RAID_LOBBY_CATEGORY = """
INSERT INTO raid_lobby_category (guild_id, category_id, log_channel_id)
VALUES ($1, $2, $3);
"""
#UPDATE_LOG_CHANNEL = """
#UPDATE raid_lobby_category
#SET log_channel_id = $1
#WHERE (guild_id = $2);
#"""
async def database_register_raid_lobby_category(bot, ctx, guild_id, category_id, log_channel_id):
    """Registers raid lobby category within database and initalizes log."""
    connection = await bot.acquire()
    results = None
    try:
        results = await connection.execute(ADD_RAID_LOBBY_CATEGORY,
                                           int(guild_id),
                                           int(category_id),
                                           int(log_channel_id))
    except asyncpg.PostgresError as error:
        print("[!] Error occured registering raid lobby category. [{}]".format(error))
    await bot.release(connection)
    if results:
        print("[*][{}][{}] New raid lobby category registered.".format(ctx.guild.name, category_id))


async def register_raid_lobby_category(ctx, bot):
    try:
        await ctx.message.delete()
    except discord.DiscordException:
        pass

    channel = ctx.channel
    if not channel.category_id:
        embed = discord.Embed(title="Error", description="This channel is not in a category. A category is necessary to set up a raid lobby system. Create a category and place a channel in there, then run this command again.", color=0xff8c00)
        ctx.send(" ",embed=embed, delete_after=15)
        return False

    category_id = channel.category_id
    log_channel_id = channel.id
    #await RLH.set_up_lobby_log_channel(ctx, bot)
    await database_register_raid_lobby_category(bot, ctx, ctx.guild.id, category_id, log_channel_id)
