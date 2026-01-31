# Local AI Agent
- Language: Python
- LLM: ollama
- Agent framework: supporting various agent types and functionalities.
  - TBD

<details><summary>Repo/Project Structure</summary>

    localAIAgent/  # Project Root
    ├── agents/  # Different agent implementations
    ├── tools/  # Tools that agents can use
    ├── utils/  # Utility functions and helpers
    ├── config/  # Configuration files
    ├── tests/  # Unit and integration tests
    ├── requirements.txt  # Project dependencies
    └── main.py  # Entry point for running the application
</details>

<details><summary>Pre-required</summary>

  1. python 10+
  2. ollama installed and set up with a local LLM model.
  3. Required Python packages installed.
  4. Install required Python packages:
      ```bash
      pip install -r requirements.txt
      ```
</details>

<details><summary>Setup</summary>

  1. git installed to clone the repository.
  2. Run the code on your favorite IDE or text editor.
  3. Run the main.py to start the agent application:
     ```bash
     python main.py
     ```
</details>

## OLLAMA Local LLM
Ollama is a tool that allows you to run large language models (LLMs) locally on your machine.

<details><summary>Ollama Features</summary>

    - Local Execution: Run LLMs on your local machine without needing cloud access.
    - Privacy: Keep your data private by processing it locally.
    - Performance: Benefit from low-latency responses since everything runs on your device.
    - Model Variety: Access a range of pre-trained models or use your own custom models.
    - Easy Integration: Simple API for integrating with applications and workflows. 
</details>

<details><summary>Ollama Installation</summary>

  1. Visit the [Ollama website](https://ollama.com/) to download the installer for your operating system.
  2. Follow the installation instructions provided on the website.
  3. After installation, verify that Ollama is set up correctly by running:
     ```bash
     ollama --help
     ollama --version
     ollama list
     ollama popd # to see available models
     ollama pull <model-name> # to download a specific model likes: llama3.2:1b, llama3.2:3b
     ollama run <model-name> # to run a specific model, such as llama3.2:1b, llama3.2:3b     
     ```
  4. For more detailed instructions, refer to the [Ollama Documentation](https://ollama.com/docs).
</details>

<details><summary>Python Packages</summary>

- <details><summary>ollama: Python client for interacting with Ollama LLMs.</summary>
  - Install via pip:
    ```bash
    pip install ollama
    ```
  - Usage example:
    ```python
    from ollama import Ollama

    ollama = Ollama()
    response = ollama.chat(model="llama3.2:1b", messages=[{"role": "user", "content": "Hello, Ollama!"}])
    print(response)
  - Documentation: [Ollama Python Client](https://pypi.org/project/ollama/
  </details>

</details>
