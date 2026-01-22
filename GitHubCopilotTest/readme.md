# GitHub Copilot
Under this folder, you can find resources and information related to GitHub Copilot.

## GitHub Copilot Vs Copilot
Both owned by Microsoft, GitHub Copilot is an "AI Pair Programmer", helps to write logic, scripts, and documentation. 
Microsoft Copilot is an "AI Office Assistant", helps to write emails, summarize meetings, and analyze data in Office apps.

### Comparison
| Feature   | GitHub Copilot                            | Microsoft Copilot                        |
|-----------|-------------------------------------------|------------------------------------------|
| Purpose   | Writing and debugging code                | Business productivity and reseach        |
| Best Task | Write a Python script to parse there logs | Summarize the key points of this meeting |
| Price     | ~$10/mo (Free for students)               | Free (Basic), ~$20/mo (Pro/Office)       |

### For Automation Engineers
If you are sitting in front of a code editor trying to make a machine move or a script run, 
GitHub Copilot is your tool. If you are sitting in a meeting or writing a report about that 
machine, Microsoft Copilot is the one to use.

- practical examples: **in progress**
  1. Generating PLC Logic (Structured Text)
  2. Auto-Generating Test Scripts (Python/Playwright)
  3. Converting Legacy Code (e.g., VBA to Python)

  ### PLC (Programmable Logic Controller)
  - In automation testing, PLC usually means validating the PLC program (ladder logic, function blocks, stc.)
  - benefit are give reliable, flexible, and cost‑effective control of machines and processes, especially compared with hard‑wired relays or ad‑hoc microcontroller setups.
  - open an .st file and start writing comments, Copilot will suggest the code for you.
  ### Auto-Generating Test Scripts
  - as a coding assistant, not a fully autonomous test tool. Likes:
    - can suggest unit and integration test code (for example, JUnit, pyTest, Jest, Pester, Selenium, Playwright) by looking at your existing functions, classes, and comments, which speeds up writing repetitive test cases.
    - Still **need human oversight** to ensure the generated tests are accurate, relevant, and comprehensive.
    - go to /GitHubCopilot/ explore how github copilot can help generate test scripts
      - ```python_unit_test.py```
      - ```math_utils.py```
      - ```test_math_utils.py```