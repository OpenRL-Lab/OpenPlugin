#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2023 The OpenRL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""""""
import json
import os
import platform
import re
import shutil
from pathlib import Path
from typing import Dict, Union

import numpy as np

import openplugin

REMOTE_URL = "https://openrl.net/plugin-store/download"


def get_zip_file_url(plugin_name: str) -> str:
    return "{}/{}".format(REMOTE_URL, plugin_name)


def get_plugin_directory() -> Path:
    return Path.home() / ".openplugin" / "plugins"


def get_plugin_list():
    plugin_list = []
    plugin_directory = get_plugin_directory()
    if plugin_directory.is_dir():
        for plugin in plugin_directory.iterdir():
            if plugin.is_dir():
                plugin_list.append(plugin.name)
    return plugin_list


def get_plugin_version(plugin_path: Union[Path, str]) -> str:
    if isinstance(plugin_path, str):
        plugin_path = Path(plugin_path)
    info_file = plugin_path / "info.json"
    assert info_file.exists(), "Plugin info file not found!"

    with open(info_file) as f:
        info = json.load(f)
    return info["version"]


def make_zip_file(dir_to_put_file_in, plugin_directory, plugin_name):
    # create a zip file
    zip_file_name = plugin_name
    zip_file_parent = Path(plugin_directory).parent
    zip_file_path = os.path.join(dir_to_put_file_in, zip_file_name)
    shutil.make_archive(zip_file_path, "zip", zip_file_parent, plugin_directory)
    return os.path.join(dir_to_put_file_in, zip_file_name + ".zip")


def get_system_info() -> Dict[str, str]:
    """
    Retrieve system and python env info for the current system.

    :return: Dictionary summing up the version for each relevant package
        and a formatted string.
    """

    env_info = {
        # In OS, a regex is used to add a space between a "#" and a number to avoid
        # wrongly linking to another issue on GitHub.
        "OS": re.sub(r"#(\d)", r"# \1", f"{platform.platform()} {platform.version()}"),
        "Python": platform.python_version(),
        "OpenPlugin": openplugin.__version__,
        "Numpy": np.__version__,
    }
    return env_info
