import inspect

# Используем модуль
from playground.ext import subpkg1
subpkg1.start()

# Используем плагин
from importlib.metadata import entry_points

if False:
    discovered_plugins = entry_points(group='playground.plugins')
    plugins = filter(lambda plugin: plugin.name == 'myplugin', discovered_plugins)
    for plugin in plugins:
        print(plugin.load())
else:
    (myplugin,) = entry_points(group='playground.plugins', name='myplugin')
    print(myplugin)
    module = myplugin.load()
    module.start()
    # Это эквивалент: 
    # from playground.core.plugins.myplugin import start
    # start()
