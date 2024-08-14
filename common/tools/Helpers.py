import os


def get_project_root_path():
    # Get the path of the currently executing script
    script_path = os.path.abspath(__file__)

    # Navigate to the parent directory
    project_root = os.path.dirname(script_path)

    # Continue navigating to the parent directory until reaching the project root
    while not os.path.isfile(os.path.join(project_root, '.gitignore')):
        project_root = os.path.dirname(project_root)

    return project_root
