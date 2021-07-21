"""https://www.dragonflycave.com/resources/pokemon-list-generator"""


NATIONAL_DEX =\
{
  "001_00":"Bulbasaur",
  "002_00":"Ivysaur",
  "003_00":"Venusaur",
  "004_00":"Charmander",
  "005_00":"Charmeleon",
  "006_00":"Charizard",
  "007_00":"Squirtle",
  "008_00":"Wartortle",
  "009_00":"Blastoise",
  "010_00":"Caterpie",
  "011_00":"Metapod",
  "012_00":"Butterfree",
  "013_00":"Weedle",
  "014_00":"Kakuna",
  "015_00":"Beedrill",
  "016_00":"Pidgey",
  "017_00":"Pidgeotto",
  "018_00":"Pidgeot",
  "019_00":"Rattata",
  "020_00":"Raticate",
  "021_00":"Spearow",
  "022_00":"Fearow",
  "023_00":"Ekans",
  "024_00":"Arbok",
  "025_00":"Pikachu",
  "026_00":"Raichu",
  "027_00":"Sandshrew",
  "028_00":"Sandslash",
  "029_00":"Nidoran-F",
  "030_00":"Nidorina",
  "031_00":"Nidoqueen",
  "032_00":"Nidoran-M",
  "033_00":"Nidorino",
  "034_00":"Nidoking",
  "035_00":"Clefairy",
  "036_00":"Clefable",
  "037_00":"Vulpix",
  "038_00":"Ninetales",
  "039_00":"Jigglypuff",
  "040_00":"Wigglytuff",
  "041_00":"Zubat",
  "042_00":"Golbat",
  "043_00":"Oddish",
  "044_00":"Gloom",
  "045_00":"Vileplume",
  "046_00":"Paras",
  "047_00":"Parasect",
  "048_00":"Venonat",
  "049_00":"Venomoth",
  "050_00":"Diglett",
  "051_00":"Dugtrio",
  "052_00":"Meowth",
  "053_00":"Persian",
  "054_00":"Psyduck",
  "055_00":"Golduck",
  "056_00":"Mankey",
  "057_00":"Primeape",
  "058_00":"Growlithe",
  "059_00":"Arcanine",
  "060_00":"Poliwag",
  "061_00":"Poliwhirl",
  "062_00":"Poliwrath",
  "063_00":"Abra",
  "064_00":"Kadabra",
  "065_00":"Alakazam",
  "066_00":"Machop",
  "067_00":"Machoke",
  "068_00":"Machamp",
  "069_00":"Bellsprout",
  "070_00":"Weepinbell",
  "071_00":"Victreebel",
  "072_00":"Tentacool",
  "073_00":"Tentacruel",
  "074_00":"Geodude",
  "075_00":"Graveler",
  "076_00":"Golem",
  "077_00":"Ponyta",
  "078_00":"Rapidash",
  "079_00":"Slowpoke",
  "080_00":"Slowbro",
  "081_00":"Magnemite",
  "082_00":"Magneton",
  "083_00":"Farfetch'd",
  "084_00":"Doduo",
  "085_00":"Dodrio",
  "086_00":"Seel",
  "087_00":"Dewgong",
  "088_00":"Grimer",
  "089_00":"Muk",
  "090_00":"Shellder",
  "091_00":"Cloyster",
  "092_00":"Gastly",
  "093_00":"Haunter",
  "094_00":"Gengar",
  "095_00":"Onix",
  "096_00":"Drowzee",
  "097_00":"Hypno",
  "098_00":"Krabby",
  "099_00":"Kingler",
  "100_00":"Voltorb",
  "101_00":"Electrode",
  "102_00":"Exeggcute",
  "103_00":"Exeggutor",
  "104_00":"Cubone",
  "105_00":"Marowak",
  "106_00":"Hitmonlee",
  "107_00":"Hitmonchan",
  "108_00":"Lickitung",
  "109_00":"Koffing",
  "110_00":"Weezing",
  "111_00":"Rhyhorn",
  "112_00":"Rhydon",
  "113_00":"Chansey",
  "114_00":"Tangela",
  "115_00":"Kangaskhan",
  "116_00":"Horsea",
  "117_00":"Seadra",
  "118_00":"Goldeen",
  "119_00":"Seaking",
  "120_00":"Staryu",
  "121_00":"Starmie",
  "122_00":"Mr-Mime",
  "123_00":"Scyther",
  "124_00":"Jynx",
  "125_00":"Electabuzz",
  "126_00":"Magmar",
  "127_00":"Pinsir",
  "128_00":"Tauros",
  "129_00":"Magikarp",
  "130_00":"Gyarados",
  "131_00":"Lapras",
  "132_00":"Ditto",
  "133_00":"Eevee",
  "134_00":"Vaporeon",
  "135_00":"Jolteon",
  "136_00":"Flareon",
  "137_00":"Porygon",
  "138_00":"Omanyte",
  "139_00":"Omastar",
  "140_00":"Kabuto",
  "141_00":"Kabutops",
  "142_00":"Aerodactyl",
  "143_00":"Snorlax",
  "144_00":"Articuno",
  "145_00":"Zapdos",
  "146_00":"Moltres",
  "147_00":"Dratini",
  "148_00":"Dragonair",
  "149_00":"Dragonite",
  "150_00":"Mewtwo",
  "151_00":"Mew",
  "152_00":"Chikorita",
  "153_00":"Bayleef",
  "154_00":"Meganium",
  "155_00":"Cyndaquil",
  "156_00":"Quilava",
  "157_00":"Typhlosion",
  "158_00":"Totodile",
  "159_00":"Croconaw",
  "160_00":"Feraligatr",
  "161_00":"Sentret",
  "162_00":"Furret",
  "163_00":"Hoothoot",
  "164_00":"Noctowl",
  "165_00":"Ledyba",
  "166_00":"Ledian",
  "167_00":"Spinarak",
  "168_00":"Ariados",
  "169_00":"Crobat",
  "170_00":"Chinchou",
  "171_00":"Lanturn",
  "172_00":"Pichu",
  "173_00":"Cleffa",
  "174_00":"Igglybuff",
  "175_00":"Togepi",
  "176_00":"Togetic",
  "177_00":"Natu",
  "178_00":"Xatu",
  "179_00":"Mareep",
  "180_00":"Flaaffy",
  "181_00":"Ampharos",
  "182_00":"Bellossom",
  "183_00":"Marill",
  "184_00":"Azumarill",
  "185_00":"Sudowoodo",
  "186_00":"Politoed",
  "187_00":"Hoppip",
  "188_00":"Skiploom",
  "189_00":"Jumpluff",
  "190_00":"Aipom",
  "191_00":"Sunkern",
  "192_00":"Sunflora",
  "193_00":"Yanma",
  "194_00":"Wooper",
  "195_00":"Quagsire",
  "196_00":"Espeon",
  "197_00":"Umbreon",
  "198_00":"Murkrow",
  "199_00":"Slowking",
  "200_00":"Misdreavus",
  "201_00":"Unown",
  "202_00":"Wobbuffet",
  "203_00":"Girafarig",
  "204_00":"Pineco",
  "205_00":"Forretress",
  "206_00":"Dunsparce",
  "207_00":"Gligar",
  "208_00":"Steelix",
  "209_00":"Snubbull",
  "210_00":"Granbull",
  "211_00":"Qwilfish",
  "212_00":"Scizor",
  "213_00":"Shuckle",
  "214_00":"Heracross",
  "215_00":"Sneasel",
  "216_00":"Teddiursa",
  "217_00":"Ursaring",
  "218_00":"Slugma",
  "219_00":"Magcargo",
  "220_00":"Swinub",
  "221_00":"Piloswine",
  "222_00":"Corsola",
  "223_00":"Remoraid",
  "224_00":"Octillery",
  "225_00":"Delibird",
  "226_00":"Mantine",
  "227_00":"Skarmory",
  "228_00":"Houndour",
  "229_00":"Houndoom",
  "230_00":"Kingdra",
  "231_00":"Phanpy",
  "232_00":"Donphan",
  "233_00":"Porygon2",
  "234_00":"Stantler",
  "235_00":"Smeargle",
  "236_00":"Tyrogue",
  "237_00":"Hitmontop",
  "238_00":"Smoochum",
  "239_00":"Elekid",
  "240_00":"Magby",
  "241_00":"Miltank",
  "242_00":"Blissey",
  "243_00":"Raikou",
  "244_00":"Entei",
  "245_00":"Suicune",
  "246_00":"Larvitar",
  "247_00":"Pupitar",
  "248_00":"Tyranitar",
  "249_00":"Lugia",
  "250_00":"Ho-Oh",
  "251_00":"Celebi",
  "252_00":"Treecko",
  "253_00":"Grovyle",
  "254_00":"Sceptile",
  "255_00":"Torchic",
  "256_00":"Combusken",
  "257_00":"Blaziken",
  "258_00":"Mudkip",
  "259_00":"Marshtomp",
  "260_00":"Swampert",
  "261_00":"Poochyena",
  "262_00":"Mightyena",
  "263_00":"Zigzagoon",
  "264_00":"Linoone",
  "265_00":"Wurmple",
  "266_00":"Silcoon",
  "267_00":"Beautifly",
  "268_00":"Cascoon",
  "269_00":"Dustox",
  "270_00":"Lotad",
  "271_00":"Lombre",
  "272_00":"Ludicolo",
  "273_00":"Seedot",
  "274_00":"Nuzleaf",
  "275_00":"Shiftry",
  "276_00":"Taillow",
  "277_00":"Swellow",
  "278_00":"Wingull",
  "279_00":"Pelipper",
  "280_00":"Ralts",
  "281_00":"Kirlia",
  "282_00":"Gardevoir",
  "283_00":"Surskit",
  "284_00":"Masquerain",
  "285_00":"Shroomish",
  "286_00":"Breloom",
  "287_00":"Slakoth",
  "288_00":"Vigoroth",
  "289_00":"Slaking",
  "290_00":"Nincada",
  "291_00":"Ninjask",
  "292_00":"Shedinja",
  "293_00":"Whismur",
  "294_00":"Loudred",
  "295_00":"Exploud",
  "296_00":"Makuhita",
  "297_00":"Hariyama",
  "298_00":"Azurill",
  "299_00":"Nosepass",
  "300_00":"Skitty",
  "301_00":"Delcatty",
  "302_00":"Sableye",
  "303_00":"Mawile",
  "304_00":"Aron",
  "305_00":"Lairon",
  "306_00":"Aggron",
  "307_00":"Meditite",
  "308_00":"Medicham",
  "309_00":"Electrike",
  "310_00":"Manectric",
  "311_00":"Plusle",
  "312_00":"Minun",
  "313_00":"Volbeat",
  "314_00":"Illumise",
  "315_00":"Roselia",
  "316_00":"Gulpin",
  "317_00":"Swalot",
  "318_00":"Carvanha",
  "319_00":"Sharpedo",
  "320_00":"Wailmer",
  "321_00":"Wailord",
  "322_00":"Numel",
  "323_00":"Camerupt",
  "324_00":"Torkoal",
  "325_00":"Spoink",
  "326_00":"Grumpig",
  "327_00":"Spinda",
  "328_00":"Trapinch",
  "329_00":"Vibrava",
  "330_00":"Flygon",
  "331_00":"Cacnea",
  "332_00":"Cacturne",
  "333_00":"Swablu",
  "334_00":"Altaria",
  "335_00":"Zangoose",
  "336_00":"Seviper",
  "337_00":"Lunatone",
  "338_00":"Solrock",
  "339_00":"Barboach",
  "340_00":"Whiscash",
  "341_00":"Corphish",
  "342_00":"Crawdaunt",
  "343_00":"Baltoy",
  "344_00":"Claydol",
  "345_00":"Lileep",
  "346_00":"Cradily",
  "347_00":"Anorith",
  "348_00":"Armaldo",
  "349_00":"Feebas",
  "350_00":"Milotic",
  "351_00":"Castform",
  "352_00":"Kecleon",
  "353_00":"Shuppet",
  "354_00":"Banette",
  "355_00":"Duskull",
  "356_00":"Dusclops",
  "357_00":"Tropius",
  "358_00":"Chimecho",
  "359_00":"Absol",
  "360_00":"Wynaut",
  "361_00":"Snorunt",
  "362_00":"Glalie",
  "363_00":"Spheal",
  "364_00":"Sealeo",
  "365_00":"Walrein",
  "366_00":"Clamperl",
  "367_00":"Huntail",
  "368_00":"Gorebyss",
  "369_00":"Relicanth",
  "370_00":"Luvdisc",
  "371_00":"Bagon",
  "372_00":"Shelgon",
  "373_00":"Salamence",
  "374_00":"Beldum",
  "375_00":"Metang",
  "376_00":"Metagross",
  "377_00":"Regirock",
  "378_00":"Regice",
  "379_00":"Registeel",
  "380_00":"Latias",
  "381_00":"Latios",
  "382_00":"Kyogre",
  "383_00":"Groudon",
  "384_00":"Rayquaza",
  "385_00":"Jirachi",
  #"386_11":"Deoxys",
  "387_00":"Turtwig",
  "388_00":"Grotle",
  "389_00":"Torterra",
  "390_00":"Chimchar",
  "391_00":"Monferno",
  "392_00":"Infernape",
  "393_00":"Piplup",
  "394_00":"Prinplup",
  "395_00":"Empoleon",
  "396_00":"Starly",
  "397_00":"Staravia",
  "398_00":"Staraptor",
  "399_00":"Bidoof",
  "400_00":"Bibarel",
  "401_00":"Kricketot",
  "402_00":"Kricketune",
  "403_00":"Shinx",
  "404_00":"Luxio",
  "405_00":"Luxray",
  "406_00":"Budew",
  "407_00":"Roserade",
  "408_00":"Cranidos",
  "409_00":"Rampardos",
  "410_00":"Shieldon",
  "411_00":"Bastiodon",
  "412_00":"Burmy",
  "413_00":"Wormadam",
  "414_00":"Mothim",
  "415_00":"Combee",
  "416_00":"Vespiquen",
  "417_00":"Pachirisu",
  "418_00":"Buizel",
  "419_00":"Floatzel",
  "420_00":"Cherubi",
  "421_00":"Cherrim",
  "422_00":"Shellos",
  "423_00":"Gastrodon",
  "424_00":"Ambipom",
  "425_00":"Drifloon",
  "426_00":"Drifblim",
  "427_00":"Buneary",
  "428_00":"Lopunny",
  "429_00":"Mismagius",
  "430_00":"Honchkrow",
  "431_00":"Glameow",
  "432_00":"Purugly",
  "433_00":"Chingling",
  "434_00":"Stunky",
  "435_00":"Skuntank",
  "436_00":"Bronzor",
  "437_00":"Bronzong",
  "438_00":"Bonsly",
  "439_00":"Mime-Jr.",
  "440_00":"Happiny",
  "441_00":"Chatot",
  "442_00":"Spiritomb",
  "443_00":"Gible",
  "444_00":"Gabite",
  "445_00":"Garchomp",
  "446_00":"Munchlax",
  "447_00":"Riolu",
  "448_00":"Lucario",
  "449_00":"Hippopotas",
  "450_00":"Hippowdon",
  "451_00":"Skorupi",
  "452_00":"Drapion",
  "453_00":"Croagunk",
  "454_00":"Toxicroak",
  "455_00":"Carnivine",
  "456_00":"Finneon",
  "457_00":"Lumineon",
  "458_00":"Mantyke",
  "459_00":"Snover",
  "460_00":"Abomasnow",
  "461_00":"Weavile",
  "462_00":"Magnezone",
  "463_00":"Lickilicky",
  "464_00":"Rhyperior",
  "465_00":"Tangrowth",
  "466_00":"Electivire",
  "467_00":"Magmortar",
  "468_00":"Togekiss",
  "469_00":"Yanmega",
  "470_00":"Leafeon",
  "471_00":"Glaceon",
  "472_00":"Gliscor",
  "473_00":"Mamoswine",
  "474_00":"Porygon-Z",
  "475_00":"Gallade",
  "476_00":"Probopass",
  "477_00":"Dusknoir",
  "478_00":"Froslass",
  "479_00":"Rotom",
  "480_00":"Uxie",
  "481_00":"Mesprit",
  "482_00":"Azelf",
  "483_00":"Dialga",
  "484_00":"Palkia",
  "485_00":"Heatran",
  "486_00":"Regigigas",
  #"487_00":"Giratina",
  "488_00":"Cresselia",
  "489_00":"Phione",
  "490_00":"Manaphy",
  "491_00":"Darkrai",
  "492_00":"Shaymin",
  "493_00":"Arceus",
  "494_00":"Victini",
  "495_00":"Snivy",
  "496_00":"Servine",
  "497_00":"Serperior",
  "498_00":"Tepig",
  "499_00":"Pignite",
  "500_00":"Emboar",
  "501_00":"Oshawott",
  "502_00":"Dewott",
  "503_00":"Samurott",
  "504_00":"Patrat",
  "505_00":"Watchog",
  "506_00":"Lillipup",
  "507_00":"Herdier",
  "508_00":"Stoutland",
  "509_00":"Purrloin",
  "510_00":"Liepard",
  "511_00":"Pansage",
  "512_00":"Simisage",
  "513_00":"Pansear",
  "514_00":"Simisear",
  "515_00":"Panpour",
  "516_00":"Simipour",
  "517_00":"Munna",
  "518_00":"Musharna",
  "519_00":"Pidove",
  "520_00":"Tranquill",
  "521_00":"Unfezant",
  "522_00":"Blitzle",
  "523_00":"Zebstrika",
  "524_00":"Roggenrola",
  "525_00":"Boldore",
  "526_00":"Gigalith",
  "527_00":"Woobat",
  "528_00":"Swoobat",
  "529_00":"Drilbur",
  "530_00":"Excadrill",
  "531_00":"Audino",
  "532_00":"Timburr",
  "533_00":"Gurdurr",
  "534_00":"Conkeldurr",
  "535_00":"Tympole",
  "536_00":"Palpitoad",
  "537_00":"Seismitoad",
  "538_00":"Throh",
  "539_00":"Sawk",
  "540_00":"Sewaddle",
  "541_00":"Swadloon",
  "542_00":"Leavanny",
  "543_00":"Venipede",
  "544_00":"Whirlipede",
  "545_00":"Scolipede",
  "546_00":"Cottonee",
  "547_00":"Whimsicott",
  "548_00":"Petilil",
  "549_00":"Lilligant",
  "550_00":"Basculin",
  "551_00":"Sandile",
  "552_00":"Krokorok",
  "553_00":"Krookodile",
  "554_00":"Darumaka",
  "555_00":"Darmanitan",
  "556_00":"Maractus",
  "557_00":"Dwebble",
  "558_00":"Crustle",
  "559_00":"Scraggy",
  "560_00":"Scrafty",
  "561_00":"Sigilyph",
  "562_00":"Yamask",
  "563_00":"Cofagrigus",
  "564_00":"Tirtouga",
  "565_00":"Carracosta",
  "566_00":"Archen",
  "567_00":"Archeops",
  "568_00":"Trubbish",
  "569_00":"Garbodor",
  "570_00":"Zorua",
  "571_00":"Zoroark",
  "572_00":"Minccino",
  "573_00":"Cinccino",
  "574_00":"Gothita",
  "575_00":"Gothorita",
  "576_00":"Gothitelle",
  "577_00":"Solosis",
  "578_00":"Duosion",
  "579_00":"Reuniclus",
  "580_00":"Ducklett",
  "581_00":"Swanna",
  "582_00":"Vanillite",
  "583_00":"Vanillish",
  "584_00":"Vanilluxe",
  "585_00":"Deerling",
  "586_00":"Sawsbuck",
  "587_00":"Emolga",
  "588_00":"Karrablast",
  "589_00":"Escavalier",
  "590_00":"Foongus",
  "591_00":"Amoonguss",
  "592_00":"Frillish",
  "593_00":"Jellicent",
  "594_00":"Alomomola",
  "595_00":"Joltik",
  "596_00":"Galvantula",
  "597_00":"Ferroseed",
  "598_00":"Ferrothorn",
  "599_00":"Klink",
  "600_00":"Klang",
  "601_00":"Klinklang",
  "602_00":"Tynamo",
  "603_00":"Eelektrik",
  "604_00":"Eelektross",
  "605_00":"Elgyem",
  "606_00":"Beheeyem",
  "607_00":"Litwick",
  "608_00":"Lampent",
  "609_00":"Chandelure",
  "610_00":"Axew",
  "611_00":"Fraxure",
  "612_00":"Haxorus",
  "613_00":"Cubchoo",
  "614_00":"Beartic",
  "615_00":"Cryogonal",
  "616_00":"Shelmet",
  "617_00":"Accelgor",
  "618_00":"Stunfisk",
  "619_00":"Mienfoo",
  "620_00":"Mienshao",
  "621_00":"Druddigon",
  "622_00":"Golett",
  "623_00":"Golurk",
  "624_00":"Pawniard",
  "625_00":"Bisharp",
  "626_00":"Bouffalant",
  "627_00":"Rufflet",
  "628_00":"Braviary",
  "629_00":"Vullaby",
  "630_00":"Mandibuzz",
  "631_00":"Heatmor",
  "632_00":"Durant",
  "633_00":"Deino",
  "634_00":"Zweilous",
  "635_00":"Hydreigon",
  "636_00":"Larvesta",
  "637_00":"Volcarona",
  "638_00":"Cobalion",
  "639_00":"Terrakion",
  "640_00":"Virizion",
  #"641_00":"Tornadus",
  #"642_00":"Thundurus",
  "643_00":"Reshiram",
  "644_00":"Zekrom",
  #"645_00":"Landorus",
  "646_11":"Kyurem",
  "647_00":"Keldeo",
  "648_00":"Meloetta",
  "649_00":"Genesect",
  "650_00":"Chespin",
  "651_00":"Quilladin",
  "652_00":"Chesnaught",
  "653_00":"Fennekin",
  "654_00":"Braixen",
  "655_00":"Delphox",
  "656_00":"Froakie",
  "657_00":"Frogadier",
  "658_00":"Greninja",
  "659_00":"Bunnelby",
  "660_00":"Diggersby",
  "661_00":"Fletchling",
  "662_00":"Fletchinder",
  "663_00":"Talonflame",
  "664_00":"Scatterbug",
  "665_00":"Spewpa",
  "666_00":"Vivillon",
  "667_00":"Litleo",
  "668_00":"Pyroar",
  "669_00":"Flabébé",
  "670_00":"Floette",
  "671_00":"Florges",
  "672_00":"Skiddo",
  "673_00":"Gogoat",
  "674_00":"Pancham",
  "675_00":"Pangoro",
  "676_00":"Furfrou",
  "677_00":"Espurr",
  "678_00":"Meowstic",
  "679_00":"Honedge",
  "680_00":"Doublade",
  "681_00":"Aegislash",
  "682_00":"Spritzee",
  "683_00":"Aromatisse",
  "684_00":"Swirlix",
  "685_00":"Slurpuff",
  "686_00":"Inkay",
  "687_00":"Malamar",
  "688_00":"Binacle",
  "689_00":"Barbaracle",
  "690_00":"Skrelp",
  "691_00":"Dragalge",
  "692_00":"Clauncher",
  "693_00":"Clawitzer",
  "694_00":"Helioptile",
  "695_00":"Heliolisk",
  "696_00":"Tyrunt",
  "697_00":"Tyrantrum",
  "698_00":"Amaura",
  "699_00":"Aurorus",
  "700_00":"Sylveon",
  "701_00":"Hawlucha",
  "702_00":"Dedenne",
  "703_00":"Carbink",
  "704_00":"Goomy",
  "705_00":"Sliggoo",
  "706_00":"Goodra",
  "707_00":"Klefki",
  "708_00":"Phantump",
  "709_00":"Trevenant",
  "710_00":"Pumpkaboo",
  "711_00":"Gourgeist",
  "712_00":"Bergmite",
  "713_00":"Avalugg",
  "714_00":"Noibat",
  "715_00":"Noivern",
  "716_00":"Xerneas",
  "717_00":"Yveltal",
  "718_00":"Zygarde",
  "719_00":"Diancie",
  "720_00":"Hoopa",
  "721_00":"Volcanion",
  "722_00":"Rowlet",
  "723_00":"Dartrix",
  "724_00":"Decidueye",
  "725_00":"Litten",
  "726_00":"Torracat",
  "727_00":"Incineroar",
  "728_00":"Popplio",
  "729_00":"Brionne",
  "730_00":"Primarina",
  "731_00":"Pikipek",
  "732_00":"Trumbeak",
  "733_00":"Toucannon",
  "734_00":"Yungoos",
  "735_00":"Gumshoos",
  "736_00":"Grubbin",
  "737_00":"Charjabug",
  "738_00":"Vikavolt",
  "739_00":"Crabrawler",
  "740_00":"Crabominable",
  "741_00":"Oricorio",
  "742_00":"Cutiefly",
  "743_00":"Ribombee",
  "744_00":"Rockruff",
  "745_00":"Lycanroc",
  "746_00":"Wishiwashi",
  "747_00":"Mareanie",
  "748_00":"Toxapex",
  "749_00":"Mudbray",
  "750_00":"Mudsdale",
  "751_00":"Dewpider",
  "752_00":"Araquanid",
  "753_00":"Fomantis",
  "754_00":"Lurantis",
  "755_00":"Morelull",
  "756_00":"Shiinotic",
  "757_00":"Salandit",
  "758_00":"Salazzle",
  "759_00":"Stufful",
  "760_00":"Bewear",
  "761_00":"Bounsweet",
  "762_00":"Steenee",
  "763_00":"Tsareena",
  "764_00":"Comfey",
  "765_00":"Oranguru",
  "766_00":"Passimian",
  "767_00":"Wimpod",
  "768_00":"Golisopod",
  "769_00":"Sandygast",
  "770_00":"Palossand",
  "771_00":"Pyukumuku",
  "772_00":"Type:-Null",
  "773_00":"Silvally",
  "774_00":"Minior",
  "775_00":"Komala",
  "776_00":"Turtonator",
  "777_00":"Togedemaru",
  "778_00":"Mimikyu",
  "779_00":"Bruxish",
  "780_00":"Drampa",
  "781_00":"Dhelmise",
  "782_00":"Jangmo-o",
  "783_00":"Hakamo-o",
  "784_00":"Kommo-o",
  "785_00":"Tapu-Koko",
  "786_00":"Tapu-Lele",
  "787_00":"Tapu-Bulu",
  "788_00":"Tapu-Fini",
  "789_00":"Cosmog",
  "790_00":"Cosmoem",
  "791_00":"Solgaleo",
  "792_00":"Lunala",
  "793_00":"Nihilego",
  "794_00":"Buzzwole",
  "795_00":"Pheromosa",
  "796_00":"Xurkitree",
  "797_00":"Celesteela",
  "798_00":"Kartana",
  "799_00":"Guzzlord",
  "800_00":"Necrozma",
  "801_00":"Magearna",
  "802_00":"Marshadow",
  "803_00":"Poipole",
  "804_00":"Naganadel",
  "805_00":"Stakataka",
  "806_00":"Blacephalon",
  "807_00":"Zeraora",
  "808_00":"Meltan",
  "809_00":"Melmetal",
  "810_00":"Grookey",
  "811_00":"Thwackey",
  "812_00":"Rillaboom",
  "813_00":"Scorbunny",
  "814_00":"Raboot",
  "815_00":"Cinderace",
  "816_00":"Sobble",
  "817_00":"Drizzile",
  "818_00":"Inteleon",
  "819_00":"Skwovet",
  "820_00":"Greedent",
  "821_00":"Rookidee",
  "822_00":"Corvisquire",
  "823_00":"Corviknight",
  "824_00":"Blipbug",
  "825_00":"Dottler",
  "826_00":"Orbeetle",
  "827_00":"Nickit",
  "828_00":"Thievul",
  "829_00":"Gossifleur",
  "830_00":"Eldegoss",
  "831_00":"Wooloo",
  "832_00":"Dubwool",
  "833_00":"Chewtle",
  "834_00":"Drednaw",
  "835_00":"Yamper",
  "836_00":"Boltund",
  "837_00":"Rolycoly",
  "838_00":"Carkol",
  "839_00":"Coalossal",
  "840_00":"Applin",
  "841_00":"Flapple",
  "842_00":"Appletun",
  "843_00":"Silicobra",
  "844_00":"Sandaconda",
  "845_00":"Cramorant",
  "846_00":"Arrokuda",
  "847_00":"Barraskewda",
  "848_00":"Toxel",
  "849_00":"Toxtricity",
  "850_00":"Sizzlipede",
  "851_00":"Centiskorch",
  "852_00":"Clobbopus",
  "853_00":"Grapploct",
  "854_00":"Sinistea",
  "855_00":"Polteageist",
  "856_00":"Hatenna",
  "857_00":"Hattrem",
  "858_00":"Hatterene",
  "859_00":"Impidimp",
  "860_00":"Morgrem",
  "861_00":"Grimmsnarl",
  "862_00":"Obstagoon",
  "863_00":"Perrserker",
  "864_00":"Cursola",
  "865_00":"Sirfetch’d",
  "866_00":"Mr-Rime",
  "867_00":"Runerigus",
  "868_00":"Milcery",
  "869_00":"Alcremie",
  "870_00":"Falinks",
  "871_00":"Pincurchin",
  "872_00":"Snom",
  "873_00":"Frosmoth",
  "874_00":"Stonjourner",
  "875_00":"Eiscue",
  "876_00":"Indeedee",
  "877_00":"Morpeko",
  "878_00":"Cufant",
  "879_00":"Copperajah",
  "880_00":"Dracozolt",
  "881_00":"Arctozolt",
  "882_00":"Dracovish",
  "883_00":"Arctovish",
  "884_00":"Duraludon",
  "885_00":"Dreepy",
  "886_00":"Drakloak",
  "887_00":"Dragapult",
  "888_00":"Zacian",
  "889_00":"Zamazenta",
  "890_00":"Eternatus",
  "891_00":"Kubfu",
  "892_00":"Urshifu",
  "893_00":"Zarude",
}

