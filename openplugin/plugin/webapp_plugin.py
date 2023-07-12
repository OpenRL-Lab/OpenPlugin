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

import ifaddr

from openplugin.plugin.base_plugin import BasePlugin
from openplugin.utils.app_util import import_app
from openplugin.utils.network_utils import display_host_info, getIp, local_addresses


class WebAppPlugin(BasePlugin):
    def run(self, host: str, port: int):
        os.chdir(self.plugin_path)
        sys.path.append("./")
        try:
            print("Loading plugin from {}".format(self.plugin_path))
            app = import_app("main:app")
        except:
            raise ValueError("plugin {} not found".format(self.plugin_name))

        print("Running plugin: {} on {}:{}".format(self.plugin_name, host, port))

        ips = set()
        outip = getIp()
        if outip is not None:
            ips.add(outip)
        ips.add("0.0.0.0")
        adapters = ifaddr.get_adapters()

        for adapter in adapters:
            # print("IPs of network adapter " + adapter.nice_name)
            for ip in adapter.ips:
                # print("   %s/%s" % (ip.ip, ip.network_prefix))
                ip_address = ip.ip
                if (
                    isinstance(ip_address, str)
                    and "(" not in ip_address
                    and ":" not in ip_address
                    and ip_address not in local_addresses
                    and not ip_address.startswith("192.168")
                ):
                    ips.add(ip_address)

        if len(ips) > 0:
            for ip in ips:
                display_host_info(ip, port)

        app.run(debug=True, host=host, port=port)
