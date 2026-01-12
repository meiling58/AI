"""
Store methods can be use under aiApi
"""


def get_file_content(file):
    try:
        with open(file, 'r') as file:
            file_content_string = file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return file_content_string
