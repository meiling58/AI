# AI 
In progress...\

Artificial intelligence (AI) is a field of computer science focused on building systems that can perform tasks 
normally require human intelligence, such as recognizing patterns, understanding language, making decisions, 
and solving problems. In simple terms, it means computers and machines using data and algorithms to learn 
from experience and then act or make recommendations on their own within specific tasks. ([wiki](https://en.wikipedia.org/wiki/Artificial_intelligence))


## Popular AIs
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

### Comparison
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

### AI - For Python/Robot Framework developers
Ask Claude with "using borda ranking system search all popular AIs with criteria, the best for developers who are using python/robot" <br>

Result:<br>
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
    10. Tabnine

- **Final Verdict**
  - **Claude** for test design, complex test generation, and documentation
  - **GitHub Copilot** for daily IDE coding with fast autocomplete
  - **ChatGPT** as backup for learning and quick questions

#### How to use GitHub Copilot in PyCharm
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

#### How to use GitHub Copilot in VS Code
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