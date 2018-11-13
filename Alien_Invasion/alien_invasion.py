#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import sys

import pygame

from ship import Ship

from setting import Settings

from pygame.sprite import Group

import game_functions as gf

from alien import Alien



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bg_color = (230, 230, 230)
    bullets = Group()
    aliens = Group()
    alien = Alien(ai_settings, screen)
    gf.update_screen(ai_settings, screen, ship, alien, bullets)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()


