# PySweeper

A Python implementation of Minesweeper using Pygame.

Last tested on Python 3.11 and Pygame version 2.4

## How to run

Preinstalled binaries are on the releases tab

Alternatively you can run the program through the source code if you have pygame installed by doing `python main.py`

To build the program for youself, you will need pyinstaller. Do `make build` and run the program by doing `dist/pysweeper`  

## Game Instructions

Select the difficulty

    1. Easy (8x8, 10 mines)

    2. Medium (18x16, 40 mines)

    3. Hard (18x30, 99 mines)

Left click the squares to select, right click to flag

Press escape key to exit the program. 

## Credits

Images by twitter

Font is Pixelod Sans Bold

# Why did i make this?

This was a small challenge that I decided to do for myself: learn a new Python library in under a week. I achieved that and more.

I decided to bring in some minesweeper code that I made a few months ago, but never got around to using, as my basis for my Pygame. For looks I decided to use Twitter emojis and a custom font in the main menu.

I spent the extra time learning how to make binaries for python using Pyinstaller so that the game could be run without having to install python. I also learned how to set up Github actions so that it would automatically compile them for each OS every time I pushed.

Overall, I felt satisfied with how I made this project. It felt similar to Processing, a language library that I was familiar with, but with a bit more boilerplate.
