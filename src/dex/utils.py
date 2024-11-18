import json

def json_parse(json_str: str):
    try:
        return json.loads(json_str)
    except Exception as er:
        
        print(er)

        return None