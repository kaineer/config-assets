# Intention:
#   create a way to replace values inside yaml object
#
# After loading replacement from different yaml
# and loading main yaml file
# run object_enum with handle function that will
# replace all values that should be interpolated

__all__ = ['object_enum', 'replace']

class Replace:
    def __init__(self, value):
        self.value = value

def replace(value):
    return Replace(value)

def build_key(parent_key, current_key):
    if parent_key == None:
        return str(current_key)
    return parent_key + '.' + str(current_key)

def object_enum(data, fn, parent_key = None):
    if type(data) == dict:
        changed = {}
        for key in data:
            current_key = build_key(parent_key, key)
            value = data[key]
            changed[key] = object_enum(value, fn, current_key)
        return changed
    elif type(data) == list:
        changed = []
        for (key, value) in enumerate(data):
            current_key = build_key(parent_key, key)
            result = object_enum(value, fn, current_key)
            changed.append(result)
        return changed
    else:
        changed = data
        result = fn(parent_key, data)
        if type(result) == Replace:
            changed = result.value
        return changed
