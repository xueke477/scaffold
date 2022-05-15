## Introduction

This repo provides a CLI tool for quickly scaffolding a Python project in the 'src layout'.
That is, it is assumed that the Python project scaffolded this way is intended to be built
into a distribution package. The source code of a project scaffolded by this CLI tool is
contained in the `src` folder. Each subfolder of `src` is a separate 'import package'
within the distribution package.

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
```

- `adhoc` is for experimental code during development.

- `main` mimics the working folder of the _user_ of the distribution package.

- `tests` is for unit tests.

- `src` contains all import packages of the distribution package. Each import package
  should be a valid Python identifier. Change `example_package` to the appropriate name.

- `.flake8`, `mypy.ini`, `pytest.ini`, `requirements-dev.txt` are configuaratoin files
  with some sample settings.

- `pyproject.toml` is a PEP-518 compliant build system dependency file.

- `setup.cfg` contain the specifications of the build process. **Its contents need manual**
  **editing to suit the particular project being developed**.

- Run `pip install -e .` from the project root folder to install the package to the DEV virtual
  environment in 'editable mode'. This is essentially a hack that adds the folder `./src` to
  `sys.path` without explicitly manipulating `sys.path` in any package source code. Thus the
  package under development can be imported by its name from within any script in the `./adhoc`,
  `./main` and `./tests` folder, allowing convenient testing during development. More importantly,
  the package is imported by these scripts because it appears to them as a properly installed
  third-party package, not because it happens to lie in the same folder as the entry-point script.
  This is an important distinction because we want the import situation in the DEV environment
  to be as close as possible to that of the actual users of the package. Putting all package
  source code in a separate `src` subfolder is why this code organization strategy is called
  the 'src layout'.

- To build the final distribution package, first install the 'build front-end' by
  `pip install build`. Then run `python -m build`.

## Installation

This repo itself uses the same src layout that it scaffolds. It is built into a distribution
package encapsulated in the `dist/scaffold-1.0.1-py3-none-any.whl` wheel
file. After installing the distribution package in the _global environment_ of a Python
interpreter, the package places an executable `scaffold.exe` in the `Scripts` folder of the
global environment on Windows, or `scaffold` in the `bin` folder on \*nix. Afterwards, create
an alias to the executable and `scaffold` is available as a command from CLI.

### Install from wheel file

1.  Download `dist/scaffold-1.0.1-py3-none-any.whl`.

2.  Pip install from the wheel file into the global environment of a Python interpreter
    versioned 3.8 or above.

    On Windows, for example:

    ```
    py -3.8 -m pip install scaffold-1.0.1-py3-none-any.whl
    ```

    On macOS, for example:

    ```
    python3 -m pip install scaffold-1.0.1-py3-none-any.whl
    ```

3.  Create alias.

    With PowerShell, put the following in the start-up script.

    ```
    Set-Alias -Name scaffold -Value C:\Users\{your_name}\AppData\Local\Programs\Python\Python38\Scripts\scaffold.exe
    ```

    With zsh on macOS, put the following in `.zshrc`:

    ```
    alias scaffold='/Users/{your_name}/Library/Python/3.8/bin/scaffold'
    ```

### Build wheel from source

Alternatively, the wheel file can be built from source by the user.
After cloning the repo, delete the old wheel file and run the following
commands in a virtual environment specifically created for this repo:

```
pip install requirements-dev.txt
python -m build
```

The rest of the installation steps are the same.

### pip install from GitHub

Finally, the package can be installed directly from GitHub:

```
pip install git+https://github.com/xueke477/scaffold.git@master
```
