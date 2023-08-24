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
from jinja2 import Template


def render_ROOT_URL(text: str, request=None) -> str:
    if request is None:
        return text
    ROOT_URL = request.url_root
    if ROOT_URL.endswith("/"):
        ROOT_URL = ROOT_URL[:-1]

    template = Template(text)
    rendered_text = template.render(ROOT_URL=ROOT_URL)
    # text = text.replace("{{ROOT_URL}}", ROOT_URL)
    return rendered_text
