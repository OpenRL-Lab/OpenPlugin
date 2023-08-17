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
from pathlib import Path


def get_local_plugin_name(plugin_path: str = "./") -> str:
    info_file = Path(plugin_path) / "info.json"

    assert info_file.exists(), "info.json not found"
    info_dict = json.load(open(info_file, "r"))
    assert "plugin_name" in info_dict, "plugin_name not found in info.json"
    plugin_name = info_dict["plugin_name"]
    return plugin_name
