This project adds easier way to set up resetting for speedrunning GTFO.

# PLEASE READ THE ENTIRE DOCUMENT IF YOU WANT TO USE IT. FAILURE TO DO SO MEANS YOU WILL NOT GET THIS TO WORK.

## How it works

It uses the LogReaderDLL to grab the data from the current seed. What matters is that it then exposes that into 
an array called `data_pulled` that can be then used by your scripts to check if this seed is good enough. In the
folder called `plugins` you will see scripts for some levels. You will need to write these scripts yourself.

In order to help with this I also provided a few functions in the file `helpers.py` in the same folder. If you
want examples, look at already existing levels.

## How to setup

1. Install AutoHotKey 2.0 from https://www.autohotkey.com/download/
2. Install Python & Pip
3. Download as a zip or clone this project somewhere.
4. Run `py -m pip install -r requirements.txt` in that folder.
5. You may need to modify `setup.py` if your logs are in a different folder or autohotkey is installed somewhere else.

## Plugins

These are the main thing about this program. They are all written in Python and they define one function:

```py 
def check() -> bool:
```

This function returns either True or False if this seed is good enough. You may need to learn how to use python
to make these. However in order to make it easier I provided the `helpers.py` which contain a few usable functions
that should help with most levels. Please take a look in that file and read the comments before each function.

Another thing to note is the names of the items are lowercase but otherwise the exact same as in Logger and also
shown on screen when you reset once through the UI. Consumables and artifacts are not shown however they are present
too under `"ArtifactWorldspawn", "ArtifactContainer", "ConsumableWorldspawn", "ConsumableContainer"`. Resource packs use the names: `"Healthpack"`, `"Ammopack"`, `"ToolRefillpack"`, `"Disinfectpack"`. Uppercases or lowercases don't matter as everything is converted to lowercase anyway.

Once a plugin is setup the program will load it and run that function every time a seed is reset to check if it is
good enough.

## How to run it

1. Check that the level you wish to run has a script in the `plugins` folder. You may need to add a script. Look
   for examples for other levels. Please re-read the section on plugins if you don't know how to.
2. Run `py -m main`.
3. Select the expedition you wish to reset. If you are already in it, you may need to reselect it.
4. Press `windows+N`
