Welcome to OpenPlugin!
====================

[`Github <https://github.com/OpenRL-Lab/OpenPlugin>`_] | [`demo video <https://youtu.be/QByu8i9zO04>`_] | [`bilibili video <https://www.bilibili.com/video/BV1AM4y1s7Qu>`_]

OpenPlugin is a toolkit for managing plugins of Large Language Model (LLM).
You can install, uninstall, run and list plugins with ``op`` .

Installation
-------

.. code-block:: bash

    pip install openplugin-py

Plugin Store
-------

We provide plugins in `Plugin Store <https://openrl.net/plugin-store/>`_ . Users can download these plugins and use them with ``op`` .

Usage
-------

* Check OpenPlugin's version with: ``op --version``
* Check system information: ``op --system_info``
* Install a plugin: ``op install <plugin_name>`` . You can also install local plugins with ``op install ./`` .

    * You can also install a plugin from a zip file: ``op install <zip_file_path>`` .

* Uninstall a plugin: ``op install <plugin_name>``
* Start a plugin: ``op run <plugin_name>`` . You can use ``-p`` to specify the port of the plugin. By default, the port is 5003. You can also run a local plugin with ``op run ./`` .
* List installed plugins: ``op list``
* Reinstall plugin: ``op reinstall <plugin_name>``

An example for using QRcode_plugin
-------

* Install QRcode_plugin: ``op install QRcode_plugin``
* Or You can install QRcode_plugin from local:

  * Go to the directory of QRcode_plugin: ``cd plugins/QRcode_plugin``
  * Install QRcode_plugin: ``op install ./``

* Or you can install QRcode_plugin from a zip file: ``op install QRcode_plugin.zip``
* Start QRcode_plugin: ``op run QRcode_plugin -p server_port``
* Or you can start QRcode_plugin from local:

  * Go to the directory of QRcode_plugin: ``cd plugins/QRcode_plugin``
  * Start QRcode_plugin: ``op run ./ -p server_port``

* Then you can get the `ai-plugin.json`` file via visiting ``http://<server_ip>:server_port/ai-plugin.json``
* You can get the ``openaip.yaml`` file via visiting ``http://<server_ip>:server_port/openaip.yaml``



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