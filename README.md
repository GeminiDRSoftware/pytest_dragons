# pytest_dragons

[![Run unit tests](https://github.com/GeminiDRSoftware/pytest_dragons/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/GeminiDRSoftware/pytest_dragons/actions/workflows/unit-tests.yml)

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

All the fixtures and helper functions now live within [pytest_dragons]. Helper functions 
are standard Python functions. Fixtures are special PyTest functions that need to be 
used as arguments for test functions.  Most of the fixtures are using by our team 
tests that run inside NOIRLab/GEMINI private network.  Getting access to external 
contributors is unlikely to happen due to cybersecurity policies and data ownership. 

However, you do need to install this plug-in if running any tests for [DRAGONS].


## Requirements
* Python >= 3.7
* PyTest 


## Installation

The easiest way to install `pytest_dragons` is via [pip]::

    $ pip install -e git+https://github.com/GeminiDRSoftware/pytest_dragons.git@v1.0.0#egg=pytest_dragons

Please, note that this is installing the `pytest_dragons` [v0.1.0]. 
Refer to the [Releases] pages for all the released versions available.

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

[v0.1.0]: https://github.com/GeminiDRSoftware/pytest_dragons/releases/tag/v0.1.0

[BSD]: http://opensource.org/licenses/BSD-3-Clause
[cookiecutter-pytest-plugin]: https://github.com/pytest-dev/cookiecutter-pytest-plugin
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[DRAGONS]: https://github.com/GeminiDRSoftware/DRAGONS 
[file an issue]: https://github.com/b1quint/pytest-dragons/issues
[pip]: https://pypi.org/project/pip/
[pytest]: https://github.com/pytest-dev/pytest
[pytest_dragons]: https://github.com/GeminiDRSoftware/pytest_dragons/blob/main/pytest_dragons.py
[PyPI]: https://pypi.org/project
[Releases]: https://github.com/GeminiDRSoftware/pytest_dragons/releases
[tox]: https://tox.readthedocs.io/en/latest/
[@hackebrot]: https://github.com/hackebrot
