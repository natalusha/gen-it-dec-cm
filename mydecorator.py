import json


def to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapper


@to_json
def to_dict(my_list):
    e_list = dict(enumerate(my_list))
    return e_list
