# interpolation.py

import re

def property(data):
    def nested(path):
        parts = path.split(".")
        result = data
        for part in parts:
            if not part in result:
                return None
            result = result[part]
        return result
    return nested

def interpolate(source, data):
    get_property = property(data)

    def replace_with(matchdata):
        content = matchdata.group(0)
        name = matchdata.group(1)
        result = get_property(name)
        if result == None:
            result = content
        return result

    return re.sub(
        r'\${([.a-z]+)}',
        replace_with,
        source
    )
