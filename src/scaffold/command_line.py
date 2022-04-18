# Built-in
import argparse
from pathlib import Path
from shutil import copyfile
from typing import Optional


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold a project with src layout."
    )
    parser.add_argument(
        '-r', '--root', type=Path, default=[Path.cwd()], action='append',
        help='project root folder path.'
    )
    args = parser.parse_args()

    if len(args.root) == 1:
        root_dir: Path = args.root[0]
    elif len(args.root) == 2:
        if args.root[1].is_absolute():
            root_dir = args.root[1]
        else:
            root_dir = args.root[0].joinpath(args.root[1])
    else:
        print('Only accepting 0 or 1 --root parameter.')
        return

    file_dir = Path(__file__).parent
    data_dir = file_dir.joinpath('data')

    def copy_config_file(target_name: str, source_name: str) -> None:
        target_path = root_dir.joinpath(target_name)
        source_path = data_dir.joinpath(source_name)
        if not target_path.exists():
            copyfile(source_path, target_path)

    def touch_file(
        target_name: str, target_dir: Optional[Path] = None
    ) -> None:
        if isinstance(target_dir, Path):
            target_path = target_dir.joinpath(target_name)
        else:
            target_path = root_dir.joinpath(target_name)
        if not target_path.exists():
            with open(target_path, 'w') as _:
                pass

    vscode_dir = root_dir.joinpath('.vscode')
    vscode_dir.mkdir(exist_ok=True)
    copy_config_file('.vscode/settings.json', 'vscode_settings.txt')

    copy_config_file('.flake8', 'flake8.txt')
    copy_config_file('.gitignore', 'gitignore.txt')
    copy_config_file('mypy.ini', 'mypy.txt')
    copy_config_file('pytest.ini', 'pytest.txt')
    copy_config_file('pyproject.toml', 'pyproject.txt')
    copy_config_file('setup.cfg', 'setup_cfg.txt')
    copy_config_file('setup.py', 'setup_py.txt')
    copy_config_file('requirements-dev.txt', 'requirements-dev.txt')
    touch_file('README.md')
    touch_file('LICENSE')

    root_dir.joinpath('main').mkdir(exist_ok=True)
    root_dir.joinpath('adhoc').mkdir(exist_ok=True)
    root_dir.joinpath('tests').mkdir(exist_ok=True)

    src_dir = root_dir.joinpath('src')
    src_dir.mkdir(exist_ok=True)
    pack_dir = src_dir.joinpath('example_package')
    pack_dir.mkdir(exist_ok=True)
    touch_file('__init__.py', pack_dir)
    touch_file('py.typed', pack_dir)
