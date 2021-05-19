# pytest_dragons

> :warning: This repository is under experimental phase and might not be useful for now.

PyTest Plugins to run DRAGONS tests. 

This plugin contains all the fixtures that we have been using in our DRAGONS Test Suite. At first, these fixtures lived in `conftest.py` files spread all over [DRAGONS](https://github.com/GeminiDRSoftware/DRAGONS) repository. Then, we collected all these fixtures and put them into a single PyTest plug-in that lived within  [DRAGONS](https://github.com/GeminiDRSoftware/DRAGONS), but using them would require installing DRAGONS. Now we are splitting up the `pytest_dragons` plugin, so you can install it without installing [DRAGONS](https://github.com/GeminiDRSoftware/DRAGONS), making it clearer where are the fixtures and allowing us to test the source code easily if wanted. 
