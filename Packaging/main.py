from my_package import print_hello_world
from my_package.printing import print_hello_world_subpackage
from my_package.version import __version__


def main() -> None:
    print(f"Version {__version__}")
    print_hello_world()
    print_hello_world_subpackage()


if __name__ == "__main__":
    main()
