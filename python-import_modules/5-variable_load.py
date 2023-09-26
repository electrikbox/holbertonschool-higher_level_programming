#!/usr/bin/python3
if __name__ == "__main__":
    import variable_load_5

    module_attributes = dir(variable_load_5)

    for attribute_name in module_attributes:
        if not attribute_name.startswith("__"):
            attribute_value = getattr(variable_load_5, attribute_name)
            if callable(attribute_value):
                continue
            print(attribute_value)
