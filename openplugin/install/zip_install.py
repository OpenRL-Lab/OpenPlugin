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

import shutil
import tempfile
import zipfile
from pathlib import Path

from openplugin.utils.local_plugin_utils import get_local_plugin_name
from openplugin.utils.util import (
    get_plugin_directory,
    get_plugin_list,
    get_plugin_version,
)


def install_zip_plugin(plugin_zip_file_path: str) -> bool:
    assert plugin_zip_file_path.endswith(".zip")

    tempdir = tempfile.mkdtemp()
    z = zipfile.ZipFile(plugin_zip_file_path)
    z.extractall(tempdir)

    plugin_name = get_local_plugin_name(Path(tempdir).iterdir().__next__())
    shutil.rmtree(tempdir, ignore_errors=True)
    plugin_list = get_plugin_list()
    if plugin_name in plugin_list:
        print("Plugin {} already installed!".format(plugin_name))
        return True

    try:
        plugin_directory = get_plugin_directory()
        if not plugin_directory.exists():
            plugin_directory.mkdir(parents=True)
        print("Extracting plugin to {}".format(plugin_directory / plugin_name))
        z.extractall(get_plugin_directory())
        plugin_version = get_plugin_version(plugin_directory / plugin_name)
    except:
        raise ValueError("Install {} failed".format(plugin_name))

    print("Installed plugin: {}:{}!".format(plugin_name, plugin_version))
    return True
