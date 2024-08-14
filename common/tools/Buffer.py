from common.tools.Logger import log_info

dict_of_variables = {}


def set_value(var_name, var_value):
    dict_of_variables[var_name] = var_value
    if "TOKEN" not in var_name:
        log_info("Buffer.set_value [Key: " + var_name + ", Value: " + dict_of_variables[var_name] + "]")


def get_value(var_name):
    if "TOKEN" not in var_name:
        log_info("Buffer.get_value [Key: " + var_name + ", Value: " + dict_of_variables[var_name] + "]")
    return dict_of_variables[var_name]


def clear_dict():
    dict_of_variables.clear()
