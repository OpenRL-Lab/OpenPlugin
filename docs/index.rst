Welcome to OpenPlugin!
====================

[`Github <https://github.com/OpenRL-Lab/OpenPlugin>`_]

OpenPlugin is a toolkit for managing plugins of Large Language Model (LLM).
You can install, uninstall, run and list plugins with `op` .

Installation
-------

.. code-block:: bash

    pip install openplugin-py


Usage
-------

- Check OpenPlugin's version with: `op --version`
- Check system information: `op --system_info`
- Install a plugin: `op install <plugin_name>`
- Uninstall a plugin: `op install <plugin_name>`
- Start a plugin: `op run <plugin_name>` . You can use `-p` to specify the port of the plugin. By default, the port is 5003.
- List installed plugins: `op list`
- Reinstall plugin: `op reinstall <plugin_name>`

An example for using ikun_plugin
-------

- Install ikun_plugin: `op install ikun_plugin`
- Start ikun_plugin: `op run ikun_plugin -p server_port`
- Then you can get the `ai-plugin.json` file via visiting `http://<server_ip>:server_port/ai-plugin.json`
- You can get the `openaip.yaml` file via visiting `http://<server_ip>:server_port/openaip.yaml`



Plugins
-------

We provide some source codes of plugins. You can find them in `plugins <https://github.com/OpenRL-Lab/OpenPlugin/tree/main/plugins>`_ .
We call for contributions of plugins.
You can fork our repo, add your plugin into `plugins <https://github.com/OpenRL-Lab/OpenPlugin/tree/main/plugins>`_  and submit a Pull Request.


Citing OpenPlugin
-----------------

If our work has been helpful to you, please feel free to cite us:

.. code-block:: bibtex

    @misc{openplugin2023,
        title={OpenPlugin},
        author={OpenRL Contributors},
        publisher = {GitHub},
        howpublished = {\url{https://github.com/OpenRL-Lab/OpenPlugin}},
        year={2023},
    }