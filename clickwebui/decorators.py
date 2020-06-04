import os
from distutils.util import strtobool

import click

from clickwebui.const import CLICK_WEBUI_ENV
from clickwebui.core import WebCommandView


def make_ui(cmd: click.Command):
    if strtobool(os.getenv(CLICK_WEBUI_ENV, 'True')):
        return WebCommandView(cmd)
    else:
        return cmd
