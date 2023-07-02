# OpenPlugin

[![PyPI](https://img.shields.io/pypi/v/openplugin-py)](https://pypi.org/project/openplugin-py/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/openplugin-py)
[![Hits-of-Code](https://hitsofcode.com/github/OpenRL-Lab/OpenPlugin?branch=main)](https://hitsofcode.com/github/OpenRL-Lab/OpenPlugin/view?branch=main)

Toolkit for managing plugins of Large Language Model (LLM). You can install, uninstall, run and list plugins with `op`.

## Installation

- `pip install openplugin-py` (or clone this repo and `pip install -e .`).

## Usage

- Check OpenPlugin's version with: `op --version`
- Check system information: `op --system_info`
- Install a plugin: `op install <plugin_name>`
- Uninstall a plugin: `op install <plugin_name>`
- Start a plugin: `op run <plugin_name>`. You can use `-p` to specify the port of the plugin.
- List installed plugins: `op list`

## An example for using ikun_plugin

- Install ikun_plugin: `op install ikun_plugin`
- Start ikun_plugin: `op run ikun_plugin -p server_port`
- Then you can get the `ai-plugin.json` file via visiting `http://<server_ip>:server_port/ai-plugin.json`
- You can get the `openaip.yaml` file via visiting `http://<server_ip>:server_port/openaip.yaml`

## Citing OpenPlugin

If our work has been helpful to you, please feel free to cite us:
```latex
@misc{openplugin2023,
    title={OpenPlugin},
    author={OpenRL Contributors},
    publisher = {GitHub},
    howpublished = {\url{https://github.com/OpenRL-Lab/openplugin}},
    year={2023},
}
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=OpenRL-Lab/OpenPlugin&type=Date)](https://star-history.com/#OpenRL-Lab/OpenPlugin&Date)
