"""
Simple Conversational AI Agent with Ollama using cli interface.
Run: python simple_agent_v1.py
Will showing the 

============================================================
Simple AI Agent - Powered by Ollama
============================================================
Type 'quit' or 'exit' to end the conversation
Type 'reset' to clear conversation history
============================================================
🧑 You: 

Now you can chat with the agent! with sample below:

Test sample:
You: Hello, who are you?
Agent: I am an AI agent powered by Ollama. How can I assist you today?
You: Yes. I would love to know what can you help to plan a trip from Taipei to Boston for 10 days.
"""

import ollama


class SimpleAgent:
    def __init__(self, model="llama3.2:3b"):
        self.model = model
        self.conversation_history = []

    def chat(self, user_message):
        """Send a message and get a response"""
        # Add user message to history
        self.conversation_history.append({
            'role': 'user',
            'content': user_message
        })

        # Get response from Ollama
        response = ollama.chat(
            model=self.model,
            messages=self.conversation_history
        )

        # Add assistant response to history
        assistant_message = response['message']['content']
        self.conversation_history.append({
            'role': 'assistant',
            'content': assistant_message
        })

        return assistant_message

    def reset(self):
        """Clear conversation history"""
        self.conversation_history = []


def main():
    # Initialize agent
    agent = SimpleAgent()

    print("=" * 60)
    print("Simple AI Agent - Powered by Ollama")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the conversation")
    print("Type 'reset' to clear conversation history")
    print("=" * 60)

    while True:
        # Get user input
        user_input = input("\n🧑 You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ['quit', 'exit']:
            print("\n👋 Goodbye!")
            break

        if user_input.lower() == 'reset':
            agent.reset()
            print("\n🔄 Conversation history cleared!")
            continue

        # Get and print response
        try:
            response = agent.chat(user_input)
            print(f"\n🤖 Agent: {response}")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Make sure Ollama is running and the model is downloaded.")
            print("Try: ollama pull llama3.2")


if __name__ == "__main__":
    main()
