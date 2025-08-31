#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, C_WHITE, C_YELLOW

class HowToPlay:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(40, "How the game works:", C_WHITE, ((WIN_WIDTH / 2), 50))

            lines = [
                "Whether you play with 1 or 2 players,",
                "the goal is to reach 1,000 points in the first level",
                "to advance to the next level, which requires 2,000 points.",
                "This makes a total of 3,000 points.",
                "After reaching this total, you win the game,",
                "and a screen will appear to enter your name.",
                "The game also records the time you took to win."
            ]
            for i, line in enumerate(lines):
                self.menu_text(15, line, C_YELLOW, ((WIN_WIDTH / 2), 100 + i * 20))

            # Check de all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
