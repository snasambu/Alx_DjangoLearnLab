import os

project_root = os.path.dirname(os.path.abspath(__file__))

print("🔍 Scanning project for 'User' references...\n")

for root, dirs, files in os.walk(project_root):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                if "User" in content and "AUTH_USER_MODEL" not in content:
                    print(f"⚠️ Found possible 'User' reference in: {filepath}")
