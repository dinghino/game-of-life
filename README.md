# Game of Life
A Python 3.6 implementation of Conway's Game of Life, using sets and generator functions

## QuickStart

    pip install -r requirements.txt

    python main.py  # will launch pygame

## Customizing the pattern

To setup patterns there are a couple of ways:

* Some example patterns can be found stored inside the ``states.py`` as set of
  tuple (which is what the game functions expects to receive).
* Some example pattern ``.lif`` files can be found inside the `patterns` folder.
  These can be loaded using the ``states.generate_from_file`` function that
  requires the filepath to the wanted pattern.

Patterns can be found I think everywhere, but the official(?) [website](http://www.conwaylife.com/) wiki section contains a whole collection of
patterns and links to the pattern files. 

> Remember that the ``generate_from_file`` function expects the ``life 1.05``
> version like [this](http://www.conwaylife.com/patterns/pulsar_105.lif)


