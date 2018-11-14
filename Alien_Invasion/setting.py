#!/usr/bin/env python
#!-*- coding:utf-8 -*-
class Settings():

    def __init__(self):
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed_factor = 2
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        self.fleet_drop_direction = 1
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_speed_factor = 3
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
