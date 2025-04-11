import os

class TreeMemory:
    def __init__(self, output_root="output"):
        self.structure = {}
        self.log = []
        self.output_root = os.path.abspath(output_root)
        self.ready_to_build = False
        self.project_name = None
        self.mode = "default"
        self.last_prompt = ""

        # Ensure output directory exists
        os.makedirs(self.output_root, exist_ok=True)

    def update_structure(self, path: str, content=None):
        """
        Update the in-memory structure AND write to disk inside output/
        """
        parts = path.strip("/").split("/")
        cursor = self.structure
        for part in parts[:-1]:
            cursor = cursor.setdefault(part + "/", {})

        final = parts[-1]
        key = final + "/" if path.endswith("/") else final

        # Update in memory
        if path.endswith("/"):
            cursor.setdefault(key, {})
        else:
            cursor[key] = content or ""

        # Write to disk
        full_path = os.path.join(self.output_root, *parts)
        if path.endswith("/"):
            os.makedirs(full_path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content or "")

    def print_structure(self):
        def recurse(d, indent=0):
            for k, v in d.items():
                print("  " * indent + k)
                if isinstance(v, dict):
                    recurse(v, indent + 1)
        recurse(self.structure)

    def get_all_files_with_content(self, base_path=""):
        """
        Recursively collect all file paths and contents from the virtual structure.
        Returns a list of (path, content) tuples.
        """
        result = []

        def recurse(node, path):
            for name, value in node.items():
                new_path = os.path.join(path, name)
                if isinstance(value, dict):
                    recurse(value, new_path)
                elif isinstance(value, str):
                    result.append((new_path.replace("\\", "/"), value))

        recurse(self.structure, base_path)
        return result

    def update_file_contents(self, path: str, content: str):
        """
        Update the content of a file in memory and write it to disk.
        """
        parts = path.strip("/").split("/")
        cursor = self.structure

        for part in parts[:-1]:
            cursor = cursor.setdefault(part + "/", {})

        final = parts[-1]
        cursor[final] = content

        full_path = os.path.join(self.output_root, *parts)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content or "")
