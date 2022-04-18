## Introduction

This repo provides a CLI tool for quickly scaffolding a Python project in the 'src layout'.
That is, it is assumed that the Python project scaffolded this way is intended to be built
into a distribution package. The package code is contained in the `src` folder.
Each subfolder of `src` is a separate 'import package' within the distribution package.

After scaffolding, the project folder has the following structure.

```
./
|----adhoc/
|----main/
|----tests/
|----src/
|     |----example_package
|           |----__init__.py
|           |----py.typed
|----.gitignore
|----LICENSE
|----README.md
|----.flake8
|----mypy.ini
|----pytest.ini
|----requirements-dev.txt
|----pyproject.toml
|----setup.cfg
|----setup.py
```

- `adhoc` is for experimental code during development.

- `main` mimics the working folder of the _user_ of the distribution package.

- `tests` is for unit tests.

- `src` contains all import packages of the distribution package. Each import package
  should be a valid Python identifier. Change `example_package` to the appropriate name.

- `.flake8`, `mypy.ini`, `pytest.ini`, `requirements-dev.txt` are configuaratoin files
  with some sample settings.

- `pyproject.toml` is a PEP-518 compliant build system dependency file.

- `setup.cfg` and `setup.py` contain the specifications of the build process. Either could
  be used to build the distribution package. `setup.py` is needed to install the package
  in 'editable mode' during development. **The contents of these two files need manual**
  **editing to suit the particular project being developed**.

- For editable install, run `pip install -e .`. Note that the final dot in the command is
  necessary.

- To build the final distribution package, first install the 'build front-end' by
  `pip install build`. Then run `python -m build`.

## Installation

This repo itself uses the same src layout that it scaffolds. It is built into a distribution
package named encapsulated in the `dist/scaffold-1.0.0-py3-none-any.whl` wheel
file. After installing the distribution package in the _global environment_ of a Python
interpreter, the package places an executable `scaffold.exe` in the `Scripts` folder of the
global environment on Windows, or `scaffold` in the `bin` folder on \*nix. Afterwards, create
an alias to the executable and `scaffold` is available as a command from CLI.

### Install from wheel file

  1.  Download `dist/scaffold-1.0.0-py3-none-any.whl`.

  2.  Pip install from the wheel file into the global environment of a Python interpreter
      versioned 3.8 or above.

        On Windows, for example:

        ```
        py -3.8 -m pip install scaffold-1.0.0-py3-none-any.whl
        ```

        On macOS, for example:

        ```
        python3 -m pip install scaffold-1.0.0-py3-none-any.whl
        ```

  3. Create alias.

        With PowerShell, put the following in the start-up script.

        ```
        Set-Alias -Name scaffold -Value C:\Users\your_name\AppData\Local\Programs\Python\Python38\Scripts\scaffold.exe
        ```

        With zsh on macOS, put the following in `.zshrc`:

        ```
        alias scaffold='/Users/your_name/Library/Python/3.8/bin/scaffold'
        ```

### Build wheel from source

  Alternatively, the wheel file can be built from source by the user.
  After cloning the repo, run the following commands _in a virtual environment_:

  ```
  pip install requirements-dev.txt
  python -m build
  ```

  The rest of the installation steps are the same.
