
*Author's Note: This was a project I wrote in High School in 2007.
I am trying to preserve it for posterity in as close to its original form as possible.
So a lot of this README is no longer relevant, but I want to preserve it.*

# Nottris 0.2

This version does not introduce any new features, it only cleaned up the code to make it more readable and extendable.
To play, run `game.py`

--------------

This is my attempt at a version of an unnamed popular video game, programmed in Python.
This is a *very* beta release. Any feedback would be appreciated.
The current features are as follows:

* Authentic _Nintendo left-hand_ rotation system.
* Pretty graphics.
* Scoring.
* Timer

While the feature list is fairly small, it is very playable, thus the release.

## Usage:

This game requires [Python](http://python.org) 2.4 or later.
A direct link to the [Windows installer](http://www.python.org/ftp/python/2.5/python-2.5.msi) is provided for your convenience.

[PyGame](http://pygame.org) 1.7+ is also required.
Direct link to [Windows PyGame installer](http://pygame.org/ftp/pygame-1.7.1release.win32-py2.5.exe).

Simply unarchive the nottris folder somewhere, and double-click `game.py` to run the game.

## Controls:
```
Z, Up arrow - rotate clockwise.
X - rotate counter-clockwise.
Left Arrow - Move piece left.
Right Arrow - Move piece right.
Down Arrow - Drop piece faster.
Escape - Quit
```
## Known bugs:

* While not a bug, the game exits immediately upon a loss. Take note of your score *before* you die.
* There is a minor problem with the lockdown time of blocks.

Special thanks to Scott for making the fancy colored blocks.

## License:

GPL v3. See LICENSE file

- Kyle Wilcox
