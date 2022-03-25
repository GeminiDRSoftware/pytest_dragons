"""
Helper functions
================

These are standard functions that we can use in our tests (or in other processes).
"""
import os
import re
import subprocess


def get_active_git_branch():
    """
    Returns the name of the active GIT branch to be used in Continuous
    Integration tasks and organize input/reference files.

    Note: This works currently only if the remote name is "origin", though it
    would be easy to adapt for other cases if needed.

    Returns
    -------
    str or None : Name of the input active git branch. It returns None if
        the branch name could not be retrieved.

    """
    print("Checking for Jenkins branch name for PR")
    jenkins_branch_name = os.getenv('CHANGE_BRANCH', None)
    if jenkins_branch_name:
        print(f"Found Jenkins branch name of {jenkins_branch_name}")
        return jenkins_branch_name
    else:
        print("No Jenkins branch set, reverting to git log to determine branch name")
    branch_re = r'\(HEAD.*, \w+\/([\w\/\.]*)(?:,\s\w+)?\)'
    git_cmd = ['git', 'log', '-n', '1', '--pretty=%d', 'HEAD']
    try:
        out = subprocess.check_output(git_cmd).decode('utf8')
        branch_name = re.search(branch_re, out).groups()[0]
    except Exception as e:
        print("\nCould not retrieve active git branch. Make sure that the\n"
              f"following path is a valid Git repository: {os.getcwd()}\n")
        print(f"git log output was:\n{out}")
        print(f"\nException was:\n{e}")
    else:
        print(f"\nRetrieved active branch name:  {branch_name:s}")
        return branch_name
