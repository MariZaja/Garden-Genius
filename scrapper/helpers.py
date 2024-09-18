import json

def get_first_x_ids(data, x):
    if isinstance(data, str):
        data = json.loads(data)

    ids = [entry['id'] for entry in data['data'][:x]]
    return ids

def read_key() -> str:
    try:
        with open('KEY.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("KEY.txt file not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return ""