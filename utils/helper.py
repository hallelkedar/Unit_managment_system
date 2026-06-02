import json

def get_soldier_by_id(soldiers: dict, soldier_id: int):
    for soldier in soldiers:
            if soldier['id'] == soldier_id:
                return soldier
    return None

def write_back_to_json(data, file):
    file.seek(0)
    json.dump(data, file, indent=2)
    file.truncate()