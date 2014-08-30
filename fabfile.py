import os
import time

from fabric.api import local, lcd, settings, task
from fabric.utils import puts

try:
    from local_settings import OUTPUT_PATH
    SETTINGS_FILE = "local_settings.py"
except ImportError:
    from settings import OUTPUT_PATH
    SETTINGS_FILE = "settings.py"


# Get directories
ABS_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ABS_SETTINGS_FILE = os.path.join(ABS_ROOT_DIR, SETTINGS_FILE)
ABS_OUTPUT_PATH = os.path.join(ABS_ROOT_DIR, OUTPUT_PATH)
TARGET_DIR = os.path.join(ABS_ROOT_DIR, 'content')
REMOTE = 'origin'
BRANCH = 'master'


@task
def html(settings_file=None):
    """Generates the pelican static site"""
    settings_file = settings_file or ABS_SETTINGS_FILE
    cmd = "pelican -s {0} {1}".format(settings_file, TARGET_DIR)
    local(cmd)


@task
def clean():
    """Destroys the pelican static site"""

    cmd = "rm -r {0}".format(os.path.join(ABS_OUTPUT_PATH, '*'))

    with settings(warn_only=True):
        result = local(cmd)

    if result.failed:
        puts("Already deleted")


@task
def serve():
    """Serves the site in the development webserver"""
    print(ABS_OUTPUT_PATH)
    with lcd(ABS_OUTPUT_PATH):
        local("python -m SimpleHTTPServer")


def git_change_branch(branch):
    """Changes from one branch to other in a git repo"""
    local("git checkout {0}".format(branch))


def git_merge_branch(branch):
    """Merges a branch in other branch"""
    local("git merge {0}".format(branch))


def git_push(remote, branch):
    """Pushes the git changes to git remote repo"""
    local("git push {0} {1}".format(remote, branch))


def git_commit_all(msg):
    """Commits all the changes"""
    local("git add .")
    local("git commit -m \"{0}\"".format(msg))


@task
def publish():
    """Generates and publish the new site in github pages"""
    html()

    # Commit changes and push
    now = time.strftime("%d %b %Y %H:%M:%S", time.localtime())
    with lcd(ABS_OUTPUT_PATH):
        git_commit_all("Publication {0}".format(now))
        git_push(REMOTE, BRANCH)


@task
def preview():
    """Generate preview version of the site with hard links to local files."""
    settings_file = os.path.join(ABS_ROOT_DIR, 'preview_config.py')
    html(settings_file)
    serve()
