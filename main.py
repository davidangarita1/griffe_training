import griffe

loader = griffe.GriffeLoader()
package_name = "htmy"
my_package = loader.load(package_name)


def colorizer(text):
    return f"\033[33m{text}\033[0m"


def show_package_name():
    print(f"{colorizer('Package name:')}\n{my_package.name}\n")


def docstring_class(class_name: str):
    my_class = my_package[class_name]
    print(
        f"{colorizer(f'Class docstring from {class_name}:')}\n{my_class.docstring.value}\n"
    )


def docstring_method(method: str):
    my_method = my_package[method]
    print(
        f"{colorizer(f'Method docstring from {method}:')}\n{my_method.docstring.value}\n"
    )


def method_class(method: str):
    my_method = my_package[method]
    print(f"{colorizer(f'Method from {method}:')}\n{my_method}\n")


def package_members():
    print(
        f"{colorizer(f'Members from {package_name}:')}\n{list(my_package.members.keys())}\n"
    )


def package_to_json():
    json_str = my_package.as_json()
    max_chars = 150
    print(f"{colorizer(f'Package {package_name} to JSON:')}\n{json_str[:max_chars]}\n")


def main():
    class_name = "BaseTag"
    show_package_name()
    package_members()
    method_class(f"{class_name}.htmy")
    docstring_class(class_name)
    docstring_method(f"{class_name}.htmy")
    package_to_json()


if __name__ == "__main__":
    main()
