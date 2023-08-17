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

import os
import shutil
import tempfile
import zipfile

from openplugin.utils.check import check_local_plugin
from openplugin.utils.local_plugin_utils import get_local_plugin_name
from openplugin.utils.util import (
    get_plugin_directory,
    get_plugin_version,
    make_zip_file,
)


def install_local_plugin() -> bool:
    local_plugin_directory = "./"
    plugin_name = get_local_plugin_name(local_plugin_directory)
    print("Installing plugin: {}...".format(plugin_name))

    success, message = check_local_plugin(local_plugin_directory)
    if not success:
        print("Error: {}".format(message))
        return False
    tempdir = tempfile.mkdtemp()
    filepath = make_zip_file(
        dir_to_put_file_in=tempdir,
        plugin_directory=local_plugin_directory,
        plugin_name=plugin_name,
    )

    z = zipfile.ZipFile(filepath)
    plugin_directory = get_plugin_directory()
    if not plugin_directory.exists():
        plugin_directory.mkdir(parents=True)
    print("Extracting plugin to {}".format(plugin_directory / plugin_name))
    z.extractall(os.path.join(get_plugin_directory(), plugin_name))
    shutil.rmtree(tempdir, ignore_errors=True)
    plugin_version = get_plugin_version(plugin_directory / plugin_name)
    print("Installed plugin: {}:{}!".format(plugin_name, plugin_version))
    return True
