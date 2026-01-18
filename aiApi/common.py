"""
Store methods can be use under aiApi
"""
import os


def get_file_content(file):
    try:
        with open(file, 'r') as file:
            file_content_string = file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return file_content_string


def get_env_key(name):
    api_key = None
    try:
        api_key = os.environ.get(name)
        # print(f"API Key: {api_key}")
    except KeyError:
        print("Error: API_KEY environment variable not set.")
    return api_key


def get_api_key(name, source='file'):
    key_sources = {'file', 'env'}
    key = None
    if source in key_sources:
        if source == 'file':
            key = get_file_content(name)
        elif source == 'env':
            key = get_env_key(name)
    else:
        print(f"Error: {source} not a Valid sources, please use file or env")
    return key
