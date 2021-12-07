# PyWorks

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A basic pygame framework, made to be expandable and facilitate faster development of games and visualizations.

This project was born out of a need for a multipurpose object oriented pygame program. This project takes heavy inspiration from how I code in C++.

## Information

Currently, the framework includes:

- Creating a window
- Processing user input
- Loading config externally
- A debug FPS counter

## Future plans

- File based configuration (.ini)
- Logging
- Better documentation

## Example Usage

    import sys
    import pygame
    from .core.engine import Engine

    engine = Engine()
    engine.start()
    
    while engine.running:
        engine.main_loop()
    pygame.quit()
    sys.exit(0)

## Requirements

To install requirements you can run
> pip install -r requirements.txt

Or you can install the packages manually if you want:

- python >= 3.9
- pygame >= 2.1.0

## Licence

This project uses the MIT licence. Please view the LICENCE file for more information.
