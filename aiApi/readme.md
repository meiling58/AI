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

## Where to store API keys
- Store the api keys in aiApi/[apiName].txt, for example, openAI.txt for openAI api key.
- Store the api keys in Environment Variables, for example, OPENAI_API_KEY for openAI api key.<br>

**Environment Variables has higher priority than the txt file.**<br>
**This project set up the file as default way to store the api keys.**<br>
- You can change the code in common.py to switch to "env", or replace (source='env') when using the methods.
- How to store the key in Environment Variables:
  - Windows:
    1. Open the Start Menu and search for "Environment Variables".
    2. Click on "Edit the system environment variables".
    3. In the System Properties window, click on the "Environment Variables" button.
    4. In the Environment Variables window, click on "New" under the "User variables" section.
    5. Enter the variable name (e.g., OPENAI_API_KEY) and the variable value (your API key).
    6. Click "OK" to save the new variable.
    7. Click "OK" again to close the Environment Variables window.
  - macOS/Linux:
    1. Open a terminal window.
    2. Use a text editor to open your shell profile file (e.g., ~/.bashrc, ~/.zshrc, or ~/.bash_profile).
    3. Add a new line to export your API key as an environment variable:
       ```bash
       export OPENAI_API_KEY="your_api_key_here"
       ```
    4. Save the file and exit the text editor.
    5. Run `source ~/.bashrc` (or the appropriate file) to apply the changes to your current terminal session.<br>

**Troubleshooting**: If the environment variable is not recognized, try restarting your terminal or IDE to ensure the changes take effect.