#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import sys

import pygame

from ship import Ship

from setting import Settings

from pygame.sprite import Group

import game_functions as gf

from alien import Alien

from game_stats import GameStats



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
    gf.create_fleet(ai_settings, screen, ship,aliens)
    gf.update_screen(ai_settings, screen, ship, aliens, bullets)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats,screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()


