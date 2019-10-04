#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program draws a background and two sprites on the pybadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# list of sprites
sprites = []


def main():
    # this function sets the background

    # sets the background to image 0 in the bank
    # backgrounds do not have magents as a transparent color
    background = stage.Grid(image_bank_1, 10, 8)

    # create a sprite
    # parameters (image bank, image # in bank, x, y)
    alien = stage.Sprite(image_bank_1, 4, 4, 5)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 6, 12, 10)
    sprites.insert(0, ship)  # insert at top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = sprites + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, or you turn it off!
    while True:
        # get user input

        # update game logic

        game.render_sprites(sprites)
        game.tick()  # wait for refresh rate to finish


if __name__ == "__main__":
    main()
