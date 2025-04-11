from agent.memory import TreeMemory
from agent.deepseek_agent import call_deepseek_agent
from interpreter.agent_ops import apply_agent_output

import os

def build_dynamic_preprompt(memory: TreeMemory) -> str:
    base = """You are TreeSketch's structure planner.

Return a single nested JSON dictionary that defines the folder and file structure.

- Folder values are nested dictionaries
- File values are string contents
- All folder names and file paths must reflect their hierarchy

Example:
{
  "project": {
    "src": {
      "index.js": "// JS entry",
      "components": {}
    },
    "README.md": "# My Project"
  }
}

Do NOT include markdown or triple backticks.
Respond ONLY with valid JSON.

"""

    file_list = memory.get_all_files_with_content()
    if not file_list:
        return base + "\n# No files exist yet.\n"

    base += "\n# Current files and contents:\n"
    for path, content in file_list:
        base += f"\n- {path}:\n{content}\n"

    return base

def main():
  memory = TreeMemory()
  print("🌳 TreeSketch — Describe your file system (type 'exit' to quit)\n")

  while True:
      preprompt = build_dynamic_preprompt(memory)

      user_input = input("🗣️  You: ")
      if user_input.strip().lower() == "exit":
          print("👋 Exiting TreeSketch.")
          break

      try:
          agent_response = call_deepseek_agent(preprompt, user_input)
          apply_agent_output(agent_response, memory)
      except Exception as e:
          print("❌ Error:", e)

      print("🗣️  You:")

if __name__ == "__main__":
    main()
