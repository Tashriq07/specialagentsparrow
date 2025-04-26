import os
import subprocess
import pyautogui
import openai

# OpenAI API Key for natural language processing (replace with your key)
openai.api_key = "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"

def chat_with_agent():
    """Chat interface for prompting tasks to the agent."""
    print("Welcome to the AI Agent!")
    print("Type 'exit' to quit the chat.\n")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Process input using OpenAI GPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"The user asked: {user_input}. Based on this, generate a Python script or clear instructions to automate the task:",
            max_tokens=150
        )
        
        # Get the response text
        task_prompt = response.choices[0].text.strip()
        print(f"AI Agent: {task_prompt}")
        
        # Confirm task execution
        confirm = input("\nDo you want the agent to execute this task? (yes/no): ").lower()
        if confirm in ["yes", "y"]:
            execute_task(task_prompt)
        else:
            print("Task execution canceled.\n")

def execute_task(task_prompt):
    """Execute tasks based on the agent's response."""
    try:
        # Use exec() to run the generated script (this is risky; confirm tasks first)
        exec(task_prompt)
    except Exception as e:
        print(f"Error executing task: {e}")

def main():
    """Main function to start the AI Agent."""
    print("AI Agent is starting...")
    
    # Start the chat interface
    chat_with_agent()

if __name__ == "__main__":
    main()