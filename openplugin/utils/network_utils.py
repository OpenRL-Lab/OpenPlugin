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


import urllib.request

IP_WEBSITES = (
    "https://ipinfo.io/ip",
    "https://ipecho.net/plain",
    "https://api.ipify.org",
    "https://ipaddr.site",
    "https://icanhazip.com",
    "https://ident.me",
    "https://curlmyip.net",
)


def getIp():
    for ipWebsite in IP_WEBSITES:
        try:
            response = urllib.request.urlopen(ipWebsite)

            charsets = response.info().get_charsets()
            if len(charsets) == 0 or charsets[0] is None:
                charset = "utf-8"  # Use utf-8 by default
            else:
                charset = charsets[0]

            userIp = response.read().decode(charset).strip()

            return userIp
        except:
            pass  # Network error, just continue on to next website.

    # Either all of the websites are down or returned invalid response
    # (unlikely) or you are disconnected from the internet.
    return None


local_addresses = ["0.0.0.0", "127.0.0.1"]


def display_host_info(ip, host):
    print(f"Launched at {ip}:{host}")
    print(f"\tYou can get json file at {ip}:{host}/ai-plugin.json")
    print(f"\tYou can get YAML file at {ip}:{host}/openapi.yaml")
