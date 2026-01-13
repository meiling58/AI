# AI API
This AI project uses the api call to communicate with AI.

## Overview
- Free version:
  - genAI(google Gemini):
    - [Documentation](https://ai.google.dev/gemini-api/docs)
    - [Google Gen AI SDK](https://googleapis.github.io/python-genai/)
  - openAI(ChatGPT)
    - [Documentation](https://openai.com/api/)
    - [openAI API SDK](https://platform.openai.com/docs/libraries)
    - [openAI gitHub](https://github.com/openai/openai-python)

- Other (may not free):
  - Claude(Antropics):
    - [Documentation](https://platform.claude.com/docs/en/home)
    - [Anthropic SDK](https://github.com/anthropics/anthropic-sdk-python)
  - Llama(Meta)
    - [Documentation-Home](https://www.llama.com/products/llama-api/)
    - [Documentation-API](https://llama.developer.meta.com/docs/overview/)
    - [llama SDK gitHub](https://github.com/meta-llama/llama-api-python)

## Folder Structure AI/aiAPi
- common.py, Store methods can be use under aiApi 
- [apiName].txt: 
  - openAI.txt, stores openAI api key.
  - genAI.txt, stores genAI api key.
- [aiName].py:
  - openAI.py, stores the openAi api functions
  - genAI.txt, stores the genAi api functions
- /Tests/[testName].py, store test code
