from google import genai
import common


def get_genai_client(source='file'):
    if source == 'file':
        key = common.get_api_key('genAI.txt', 'file')
    elif source == 'env':
        key = common.get_api_key('genAI', 'env')
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
