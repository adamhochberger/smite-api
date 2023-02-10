
def get_method_name_from_api(api_name: str):
    should_start_processing_method_name = False
    method_name = ""

    for char in api_name:
        if char == "/":
            should_start_processing_method_name = True
            continue
        elif char == "{":
            return method_name

        if should_start_processing_method_name:
            method_name += char
