import os
import json
import requests

def detect_significant_structure_change(current: dict, incoming: dict) -> bool:
    return False

def install_agent(token: str, target_dir="agents/"):
    url = f"http://localhost:5050/download?token={token}"

    try:
        print("🔐 Contacting TreeSketch download server...")
        response = requests.get(url)
        if response.status_code == 200:
            os.makedirs(target_dir, exist_ok=True)
            filename = os.path.join(target_dir, "premium_agent.py")
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✅ Premium agent installed to {filename}")
        else:
            print(f"❌ Download failed with code {response.status_code}")
    except Exception as e:
        print(f"⚠️ Error during install: {e}")

import os

def apply_instruction_tree(tree: dict, memory, base_path=""):
    """
    Recursively apply the instruction-based structure from the agent.
    Each item must define:
      - type: 'file' or 'folder'
      - operation: 'create', 'modify', 'delete', or None
      - content (for files only)
    """
    for name, node in tree.items():
        if not isinstance(node, dict) or "type" not in node:
            continue  # skip malformed

        full_path = os.path.join(base_path, name)

        if node["type"] == "folder":
            op = node.get("operation")
            if op == "create":
                memory.update_structure(full_path + "/")
            elif op == "delete":
                memory.delete_path(full_path + "/")

            # Recurse into folder regardless
            for child_name, child_node in node.items():
                if child_name in ["type", "operation"]:
                    continue
                apply_instruction_tree({child_name: child_node}, memory, full_path)

        elif node["type"] == "file":
            op = node.get("operation")
            content = node.get("content", "")
            if op == "create":
                memory.update_structure(full_path, content)
            elif op == "modify":
                memory.update_file_contents(full_path, content)
            elif op == "delete":
                memory.delete_path(full_path)

    print("🤖 TreeSketch: Structure instructions applied.")
    memory.print_structure()


def apply_agent_output(structure_dict, memory, root: str = ""):
    """
    Accepts a JSON string representing a nested folder/file structure.
    Deserializes it and applies the structure to TreeMemory.
    """
    
    if isinstance(structure_dict, str):
        try:
            structure_dict = json.loads(structure_dict)
        except json.JSONDecodeError as e:
            print("❌ JSON parsing error:", e)
            return
    elif isinstance(structure_dict, dict):
        pass
    else:
        print("❌ Invalid agent response. Must be a dict or JSON string.")
        return

    # 🔍 Compare top-level keys with existing memory
    if detect_significant_structure_change(memory.structure, structure_dict):
        print("⚠️ Detected a major change in project structure.")
        response = input("🧠 This looks like a new project. Place in a new subdirectory in `output/`? (yes/no): ").strip().lower()
        if response in ["yes", "y"]:
            from datetime import datetime
            project_subdir = f"project-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
            memory.output_root = os.path.join(memory.output_root, project_subdir)
            os.makedirs(memory.output_root, exist_ok=True)
            print(f"📁 Structure will now be written to: {memory.output_root}")

    # ✅ Continue applying the structure
    def recurse(structure, base_path):
        for name, value in structure.items():
            full_path = os.path.join(base_path, name)
            if isinstance(value, dict):
                memory.update_structure(full_path + "/")
                recurse(value, full_path)
            elif isinstance(value, str):
                memory.update_structure(full_path, value)
            else:
                print(f"⚠️ Skipped invalid entry at: {full_path}")

    recurse(structure_dict, root)
    print("🤖 TreeSketch: Structure applied successfully.")
    memory.print_structure()
