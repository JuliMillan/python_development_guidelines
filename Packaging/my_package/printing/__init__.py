# from ._printing import print_from_private


def print_hello_world_subpackage() -> None:
    print(__name__)
    print("Hello World from the subpackage")
