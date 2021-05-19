# pytest_dragons

> :warning: This repository is under experimental phase and might not be useful for now.

This plugin contains the fixtures for the DRAGONS Test Suite. At first, these 
fixtures lived in `conftest.py` files spread all over [DRAGONS] repository. 
Then, we collected all these fixtures and put them into a single PyTest plug-in 
that lived within [DRAGONS], but using them would require installing [DRAGONS]. 
Now we are splitting up the `pytest_dragons` plugin, so you can install it 
without installing [DRAGONS], making it clearer where are the fixtures and 
allowing us to test the source code easily if wanted. 

----
This [pytest] plugin was generated with [Cookiecutter] along with 
[@hackebrot]'s [cookiecutter-pytest-plugin] template.


## Features
* TODO


## Requirements
* TODO


## Installation
You can install "pytest-dragons" via [pip] from [PyPI]::

    $ pip install pytest_dragons


## Usage
* TODO

## Contributing
Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License
Distributed under the terms of the [BSD] license, "pytest_dragons" is free and 
open source software.


## Issues
If you encounter any problems, please [file an issue] along with a detailed 
description.

[BSD]: http://opensource.org/licenses/BSD-3-Clause
[cookiecutter-pytest-plugin]: https://github.com/pytest-dev/cookiecutter-pytest-plugin
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[DRAGONS]: https://github.com/GeminiDRSoftware/DRAGONS 
[file an issue]: https://github.com/b1quint/pytest-dragons/issues
[pip]: https://pypi.org/project/pip/
[pytest]: https://github.com/pytest-dev/pytest
[PyPI]: https://pypi.org/project
[tox]: https://tox.readthedocs.io/en/latest/
[@hackebrot]: https://github.com/hackebrot