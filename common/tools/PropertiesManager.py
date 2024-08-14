from jproperties import Properties

from common.tools.Helpers import get_project_root_path


def get_property_value(property_file, property_name):
    config = Properties()
    path = ""
    if "test_config" in property_file:
        path = get_project_root_path() + '/tests/test_configs/' + property_file
    elif "dataset" in property_file:
        path = get_project_root_path() + '/tests/test_configs/datasets/' + property_file
    elif "env1" in property_file:
        path = get_project_root_path() + '/tests/test_configs/envs/' + property_file
    with open(path, 'rb') as config_file:
        config.load(config_file)

    return config.get(property_name)[0]

