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
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from openplugin.template.utils import render_ROOT_URL


class BaseTemplate(ABC):
    def __init__(self, template_file: Union[str, Path]):
        self.template_file = template_file
        self._load_text()

    def _load_text(self):
        with open(self.template_file) as f:
            text = f.read()
            self.text = text

    @abstractmethod
    def render(self, request=None) -> str:
        raise NotImplementedError
