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

from openplugin.install.local_install import install_local_plugin
from openplugin.install.remote_install import remote_install
from openplugin.install.uninstall import uninstall_plugin
from openplugin.install.zip_install import install_zip_plugin


def install_plugin(plugin_name: str) -> bool:
    if plugin_name == "./" or plugin_name == ".":
        print("Installing current directory as plugin...")
        return install_local_plugin()

    if plugin_name.endswith(".zip"):
        print("Installing plugin from zip file...")
        return install_zip_plugin(plugin_name)

    return remote_install(plugin_name)


def reinstall_plugin(plugin_name: str) -> bool:
    uninstall_plugin(plugin_name)
    return install_plugin(plugin_name)
