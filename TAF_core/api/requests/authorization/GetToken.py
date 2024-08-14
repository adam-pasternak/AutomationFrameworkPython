from common.tools.Buffer import set_value

username = "ABC"
password = "DEF"


def get_token():
    set_value("TOKEN", username + password)
