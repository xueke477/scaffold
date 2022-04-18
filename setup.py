import setuptools  # type: ignore


with open('README.md', 'r', encoding='utf-8') as fr:
    long_description = fr.read()

setuptools.setup(
    name='scaffold',
    version='1.0.0',
    author='Ke Xue',
    author_email='xueke.kent@gmail.com',
    description='Scaffold a project with src layout.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.8',
    zip_safe=False,
    package_data={
        'scaffold': ['data/*', 'py.typed']
    },
    entry_points={
        'console_scripts': ['scaffold=scaffold.command_line:main']
    }
)