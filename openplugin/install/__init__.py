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
import os
import shutil
import zipfile
import tempfile

from pathlib import Path
import requests
import json

from openplugin.utils.util import (
    get_plugin_directory,
    get_plugin_list,
    get_zip_file_url,
    make_zip_file,
)
# import urllib
def install_plugin(plugin_name: str) -> bool:
    if plugin_name == "./":
        print("Installing current directory as plugin...")
        return install_local_plugin()

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
    except:
        raise ValueError("plugin {} not found".format(plugin_name))
    print("Installed plugin: {}!".format(plugin_name))
    return True
    # urllib.request.urlretrieve(zip_file_url, f'{plugin_name}.zip')

def install_local_plugin() -> bool:
    info_file = Path("info.json")
    assert info_file.exists(), "info.json not found"
    info_dict = json.load(open("info.json", "r"))
    assert "plugin_name" in info_dict, "plugin_name not found in info.json"
    plugin_name = info_dict["plugin_name"]
    print("Installing plugin: {}...".format(plugin_name))

    tempdir = tempfile.mkdtemp()
    filepath = make_zip_file(dir_to_put_file_in=tempdir,
                             plugin_directory="./", plugin_name = plugin_name)

    z = zipfile.ZipFile(filepath)
    plugin_directory = get_plugin_directory()
    if not plugin_directory.exists():
        plugin_directory.mkdir(parents=True)
    print("Extracting plugin to {}".format(plugin_directory / plugin_name))
    z.extractall(os.path.join(get_plugin_directory(),plugin_name))
    shutil.rmtree(tempdir, ignore_errors=True)
    return True
def uninstall_plugin(plugin_name: str) -> bool:
    plugin_list = get_plugin_list()
    if plugin_name not in plugin_list:
        print("Plugin {} not installed!".format(plugin_name))
        return True

    plugin_path = get_plugin_directory() / plugin_name
    if plugin_path.exists() and plugin_path.is_dir():
        shutil.rmtree(plugin_path)
    print("Uninstalled plugin: {}!".format(plugin_name))


def reinstall_plugin(plugin_name: str) -> bool:
    uninstall_plugin(plugin_name)
    return install_plugin(plugin_name)


def list_plugins() -> bool:
    plugin_list = get_plugin_list()
    print("Installed plugins:")
    for plugin in plugin_list:
        print(plugin)
