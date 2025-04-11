from agent.memory import TreeMemory
from agent.deepseek_agent import call_deepseek_agent
from interpreter.agent_ops import apply_instruction_tree

import os


def build_instruction_style_preprompt(memory: TreeMemory) -> str:
    base = """You are TreeSketch's structure planner.
        
        Before reading the new prompt which will be denoted below after the file contents, 
        always read through and save the file contents to memory before 
        making updates to files.
        
        Return a single nested JSON object representing file and folder instructions.
        
        Each key is a file or folder name.
        Each value must be a dictionary with at least:
        - "type": "file" or "folder"
        - "operation": "create", "modify", "delete", or null
        - "content": string (required only for file create/modify)

        Example:
        {
        "src": {
            "type": "folder",
            "operation": "create",
            "main.py": {
            "type": "file",
            "operation": "create",
            "content": "# code here"
            }
        },
        "backend": {
            "type": "folder",
            "operation": null,
            "server.py": {
            "type": "file",
            "operation": "modify",
            "content": "# updated server code"
            }
        }
        }

        Respond ONLY with valid JSON. Do not include markdown or extra explanation.
        -----------------------------------------------
        file contents:


        """

    # Append current file snapshot to preprompt
    files = memory.get_all_files_with_content()
    if files:
        base += "\n# Current project file contents:\n"
        for path, content in files:
            base += f"\n- {path}:\n{content}\n"

    return base

def main():
    memory = TreeMemory()
    print("🌳 TreeSketch — Describe your file system (type 'exit' to quit)\n")

    while True:
        preprompt = build_instruction_style_preprompt(memory)

        user_input = input("🗣️  You: ")
        if user_input.strip().lower() == "exit":
            break

        agent_response = call_deepseek_agent(preprompt, user_input)
        apply_instruction_tree(agent_response, memory)

if __name__ == "__main__":
    main()
