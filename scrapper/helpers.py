import json

def read_key() -> str:
    try:
        with open('KEY.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("KEY.txt file not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return ""

def read_keys() -> list:
    keys = []
    try:
        with open('KEYS.txt', 'r') as file:
            keys = file.read().splitlines()
    except FileNotFoundError:
        print("KEYS.txt file not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return keys