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
import io
import zipfile

import requests

from openplugin.utils.util import (
    get_plugin_directory,
    get_plugin_list,
    get_plugin_version,
    get_zip_file_url,
)


def remote_install(plugin_name: str) -> bool:
    plugin_list = get_plugin_list()
    if plugin_name in plugin_list:
        print("Plugin {} already installed!".format(plugin_name))
        return True

    print("Installing plugin: {}...".format(plugin_name))
    zip_file_url = get_zip_file_url(plugin_name)
    try:
        print("Downloading plugin from {}".format(zip_file_url))
        r = requests.get(zip_file_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        plugin_directory = get_plugin_directory()
        if not plugin_directory.exists():
            plugin_directory.mkdir(parents=True)
        print("Extracting plugin to {}".format(plugin_directory / plugin_name))
        z.extractall(get_plugin_directory())
        plugin_version = get_plugin_version(plugin_directory / plugin_name)
    except:
        raise ValueError("plugin {} not found".format(plugin_name))
    print("Installed plugin: {}:{}!".format(plugin_name, plugin_version))
    return True
