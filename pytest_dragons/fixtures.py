"""
Fixtures
========

These are fixtures used in DRAGONS' tests. Remember that fixtures are normally
used as arguments for test functions and cannot be called directly. In a few cases,
our fixtures might return a function, which we can call, or a context manager, which
we use with the `with` statement.
"""
import os
import pytest

from contextlib import contextmanager
from .helper import get_active_git_branch


@pytest.fixture(scope="session")
def astrofaker():
    """
    Wrapper fixture that prevents undesired behaviour when using astrofaker.
    """
    return pytest.importorskip("astrofaker")


@pytest.fixture(scope="session")
def base_temp(tmp_path_factory):
    """
    Created a place to store the tests outputs. Can be set using the command
    line --basetemp (WARNING: WILL DELETE ALL OF ITS CURRENT CONTENT)

    Parameters
    ----------
    tmp_path_factory : fixture
        PyTest's build-in fixture.

    Returns
    -------
    str : Path for the tests results for the current session
    """
    return tmp_path_factory.mktemp("dragons-tests-")


@pytest.fixture(scope='module')
def change_working_dir(path_to_outputs):
    """
    Factory that returns the output path as a context manager object, allowing
    easy access to the path to where the processed data should be stored.

    Parameters
    ----------
    path_to_outputs : pytest.fixture
        Fixture containing the root path to the output files.

    Returns
    -------
    contextmanager
        Enable easy change to temporary folder when reducing data.
    """
    path = os.path.join(path_to_outputs, "outputs")
    os.makedirs(path, exist_ok=True)
    print(f"Using working dir:\n  {path}")

    @contextmanager
    def _change_working_dir(sub_path=""):
        """
        Changed the current working directory temporarily easily using the
        `with` statement.

        Parameters
        ----------
        sub_path : str
            Sub-path inside the directory where we are working.
        """
        oldpwd = os.getcwd()
        os.chdir(path)

        if sub_path:
            os.makedirs(sub_path, exist_ok=True)
            os.chdir(sub_path)

        try:
            yield
        finally:
            os.chdir(oldpwd)

    return _change_working_dir


@pytest.fixture(scope='module')
def path_to_inputs(request, env_var='DRAGONS_TEST'):
    """
    PyTest fixture that returns the path to where the input files for a given
    test module live.

    Parameters
    ----------
    request : fixture
        PyTest's built-in fixture with information about the test itself.

    env_var : str
        Environment variable that contains the root path to the input data.

    Returns
    -------
    str:
        Path to the input files.
    """
    path_to_test_data = os.getenv(env_var)

    if path_to_test_data is None:
        pytest.skip('Environment variable not set: $DRAGONS_TEST')

    path_to_test_data = os.path.expanduser(path_to_test_data).strip()

    module_path = request.module.__name__.split('.') + ["inputs"]
    module_path = [item for item in module_path if item not in "tests"]
    path = os.path.join(path_to_test_data, *module_path)

    if not os.path.exists(path):
        raise FileNotFoundError(
            " Could not find path to input data:\n    {:s}".format(path))

    if not os.access(path, os.R_OK):
        pytest.fail('\n  Path to input test data exists but is not accessible: '
                    '\n    {:s}'.format(path))

    branch_name = get_active_git_branch()

    if branch_name:
        branch_name = branch_name.replace("/", "_")
        path_with_branch = path.replace("/inputs", f"/inputs_{branch_name}")
        path = path_with_branch if os.path.exists(path_with_branch) else path

    print(f"Using the following path to the inputs:\n  {path}\n")
    return path


@pytest.fixture(scope='module')
def path_to_refs(request, env_var='DRAGONS_TEST'):
    """
    PyTest fixture that returns the path to where the reference files for a
    given test module live.

    Parameters
    ----------
    request : fixture
        PyTest's built-in fixture with information about the test itself.

    env_var : str
        Environment variable that contains the root path to the input data.

    Returns
    -------
    str:
        Path to the reference files.
    """
    path_to_test_data = os.getenv(env_var)

    if path_to_test_data is None:
        pytest.skip('Environment variable not set: $DRAGONS_TEST')

    path_to_test_data = os.path.expanduser(path_to_test_data).strip()

    module_path = request.module.__name__.split('.') + ["refs"]
    module_path = [item for item in module_path if item not in "tests"]
    path = os.path.join(path_to_test_data, *module_path)

    if not os.path.exists(path):
        pytest.fail('\n Path to reference test data does not exist: '
                    '\n   {:s}'.format(path))

    if not os.access(path, os.R_OK):
        pytest.fail('\n Path to reference test data exists but is not accessible: '
                    '\n    {:s}'.format(path))

    branch_name = get_active_git_branch()

    if branch_name:
        branch_name = branch_name.replace("/", "_")
        path_with_branch = path.replace("/refs", f"/refs_{branch_name}")
        path = path_with_branch if os.path.exists(path_with_branch) else path

    print(f"Using the following path to the refs:\n  {path}\n")
    return path


@pytest.fixture(scope='module')
def path_to_outputs(request, base_temp):
    """
    PyTest fixture that creates a temporary folder to save tests outputs. You
    can set the base directory by passing the ``--basetemp=mydir/`` argument to
    the PyTest call (See [Pytest - Temporary Directories and Files][1]).

    [1]: https://docs.pytest.org/en/stable/tmpdir.html#temporary-directories-and-files

    Returns
    -------
    str
        Path to the output data.

    Raises
    ------
    IOError
        If output path does not exits.
    """
    module_path = request.module.__name__.split('.')
    module_path = [item for item in module_path if item not in "tests"]
    path = os.path.join(base_temp, *module_path)
    os.makedirs(path, exist_ok=True)

    return path


@pytest.fixture(scope='module')
def path_to_common_inputs(request, env_var='DRAGONS_TEST'):
    """
    PyTest fixture that returns the path to where the common input files
    for a given package live.

    Parameters
    ----------
    request : fixture
        PyTest's built-in fixture with information about the test itself.

    env_var : str
        Environment variable that contains the root path to the input data.

    Returns
    -------
    str:
        Path to the input files (e.g.,
        "/rtfperm/jenkins/dragons/geminidr/common_inputs")
    """
    path_to_test_data = os.getenv(env_var)

    if path_to_test_data is None:
        pytest.skip('Environment variable not set: $DRAGONS_TEST')

    path_to_test_data = os.path.expanduser(path_to_test_data).strip()

    module_path = request.module.__name__.split('.')[:1] + ["common_inputs"]
    path = os.path.join(path_to_test_data, *module_path)

    if not os.path.exists(path):
        raise FileNotFoundError(
            " Could not find path to input data:\n    {:s}".format(path))

    if not os.access(path, os.R_OK):
        pytest.fail('\n  Path to input test data exists but is not accessible: '
                    '\n    {:s}'.format(path))

    branch_name = get_active_git_branch()

    if branch_name:
        branch_name = branch_name.replace("/", "_")
        path_with_branch = path.replace("/common_inputs", f"/common_inputs_{branch_name}")
        path = path_with_branch if os.path.exists(path_with_branch) else path

    print(f"Using the following path to the inputs:\n  {path}\n")
    return path



