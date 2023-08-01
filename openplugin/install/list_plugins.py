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
from openplugin.utils.util import (
    get_plugin_directory,
    get_plugin_list,
    get_plugin_version,
)


def list_plugins() -> bool:
    plugin_list = get_plugin_list()
    plugin_directory = get_plugin_directory()
    print("Installed plugins:")
    for plugin in plugin_list:
        plugin_version = get_plugin_version(plugin_directory / plugin)
        print(f"{plugin}:{plugin_version}")
