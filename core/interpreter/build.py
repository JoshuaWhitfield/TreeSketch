import os

def build_structure(structure, root="output"):
    for name, content in structure.items():
        path = os.path.join(root, name)

        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            build_structure(content, root=path)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
