import pygame
from constants import *


class Body:
    def __init__(
        self,
        name: str,
        x: int,
        y: int,
        mass: int,
        radius: int,
        color: tuple,
        vel_y: int = 0,
    ) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.color = color
        self.vel_y = vel_y
        self.vel_x = 0
        self.acc_x = 0
        self.acc_y = 0
        self.force_x = 0
        self.force_y = 0

    def draw(self, surface) -> None:
        x = self.x * SCALE_DOWN_FACTOR + self.x
        y = self.y * SCALE_DOWN_FACTOR + self.y
        pygame.draw.circle(surface, self.color, (x, y), self.radius)

    def __repr__(self) -> str:
        return f"""
        Name: {self.name}
        Force_x: {self.force_x}
        Force_y: {self.force_y}
        Velocity_x: {self.vel_x}
        Velocity_y: {self.vel_y}
        Acc_x: {self.acc_x}
        Acc_y: {self.acc_y}
        X: {self.x}
        Y: {self.y}
        """
