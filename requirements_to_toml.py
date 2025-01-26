import re

def requirements_to_toml(requirements_file, toml_file):
    with open(requirements_file, 'r') as req_file:
        dependencies = req_file.readlines()
    
    toml_dependencies = ["[tool.poetry.dependencies]", 'python = "^3.9"']  # Adjust Python version as needed
    
    for dep in dependencies:
        dep = dep.strip()
        if not dep or dep.startswith("#"):
            continue  # Skip empty lines and comments
        match = re.match(r"([\w\-]+)([<>=!~]+.+)?", dep)
        if match:
            name, version = match.groups()
            version = version.strip() if version else "*"
            toml_dependencies.append(f'{name} = "{version}"')
    
    with open(toml_file, 'w') as toml_out:
        toml_out.write("\n".join(toml_dependencies))
    
    print(f"Converted {requirements_file} to {toml_file}")

# Example usage
requirements_to_toml("requirements.txt", "pyproject_requirements.toml")