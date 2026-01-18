from openai import OpenAI
import common

default_file = 'openAI.txt'      # Replace with your actual file path
default_env = 'OPENAI_API_KEY'   # Replace with your actual environment variable name


def get_openai_client(source='file'):
    if source == 'file':
        key = common.get_api_key(default_file, 'file')
    elif source == 'env':
        key = common.get_api_key(default_env, 'env')
    return OpenAI(api_key=key)


def get_text_search(text, source='file'):
    client = get_openai_client(source)
    response = client.responses.create(
        model="gpt-5-nano",
        input=text
    ).output_text
    return response


def get_web_search(content, source='file'):
    client = get_openai_client()
    response = client.responses.create(
        model="gpt-5-nano",
        tools=[{"type": "web_search"}],
        input=content
    ).output_text
    return response


def get_python_function(des, source='file'):
    client = get_openai_client()
    response = client.responses.create(
        model="gpt-5-nano",
        input=des
    ).output_text
    return response
