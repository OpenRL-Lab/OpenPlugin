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

from openplugin.plugin.webapp_plugin import WebAppPlugin
from openplugin.utils.local_plugin_utils import get_local_plugin_name


def run_local_plugin(host: str, port: int) -> bool:
    plugin_name = get_local_plugin_name()
    print("Installing plugin: {}...".format(plugin_name))
    plugin = WebAppPlugin(plugin_name, plugin_path="./")
    plugin.run(host, port)
    return True