MEGA_DEX =\
{
  "003_51":"Venusaur",
  "006_51":"Charizard-X",
  "006_52":"Charizard-Y",
  "009_51":"Blastoise",
  "65_51":"Alakazam",
  "094_51":"Gengar",
  "115_51":"Kangaskhan",
  "127_51":"Pinsir",
  "130_51":"Gyarados",
  "142_51":"Aerodactyl",
  "150_51":"Mewtwo-X",
  "150_52":"Mewtwo-Y",
  "181_51":"Ampharos",
  "212_51":"Scizor",
  "214_51":"Heracross",
  "229_51":"Houndoom",
  "248_51":"Tyranitar",
  "257_51":"Blaziken",
  "282_51":"Gardevoir",
  "303_51":"Mawile",
  "306_51":"Aggron",
  "308_51":"Medicham",
  "310_51":"Manectric",
  "359_51":"Absol",
  "380_51":"Latias",
  "381_51":"Latios",
  "445_51":"Garchomp",
  "448_51":"Lucario",
  "460_51":"Abomasnow",
  "015_51":"Beedrill",
  "018_51":"Pidgeot",
  "80_51":"Slowbro",
  "208_51":"Steelix",
  "254_51":"Sceptile",
  "260_51":"Swampert",
  "302_51":"Sableye",
  "319_51":"Sharpedo",
  "323_51":"Camerupt",
  "334_51":"Altaria",
  "362_51":"Glalie",
  "373_51":"Salamence",
  "376_51":"Metagross",
  "384_51":"Rayquaza",
  "428_51":"Lopunny",
  "475_51":"Gallade",
  "531_51":"Audino",
  "719_51":"Diancie"
}

ALOLAN_DEX =\
{
  "019_61":"Alolan-Rattata",
  "020_61":"Alolan-Raticate",
  "026_61":"Alolan-Raichu",
  "027_61":"Alolan-Sandshrew",
  "028_61":"Alolan-Sandslash",
  "037_61":"Alolan-Vulpix",
  "038_61":"Alolan-Ninetales",
  "050_61":"Alolan-Diglett",
  "051_61":"Alolan-Dugtrio",
  "052_61":"Alolan-Meowth",
  "053_61":"Alolan-Persian",
  "074_61":"Alolan-Geodude",
  "075_61":"Alolan-Graveler",
  "076_61":"Alolan-Golem",
  "088_61":"Alolan-Grimer",
  "089_61":"Alolan-Muk",
  "103_61":"Alolan-Exeggutor",
  "105_61":"Alolan-Marowak"
}

GALARIAN_DEX =\
{
  "052_31":"Galarian-Meowth",
  "077_31":"Galarian-Ponyta",
  "078_31":"Galarian-Rapidash",
  "079_31":"Galarian-Slowpoke",
  "080_31":"Galarian-Slowbro",
  "083_31":"Galarian-Farfetch'd",
  "110_31":"Galarian-Weezing",
  "122_31":"Galarian-Mr-Mime",
  "144_31":"Galarian-Articuno",
  "145_31":"Galarian-Zapdos",
  "146_31":"Galarian-Moltres",
  "222_31":"Galarian-Corsola",
  "263_31":"Galarian-Zigzagoon",
  "264_31":"Galarian-Linoone",
  "554_31":"Galarian-Darumaka",
  "555_31":"Galarian-Darmanitan",
  "562_31":"Galarian-Yamask",
  "618_31":"Galarian-Stunfisk"
}

ALTERNATE_FORME_DEX =\
{
  "386_12":"Deoxys-Attack",
  "386_13":"Deoxys-Defense",
  "386_14":"Deoxys-Speed",
  "487_12":"Giratina-Origin",
  "487_11":"Giratina-Altered",
  "645_11":"Landorus-Incarnate",
  "645_12":"Landorus-Therian",
  "641_11":"Tornadus-Incarnate",
  "641_12":"Tornadus-Therian",
  "642_11":"Thundurus-Incarnate",
  "642_12":"Thundurus-Therian"
}

RAID_COUNTER_GUIDE =\
{
  "Lugia":"https://cdn.discordapp.com/attachments/773944383765741578/773944587567628338/Screenshot_2031.png",
  "Virizion":"https://cdn.discordapp.com/attachments/773944383765741578/777909650821480468/20201116_094935.png",
  "Terrakion":"https://cdn.discordapp.com/attachments/773944383765741578/777909650569035786/20201116_094747.png",
  "Cobalion":"https://cdn.discordapp.com/attachments/773944383765741578/777909650279759872/20201116_094457.png",
  "Kyurem":"https://media.discordapp.net/attachments/773944383765741578/783342291489128448/20201201_093937.png",
  "Regirock":"https://media.discordapp.net/attachments/773944383765741578/786995722720509981/20201211_113941.png",
  "Registeel":"https://media.discordapp.net/attachments/773944383765741578/789523556329193482/20201218_110403.png",
  "Ho-Oh":"https://media.discordapp.net/attachments/773944383765741578/794608585916022794/20210101_115014.png",
  "Heatran":"https://media.discordapp.net/attachments/773944383765741578/798418704475357184/20210112_000440.png",
  "Landorus-Incarnate":"https://cdn.discordapp.com/attachments/773944383765741578/815658935955750962/20210228_135615.png",
  "Tornadus-Incarnate":"https://cdn.discordapp.com/attachments/773944383765741578/817504573118873700/20210305_160950.png",
  "Thundurus-Incarnate":"https://cdn.discordapp.com/attachments/773944383765741578/819405478479134730/20210310_220406.png"
}

POKEBATTLER_LINK =\
{
  "Lugia":"https://www.pokebattler.com/raids/LUGIA",
  "Virizion":"https://www.pokebattler.com/raids/Virizion",
  "Terrakion":"https://www.pokebattler.com/raids/Terrakion",
  "Cobalion":"https://www.pokebattler.com/raids/Cobalion",
  "Kyurem":"https://www.pokebattler.com/raids/Kyurem"
}

NAME_TO_POKEBATTLER_ID =\
{
  "Charizard-X":"CHARIZARD_MEGA_X",
  "Charizard-Y":"CHARIZARD_MEGA_Y",
  "Mewtwo-X":"MEWTWO_MEGA_X",
  "Mewtwo-Y":"MEWTWO_MEGA_Y",
  "Nidoran-M":"NIDORAN_MALE",
  "Nidoran-F":"NIDORAN_FEMALE",
  "Giratina-Altered":"GIRATINA",
}
