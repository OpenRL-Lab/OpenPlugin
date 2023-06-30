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
import subprocess
import sys

import pytest


@pytest.mark.unittest
def test_version():
    from openplugin.cli.cli import print_version

    print_version(ctx=None, param=None, value=False)
    out = subprocess.check_output("op --version".split())
    assert "OPENPLUGIN version" in out.decode("utf-8")


@pytest.mark.unittest
def test_system_info():
    out = subprocess.check_output("op --system_info".split())
    assert "OpenPlugin" in out.decode("utf-8")


if __name__ == "__main__":
    sys.exit(pytest.main(["-sv", os.path.basename(__file__)]))
