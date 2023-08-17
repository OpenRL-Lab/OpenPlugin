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
from typing import Tuple, Union


def check_info_file(info_file: Union[str, Path]) -> Tuple[bool, str]:
    """Check if the given info file is valid."""
    message = ""
    success = True
    if isinstance(info_file, str):
        info_file = Path(info_file)
    if not info_file.exists():
        success = False
        message = f"Info file {info_file} does not exist."
    else:
        info = json.load(open(info_file))
        must_have_keys = ["plugin_name", "version", "description"]
        if not all((k in info) for k in must_have_keys):
            success = False
            message = f"Info file {info_file} does not contain all required keys."
    return success, message


def check_local_plugin(plugin_path: Union[str, Path]) -> Tuple[bool, str]:
    """Check if the given path is a valid local plugin."""
    message = ""
    success = True
    if isinstance(plugin_path, str):
        plugin_path = Path(plugin_path)

    must_have_files = ["info.json", "ai-plugin.json", "openapi.yaml"]

    if not plugin_path.exists():
        success = False
        message = f"Plugin path {plugin_path} does not exist."
    elif not plugin_path.is_dir():
        success = False
        message = f"Plugin path {plugin_path} is not a directory."
    elif not all((plugin_path / f).exists() for f in must_have_files):
        success = False
        message = f"Plugin path {plugin_path} does not contain all required files."
    else:
        success, message = check_info_file(plugin_path / "info.json")
    return success, message
