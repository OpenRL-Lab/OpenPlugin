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
import sys
from openplugin.utils.app_util import import_app
def run_plugin(plugin_name):
    os.chdir(f"./plugins/{plugin_name}")
    sys.path.append('./')
    try:
        app = import_app("main:app")
    except:
        raise ValueError("plugin {} not found".format(plugin_name))
    print("running plugin: {}...".format(plugin_name))
    app.run(debug=True, host="0.0.0.0", port=5003)
