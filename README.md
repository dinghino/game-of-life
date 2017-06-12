# Game of Life
A Python 3.6 implementation of Conway's Game of Life, using sets and generator functions and ``pygame`` to make it alive.

## QuickStart

    pip install -r requirements.txt

    python main.py # will launch pygame

### Optional arguments

* ``-p`` (``--pattern``): relative path to the pattern to play
* ``-i`` (``--iterations``): number of iterations to play
* ``-f`` (``--fps``): frames per seconds (animation speed)
* ``-h``: shows help

## Customizing the pattern

To setup patterns there are a couple of ways:

* Some example patterns can be found stored inside the ``states.py`` as set of
  tuple (which is what the game functions expects to receive).
* Some example pattern ``.lif`` files can be found inside the `patterns` folder.
  These can be loaded using the ``states.generate_from_file`` function that
  requires the filepath to the wanted pattern.

> Patterns can be found I think everywhere, but the official(?) [website](http://www.conwaylife.com/) wiki section contains a whole collection of
patterns and links to the pattern files. 

To add a pattern simply get the ``.fil`` from the website, add it to the
patterns folder and call

    python main.py -p ./game/patterns/my_pattern.lif

# License

Release under [MIT](/LICENSE) license.