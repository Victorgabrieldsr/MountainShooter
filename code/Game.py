#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass