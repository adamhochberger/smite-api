class HirezApiMethods:
    # Connectivity, Development, And System Status
    PING = "/ping{ResponseFormat}"
    CREATE_SESSION = "/createsession{ResponseFormat}/{developerId}/{signature}/{timestamp}"
    TEST_SESSION = "/testsession{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"
    GET_DATA_USED = "/getdataused{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"
    GET_HIREZ_SERVER_STATUS = "/gethirezserverstatus{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"
    GET_PATCH_INFO = "/getpatchinfo{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"
    GET_PLAYER_WITH_PORTAL = "getplayer{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{player}/{portalId}" # 1:Hi-Rez, 5:Steam, 9:PS4, 10:Xbox, 22:Switch, 25:Discord, 28:Epic
    GET_PLAYER = "/getplayer{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{player}"
    GET_PLAYER_ID_BY_NAME = "/getplayeridbyname{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerName}"
    GET_PLAYER_ID_BY_PORTAL_USER_ID = "/getplayeridbyportaluserid{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{portalId}/{portalUserId}"
    GET_PLAYER_IDS_BY_GAMER_TAG = "/getplayeridsbygamertag{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{portalId}/{gamerTag}"
    GET_FRIENDS = "/getfriends{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerId}"
    GET_PLAYER_STATUS = "/getplayerstatus{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerId}" # 0-OFFLINE, 1-IN LOBBY, 2-IN SELECT, 3-IN GAME, 4-ONLINE, 5-UNKNOWN
    GET_MATCH_HISTORY = "/getmatchhistory{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerId}"
    GET_QUEUE_STATS = "/getqueuestats{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerId}/{queue}"
    SEARCH_PLAYERS = "/searchplayers{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{searchPlayer}"
    GET_DEMO_DETAILS = "/getdemodetails{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{matchId}"
    GET_MATCH_DETAILS = "/getmatchdetails{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{matchId}"
    GET_MATCH_DETAILS_BATCH = "/getmatchdetailsbatch{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{matchIdList}"
    GET_MATCH_IDS_BY_QUEUE = "/getmatchidsbyqueue{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{queue}/{date}/{hour}"
    GET_MATCH_PLAYER_DETAILS = "/getmatchplayerdetails{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{matchId}"
    GET_TOP_MATCHES = "/gettopmatches{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"

    # Leagues, Seasons, And Rounds
    GET_LEAGUE_LEADERBOARD = "/getleagueleaderboard{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{queue}/{tier}/{round}"
    GET_LEAGUE_SEASONS = "/getleagueseasons{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{queue}"

    # Team Info
    GET_TEAM_DETAILS = "/getteamdetails{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{clanId}"
    GET_TEAM_PLAYERS = "/getteamplayers{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{clanId}"
    SEARCH_TEAMS = "/searchteams{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{searchTeam}"

    # Other
    GET_ESPORTS_PRO_LEAGUE_DETAILS = "/getesportsproleaguedetails{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"
    GET_MOTD = "/getmotd{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"


class SmiteApiMethods(HirezApiMethods):
    # Gods, And Items
    GET_GODS = "/getgods{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{languageCode}"
    GET_GOD_LEADERBOARD = "/getgodleaderboard{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{godId}/{queue}"  # only queues 440, 450, 451
    GET_GOD_ALT_ABILITIES = "/getgodaltabilities{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"
    GET_GOD_SKINS = "/getgodskins{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}"
    GET_GOD_RECOMMENDED_ITEMS = "/getgodrecommendeditems{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{godId}/{languageCode}"
    GET_ITEMS = "/getitems{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{languagecode}"
    GET_GOD_RANKS = "/getgodranks{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerId}"
    GET_PLAYER_ACHIEVEMENTS = "/getplayerachievements{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerId}"


class PaladinsApiMethods(HirezApiMethods):
    # Champions, And Items
    GET_CHAMPIONS = "/getchampions{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{languageCode}"
    GET_CHAMPION_CARDS = "/getchampions{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{languageCode}"
    GET_CHAMPION_LEADERBOARD = "/getchampionleaderboard{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{championId}/{queue}"  # only queue 428
    GET_CHAMPION_SKINS = "/getchampionskins{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{championId}/{languageCode}"
    GET_CHAMPION_RECOMMENDED_ITEMS = "/getchampionecommendeditems{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{championId}/{languageCode}"
    GET_BOUNTY_ITEMS = "/getbountyitems{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"
    GET_PLAYER_BATCH = "/getplayerbatch{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerIdList}"
    GET_PLAYER_ID_INFO_FOR_XBOX_AND_SWITCH = "/getplayeridinfoforxboxandswitch{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerName}"
    GET_CHAMPION_RANKS = "/getchampionranks{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/{playerId}"
    GET_PLAYER_LOADOUTS = "/getplayerloadouts{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}/playerId}/{languageCode}"


def get_api_as_url(formatted_string):
    return "https://api.smitegame.com/smiteapi.svc" + formatted_string
