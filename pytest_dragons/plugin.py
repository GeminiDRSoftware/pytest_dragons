"""
Entry point for PyTest
======================

Changes how PyTest behaves by adding new command-line options, or
changing what it prints in our screen.
"""
import os
import pytest

from .fixtures import (astrofaker, base_temp, change_working_dir,
                       path_to_inputs, path_to_refs, path_to_outputs)


def pytest_addoption(parser):
    parser.addoption(
        "--dragons-remote-data",
        action="store_true",
        default=False,
        help="Enable tests that use the download_from_archive function."
    )
    parser.addoption(
        "--do-plots",
        action="store_true",
        default=False,
        help="Plot results of each test after running them."
    )
    parser.addoption(
        "--keep-data",
        action="store_true",
        default=False,
        help="Keep intermediate data (e.g. pre-stack data)."
    )
    parser.addoption(
        "--interactive",
        action="store_true",
        default=False,
        help="Run interactive tests."
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "dragons_remote_data: tests with this mark will download a large "
        "volume of data and run")
    config.addinivalue_line(
        "markers",
        "preprocessed_data: tests with this download and preprocess the "
        "data if it does not exist in the cache folder.")
    config.addinivalue_line(
        "markers",
        "interactive: for tests that run interactively and require a display to"
        "run.")


def pytest_collection_modifyitems(config, items):
    """
    Add custom command line options to the PyTest call for DRAGONS.

    Examples
    ========
    ```
    $ pytest --interactive geminidr/gmos/tests/spect/test_trace_apertures.py
    ```
    """
    if not config.getoption("--dragons-remote-data"):
        marker = pytest.mark.skip(reason="need --dragons-remote-data to run")
        for item in items:
            if "dragons_remote_data" in item.keywords:
                item.add_marker(marker)

    if not config.getoption("--interactive"):
        marker = pytest.mark.skip(reason="need --interactive to run")
        for item in items:
            if "interactive" in item.keywords:
                item.add_marker(marker)

    if "GITHUB_WORKFLOW" in os.environ:
        marker = pytest.mark.skip(
            reason="GitHub Actions do not support tests with preprocessed data")
        for item in items:
            if "preprocessed_data" in item.keywords:
                item.add_marker(marker)


def pytest_report_header(config):
    return f"DRAGONS_TEST directory: {os.getenv('DRAGONS_TEST')}"
