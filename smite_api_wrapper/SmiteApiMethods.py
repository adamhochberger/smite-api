class HirezApiMethods:
    # Connectivity, Development, And System Status
    PING = "/ping{ResponseFormat}"
    CREATE_SESSION = "/createsession{ResponseFormat}/{developerId}/{signature}/{timestamp}"
    TEST_SESSION = "/testsession[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}"
    GET_DATA_USED = "/getdataused[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}"
    GET_HIREZ_SERVER_STATUS = "/gethirezserverstatus[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}"
    GET_PATCH_INFO = "/getpatchinfo[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}"


class SmiteApiMethods(HirezApiMethods):
    # Gods, And Items
    GET_GODS = "/getgods[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languageCode}"
    GET_GOD_LEADERBOARD = "/getgodleaderboard[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{godId}/{queue}"  # only queues 440, 450, 451


class PaladinsApiMethods(HirezApiMethods):
    # Champions, And Items
    GET_CHAMPIONS = "/getchampions[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languageCode}"
    GET_CHAMPION_CARDS = "/getchampions[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{languageCode}"
    GET_CHAMPION_LEADERBOARD = "/getchampionleaderboard[ResponseFormat]/{developerId}/{signature}/{session}/{timestamp}/{championId}/{queue}"  # only queue 428


def get_list_of_params(method_name: str):
    list_of_params = []

    temp_string = ""
    should_read_letters = False

    for char in method_name:
        if char == "{":
            should_read_letters = True
            continue

        if char == "}":
            should_read_letters = False
            list_of_params.append(temp_string)
            temp_string = ""

        if should_read_letters:
            temp_string += char

    return list_of_params
