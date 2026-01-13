from openai import OpenAI
import common


def get_openai_client(source='file'):
    if source == 'file':
        key = common.get_api_key('openAI.txt', 'file')
    elif source == 'env':
        key = common.get_api_key('openAI', 'env')
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
