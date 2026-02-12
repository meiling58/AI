# Overview --In grogress...
 This repo including AI relating information and projects
 <details>
  <summary> Repo Structure </summary>
  TBD
 </details>

 <details>
  <summary>Projects</summary>

- [GitHubCopilotTest](https://github.com/meiling58/AI/tree/main/GitHubCopilotTest/readme.md): This project shows how to use GitHub Copilot with demo code.
- [aiAPi](https://github.com/meiling58/AI/blob/main/aiApi/readme.md): This project demos communicate AIs by using api .
- [myFirstAgentAI](https://github.com/meiling58/AI/blob/main/myFirstAgentAI/readme.md): This project including all basic knowledge and testing code for AI agents.
- [QAAgent](): TBD
- [searchEngine](): TBD
 </details>
<br>
QickLinks:

[ChatGPT](https://chatgpt.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Copilot](https://copilot.microsoft.com/), [Grok](https://grok.com/), [DeepSeek](https://chat.deepseek.com/), [Perplexity AI](https://www.perplexity.ai/), [Midjourney](https://www.midjourney.com/explore?tab=video_top), [Synthesia AI](https://www.synthesia.io/)
<br>

# AI 
Artificial intelligence (AI) is a field of computer science focused on building systems that can perform tasks 
normally require human intelligence, such as recognizing patterns, understanding language, making decisions, 
and solving problems. In simple terms, it means computers and machines using data and algorithms to learn 
from experience and then act or make recommendations on their own within specific tasks. ([wiki](https://en.wikipedia.org/wiki/Artificial_intelligence))

<details>

<summary>Popular AIs</summary>

- [ChatGPT (openAI)](https://chatgpt.com/)
- [Gemini (Google)](https://gemini.google.com/)
- [Claude (Anthropic)](https://claude.ai/)
- [Copilot (Microsoft)](https://copilot.microsoft.com/)
- [Grok (xAI)](https://grok.com/)
- [DeepSeek (DeepSeek)](https://chat.deepseek.com/)
- [Midjourney](https://www.midjourney.com/explore?tab=video_top)
- [Perplexity AI](https://www.perplexity.ai/)
- [Llama (Meta)](https://www.llama.com/)
- [Synthesia AI](https://www.synthesia.io/)
</details>
<details>
<summary>Comparison</summary>

- Manual searching "can you provide top 5 popular AIs" on chatGPT, Gemini, Claude, Copilot, Grok, Deepseek, Perplexity. 
  - No critical used, 5 points for 1st.
  - Final list
    1. ChatGPT, 5*7=35
    2. Gemini, 4*6+3=27
    3. Claude, 22
    4. Copilot, 7
    5. Grok, 4
    6. DeepSeek, 3
    7. Midjourney, 3
    8. Perplexity, 3
    9. Synthesia, 1
    10. Llama, 0
- Using Claude with prompt "provide the top popular AIs using borda ranking system methodology by search chatgpt, claude, Gemini, copilot, grok, deepseek"
  - critical used:
    - Overall Popularity/Market Share
    - Reasoning & Problem-Solving Ability
    - Coding Capabilities
    - Creative Writing
    - Multimodal Capabilities (images, voice, etc.)
    - Context Window/Long Conversations
    - Speed & Efficiency
    - Cost/Accessibility (free tier quality)
  - Final List
  
| Rank(total points) | AI         | Strengths                                            |
|--------------------|:-----------|:-----------------------------------------------------|
| 1 - 31 points      | ChatGPT    | Most Versatile, Balanced strength across all areas   |
| 2 - 29 points      | Claude     | Best for Developers, Superior coding and reasoning   |
| 3 - 27 points      | Gemini     | Best for Multimodal, images, video, audio handling   |
| 4 - 15 points      | DeepSeek   | Best Value/Efficiency, cost-effective, fast, capable |
| 5 - 11 points      | Copilot    | Most Integrated, works within Microsoft ecosystem    |
| 6 - 8 points       | Grok       | Most Unique, Personality and X integration           |

- Other
  - can add more specific criteria, likes API pricing, specific benchmark scores
  - create ranking for specific use cases, like best AI for students, for developers
  - using another ranking method, like copeland, TrueSkill or Elo

- Using Claude with "can you use Copeland instead"
  - same critical
  - Final List
  
| Rank   | AI         | Copeland Score | Wins | Losses | Record  |
|--------|:-----------|:---------------|------|--------|---------|
| 1      | ChatGPT    | +4.5           | 4.5  | 0.5    | 4.5-0.5 |
| 2(tie) | Claude     | +3.5           | 3.5  | 1.5    | 3.5-1.5 |
| 3(tie) | Gemini     | +3.5           | 3.5  | 1.5    | 3.5-1.5 |
| 4      | DeepSeek   | 0              | 2    | 2      | 2-3     |
| 5      | Copilot    | -2.5           | 1    | 3.5    | 1-4     |
| 6      | Grok       | -4.5           | 0    | 4.5    | 0-5     |
</details>

<details>
<summary>AI - For Python/Robot Framework developers</summary>

- Ask Claude with "using borda ranking system search all popular AIs with criteria, the best for developers who are using python/robot" <br>
- Result:<br>
  - Top AIs:
    - GitHub Copilot
    - Cursor
    - Claude (Anthropic)
    - Windsurf (formerly Codeium)
    - ChatGPT (OpenAI)
    - Qodo (formerly CodiumAI)
    - Tabnine
    - Amazon Q Developer (CodeWhisperer)
    - JetBrains AI Assistant
    - Aider
  - Criteria:
    - Python Code Generation Quality
    - Test Automation Support (Robot Framework, pytest, selenium)
    - IDE Integration (VS Code, PyCharm, JetBrains)
    - Code Completion Speed
    - Project-Wide Context Awareness
    - Debugging & Error Resolution
    - Documentation Generation
    - Cost/Value (Free tier + paid pricing)
    - Robot Framework Specific Support
    - Learning Curve (Ease of use)
  
- Final Rank:
    1. Claude
    2. GitHub Copilot
    3. Cursor
    4. ChatGPT
    5. Windsurf
    6. Qodo
    7. JetBrains AI
    8. Amazon Q
    9. Aider
    10. Tabnine <br>
- **Final Verdict**
  - **Claude** for test design, complex test generation, and documentation
  - **GitHub Copilot** for daily IDE coding with fast autocomplete
  - **ChatGPT** as backup for learning and quick questions

</details>

<details><summary>How to use GitHub Copilot in PyCharm </summary>

- Pre-requisites:
  - PyCharm IDE (Professional or Community), version 2021.2+
  - GitHub account with Copilot subscription
- Open PyCharm
  - Go to Settings/Preferences > Plugins > GitHub Copilot
  - Install and restart IDE
  - Tools → GitHub Copilot → Login to GitHub (Sign in to GitHub account)
    - A browser window will open asking you to authorize JetBrains + GitHub.
    - Once you approve, PyCharm will show : Connected as your‑GitHub‑username
- Testing it out
  - Open a Python file : `github_copilot_test.py`
  - Start typing code or comments describing what you want
  - GitHub Copilot will suggest code completions inline
  - Use Tab to accept suggestions, or Ctrl + ] / Ctrl + [ to cycle through alternatives
  </details>

<details><summary>How to use GitHub Copilot in VS Code</summary>

- Pre-requisites:
  - VS Code installed
  - GitHub account with Copilot subscription
- Open VS Code
  - Go to Extensions (Ctrl+Shift+X)
    - Search for "GitHub Copilot"
    - Click Install
    - After installation, you may need to reload VS Code
- Sign in to GitHub
  - A browser window opens
  - Authorize GitHub Copilot
  - Return to VS Code
  - signing in to GitHub
- Enabling Copilot, Look at the bottom-right status bar:
  - Click the Copilot icon
  - Select "Enable GitHub Copilot"
  - enabling Copilot features
- Testing it out
  - Open a Python file : `github_copilot_test.py`
  - Start typing code or comments describing what you want
  - GitHub Copilot will suggest code completions inline
  - Use Tab to accept suggestions, or Ctrl + ] / Ctrl + [ to cycle through alternatives
  
  </details>
<br>
 
# Llama / Ollama

**LLaMA (Large Language Model Application)**: A large language model developed by Meta AI that uses transformer architecture to process and understand human language, with applications in text generation, question answering, and more.

**Ollama** is a command-line interface (CLI) tool for interacting with local large language models (LLMs). It allows users to run, manage, and utilize LLMs on their own machines without relying on cloud services.

<details><summary>popular LLMs (Large Language Moodels)</summary>

- **LLaMA (Meta AI)**: A large language model that uses transformer architecture to process and understand human language.
- **T5 (Google)**: A large language model that uses the T5 model architecture, which is designed for text-to-text tasks like question answering and summarization.
- **BERT (Google)**: A pre-trained language model that uses a two-layer bidirectional transformer encoder to generate contextualized representations of words in text.
- **RoBERTa (Facebook AI)**: A variant of BERT that uses a different approach to training, which includes removing the next sentence prediction task and using a larger vocabulary.
- **DistilBERT (Google)**: A smaller and more efficient version of BERT that's designed for faster inference times and lower memory usage.
- **XLNet (Facebook AI)**: A large language model that uses a similar approach to BERT, but with a few key differences in terms of architecture and training data.
- **Longformer (Hugging Face)**: A large language model that uses a different approach to processing long-range dependencies in text, which includes using a separate attention mechanism for longer sequences.
- **EleutherA (Facebook AI)**: A large language model that's designed to be more fine-tunable than other models, with a focus on improving performance on specific tasks like question answering and sentiment analysis.
- **ParlAI (Stanford University)**: A large language model that's designed for conversational dialogue systems, which includes using a combination of transformer architecture and attention mechanisms.
- **Google's LaMDA**: A large language model that uses a combination of transformer architecture and machine learning to generate human-like responses to user input.
- **OpenAI's GPT-3**: A large language model that uses transformer architecture to generate human-like text, with applications in text generation, translation, and more.
- **Cohere's Command R**: A large language model optimized for retrieval-augmented generation tasks, combining language understanding with information retrieval.
- **Mistral 7B**: A large language model developed by Mistral AI, known for its efficiency and performance in various NLP tasks.
- **Falcon 40B**: A large language model developed by the Technology Innovation Institute, recognized for its high performance in natural language understanding and generation tasks.
</details>

<details><summary>LLaMA Vs OpenAI</summary>
LLaMA and OpenAI are both large language models developed by Meta AI and OpenAI, respectively. While they share some similarities, there are also some key differences.<br>
Overall, LLaMA can process longer texts and maintain context better than GPT-3. LLaMA is optimized for lower latency, making it more suitable for real-time applications, LLaMA is an open-source model
</details>

## How to use LLaMa


Topics:
<details><summary>The best practices</summary>

  * Choose the right model size for the job
  * Use high-quality prompts
  * Leverage system prompts
  * Use retrieval when accuracy matters
  * Fine-tune only when necessary
  * Use quantization wisely
  * Evalute outputs systematically
  * guardrails matter
  * Optimize for context lenght
  * Iterate
</details>

<details><summary>How to run LLaMa Locally</summary>

  1. **Confirm your System:** quick way is using AI and giving the details of your operation system, including storage, RAM, CPU, GPU and OS.
  2. Pick one and follow the instructions which AI provided
  3. For my case, I will do the **Ollama**
</details>

<details><summary>Here is the sample of mine</summary>

- CPU: AMD Ryzen 7 5700G → Strong multi‑core CPU, great for llama.cpp
- GPU: 16 GB VRAM → Excellent for 7B and 13B models, and usable for 30B (quantized)
- RAM: 32 GB → Plenty for running medium‑sized models
- Storage: 2.28 TB → More than enough for multiple models
- OS: Windows 11 Pro → Compatible with all major LLaMA runtimes
</details>

### Ollama Setup

1. [Install Ollama](https://ollama.com/download)
2. Check what LLaMA Models you can Run, for my case: <br>
7B  -> Easilly, Full speed on GPU <br>
13B -> very good, smooth with 4-bit or 8 bit <br>
30B -> with quantization, GPU may need offloading to CPU <br>
70B -> Not practical, Needs multi-GPU or server hardsare <br>
3. Run a model ```ollama run llama3```
4. Download(PUll) a specific size ```ollama pull llama3:8b``` or ```ollama pull llama3:3b```

<details><summary>Ollama Command Cheat Sheet</summary>

```
## Basic Info ###########################
ollama --version        # Show Ollama version
ollama ps               # Show running models / processes
ollama list             # List all installed models

## Download Models ######################
ollama pull llama3      # Download default LLaMA 3 model
ollama pull llama3:8b   # Download specific size
ollama pull llama3:13b

## Run Models ##########################
ollama run llama3                       # Start interactive chat
ollama run llama3 "Your prompt here"    # One-shot prompt
ollama run llama3 --verbose             # Show GPU/CPU usage
ollama run llama3 --system "You are a tutor." 

## Stop Models #########################
ollama stop all         # Stop all running models
ollama stop llama3      # Stop a specific model

## Manage Models ######################
ollama rm llama3        # Remove a model
ollama cp llama3 my-llama   # Copy/rename a model

## Create Custom Models ###############
## modelfile example
FROM llama3
SYSTEM "You are a helpful assistant."
## Build it
ollama create mymodel -f Modelfile
## Run it
ollama run mymodel

## API Usage ##########################
ollama serve             # Start API server (Linux/macOS only)
## Send a request
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Write a haiku about winter."
}'

## Windows Service Control ###########
net stop ollama          # Stop Ollama service
net start ollama         # Start Ollama service
taskkill /F /IM ollama.exe   # Force-kill all Ollama processes

## Port / Process Debugging ##########
netstat -ano | findstr 11434   # Check what uses Ollama port
taskkill /PID <PID> /F         # Kill specific process

```
</details>