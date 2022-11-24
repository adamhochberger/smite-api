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
