import json

def load_json(file_path: str):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_json(file_path: str, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)