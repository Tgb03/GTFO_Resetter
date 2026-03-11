import importlib
import pathlib

PLUGIN_DIR = pathlib.Path("plugins")

plugins = {}

def load_plugins():
    for file in PLUGIN_DIR.glob("*.py"):
        if file.name.startswith("_"):
            continue

        module_name = f"plugins.{file.stem}"
        module = importlib.import_module(module_name)

        if hasattr(module, "check"):
            plugins[file.stem] = module.check