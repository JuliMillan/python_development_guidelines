# Course Python: Guidelines, Tools and Packages

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

Ruff is a very fast code linter that replaces traditional code linters like Flake8 and Pylint.

We can run `ruff check .` to run ruff on the entire current directory, and `ruff fix` to fix the issues detected. Not all errors can be fixed.