from body import Body
import pygame


def draw_bodies(surface: pygame.Surface, bodies: list[Body]) -> None:
    """
    Draws bodies on the screen
    """
    for body in bodies:
        body.draw(surface)
