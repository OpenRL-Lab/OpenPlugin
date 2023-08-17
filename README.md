# OpenPlugin

[![PyPI](https://img.shields.io/pypi/v/openplugin-py)](https://pypi.org/project/openplugin-py/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/openplugin-py)
[![Hits-of-Code](https://hitsofcode.com/github/OpenRL-Lab/OpenPlugin?branch=main)](https://hitsofcode.com/github/OpenRL-Lab/OpenPlugin/view?branch=main)

[![Documentation Status](https://readthedocs.org/projects/openplugin/badge/?version=latest)](https://openplugin.readthedocs.io/en/latest/?badge=latest)

[[demo video](https://youtu.be/QByu8i9zO04)] | [[bilibili video](https://www.bilibili.com/video/BV1AM4y1s7Qu)]

OpenPlugin-v0.0.8 is updated on Aug 17, 2023

Toolkit for managing plugins of Large Language Model (LLM). You can install, uninstall, run and list plugins with `op`.

## Installation

- `pip install openplugin-py` (or clone this repo and `pip install -e .`).


## Plugin Store

We provide plugins in [Plugin Store](https://openrl.net/plugin-store/). Users can download these plugins and use them with `op`.

## Usage

- Check OpenPlugin's version with: `op --version`
- Check system information: `op --system_info`
- Install a plugin: `op install <plugin_name>`. You can also install local plugins with `op install .`.
  - You can also install a plugin from a zip file: `op install <zip_file_path>`.
- Uninstall a plugin: `op uninstall <plugin_name>`
- Start a plugin: `op run <plugin_name>`. You can use `-p` to specify the port of the plugin. By default, the port is 5003.  You can also run a local plugin with `op run ./`.
- List installed plugins: `op list`
- Reinstall plugin: `op reinstall <plugin_name>`

## An example for using QRcode_plugin

- Install QRcode_plugin: `op install QRcode_plugin`
- Or You can install QRcode_plugin from local:
  - Go to the directory of QRcode_plugin: `cd plugins/QRcode_plugin`
  - Install QRcode_plugin: `op install .`
- Or you can install QRcode_plugin from a zip file: `op install QRcode_plugin.zip`
- Start QRcode_plugin: `op run QRcode_plugin -p server_port`
- Or you can start QRcode_plugin from local:
  - Go to the directory of QRcode_plugin: `cd plugins/QRcode_plugin`
  - Start QRcode_plugin: `op run ./ -p server_port`
- Then you can get the `ai-plugin.json` file via visiting `http://<server_ip>:server_port/ai-plugin.json`
- You can get the `openaip.yaml` file via visiting `http://<server_ip>:server_port/openaip.yaml`

## Plugins

We provide some source codes of plugins. You can find them in [plugins](./plugins). 
We call for contributions of plugins. 
You can fork our repo, add your plugin into [plugins](./plugins) and submit a Pull Request.


## Citing OpenPlugin

If our work has been helpful to you, please feel free to cite us:
```latex
@misc{openplugin2023,
    title={OpenPlugin},
    author={OpenRL Contributors},
    publisher = {GitHub},
    howpublished = {\url{https://github.com/OpenRL-Lab/OpenPlugin}},
    year={2023},
}
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=OpenRL-Lab/OpenPlugin&type=Date)](https://star-history.com/#OpenRL-Lab/OpenPlugin&Date)
