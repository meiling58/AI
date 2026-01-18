from google import genai
import common


default_file = 'genAI.txt'      # Replace with your actual file path
default_env = 'GENAI_API_KEY'   # Replace with your actual environment variable name


def get_genai_client(source='file'):
    if source == 'file':
        key = common.get_api_key(default_file, 'file')
    elif source == 'env':
        key = common.get_api_key(default_env, 'env')
    return genai.Client(api_key=key)


def get_text_search(text, source='file'):
    client = get_genai_client(source)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text
        ).text
    return response


def get_python_function(des, source='file'):
    client = get_genai_client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=des,
    ).text
    return response
