# Course Python: Guidelines, Tools and Packages

> This repo is a follow-along of the Udemy course *Python: Coding Guidelines, Tools, Tests and Packages* 
> The original course repository can be found [here](https://github.com/franneck94/UdemyPythonProEng/tree/master).

Create and activate environment, install requirements.

```python
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# OR
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Coding style

### VSCode settings

To create the settings.json, launch.json and tasks.json files, go to the Command Palette and click "Generate python config files"

### Imports

According to [PEP 8](https://peps.python.org/pep-0008/) recommendations, standard libraries should be imported in the first block of code, third party libraries in the second (other teams' libraries, like numpy and pandas), and local applications or libraries at the end (libraries I participated in development)

#### isort

[isort](https://pycqa.github.io/isort/) will autoamtically sort your imports.

On the command line type `isort .` to sort imports in the entire directory or `isort <filename>` to sort a single file.

The `.isort.config` file will help define how it will sort them.

### Code linters

A code linter is a dev tool that analyses source code for errors, vulnerabilities and stylistic issues to improve code quality.

[Ruff](https://docs.astral.sh/ruff/) is a very fast code linter that replaces traditional code linters like Flake8 and Pylint.

We can run `ruff check .` to look for errors on the entire current directory, and `ruff check --fix` to fix the issues detected. 

Not all errors can be fixed. We can configure how to fix some errors on the `pyproject.toml` file under the `[tool.ruff]` part.

Ruff can also replace isort, even though not all the functionalities.

### Formatters

Tools that make sure the code follows certain format guidelines.

- [Black](https://black.readthedocs.io/en/stable/)

Industry standard. Not much configurable style.

Run it with `python -m black <file or directory>`.

In the `pyproject.toml` file, we can add settings at the `[tool.black]` part.

- Ruff Formatter can also be used and it's much faster. It also has some improvements.

In the `settings.json` file, change the `editor.defaultFormatter` to `charliermarsh.ruff`, and add the wanted configurations to the `pyproject.toml` file in the `[tool.ruff.format]` section. And then run  `ruff format .`.

## Documentation: Type Annotations and Docstrings

> dunder: comes from double underscore and it reffers to special class methods that python automatically calls as a response to certain operations.

### Docstring

> See examples in the [Docstrings folder](\Docstrings).

Documentation string for functions, methods, classes or files. Always used below the documented element.

- [Google style](Docstrings\vector_google_style.py): Starts with a brief description, follows a list of arguments (Args), then possible outcomes of the element (Raises if it couls raise an error), Return if the function returns something.
- [Numpy style](Docstrings\vector_numpy_style.py): Starts with brief description; follows with Paramters and dashes (that render as a title), the list of parameters has their data types and if it's optional or not; then the outcome (Raises or Returns), dashes, and the data type of whatever is returned.

#### autoDoc

It's an automatic python docstring generator extension for VSCode. It will generate the docstring structure of choosing.

We can configure it from the `settings.json` file in the autoDocstring section.

When writing a function, add 3 quotation marks and it will give you the option to create the docstring.

### [Type Annotations](https://docs.python.org/3/library/typing.html)

> [typing cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

Adding data types to arguments and outputs of functions. They're not used during runtime, but are a useful tool to check for input data types before running code. The IDE will show an error if the arguments don't match the expected data types.

For simple functions, they can be useful by themselves, but they can also be combined with docstrings.

See some examples [here](TypeAnnotations\vector_type_annotations.py).

Special cases:

- If the arguments could take all types of data, we can use the `Any` type (`from typing import Any`).

- If the argument is optional we can use `Optional` (`from typing import Optional`). Like this: `param: Optional[int] = None`. Only acceptable for arguments that have default value = None. 
  - Can be replaced by `param: list[int] | None = None`.

- If the input of a function is another function, we should use `Callable` (`from collections.abc import Callable`). See example [here](TypeAnnotations\callable.py).
- For dictionaries we use `param: dict[str, int]`. The keys are strings and values are integers.
- Mappings:
  - Iterable containers (collections) that allows you to look up a key and retrieve its value. The generic form of a dictionary.
  - We use the Mapping obj from collections.abc (abstract base classes): `from collections.abc import Mapping`. And use it like `param: Mapping[str, int]`.
- `NoReturn` can be used if the function don't return anything.

### [pre-commit](https://pre-commit.com/)

Pre-commit hooks work for checking for errors in the code and making sure everything follows the same guidelines before commiting.

In the [.pre-commit-config.yaml file](.pre-commit-config.yaml) we list the tools and configurations we want to follow.

To install run `pre-commit install-hooks`, then to install the hooks (configs in the yaml file) run `pre-commit install-hooks`, then `pre-commit run` will run it on the uncommitted files. For all files we run `pre-commit run --all-files`

## Debugging

To choose configurations for the debugger in VSCode, we need to create a [`launch.json` file](.vscode\launch.json).

Whenever we want to debug, we mark the breakpoint line where the debugger will stop running the code.

Open the file you want to debug, and run the debugger in the configuration of current file. On the left panel, we'll see the variables created and the calls of the function and a list of breakpoints.

On top there are buttons with the possible actions.

