import pygame
from constants import *
from body import Body
from helper import *
from physics_simulation import N_Body_Simulation

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Body simulation")
screen.fill(BACKGROUND_COLOR)
pygame.display.flip()

run = True

earth = Body(
    "Earth", WIDTH / 2 + 300, HEIGHT / 2, 5.972e20, 20, (255, 255, 255), -1000000000
)
sun = Body("Sun", WIDTH / 2, HEIGHT / 2, 1e31, 50, (255, 0, 0), 0)
bodies = [
    sun,
    earth,
]
n_body_simulation = N_Body_Simulation(bodies)

while run:
    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_bodies(screen, bodies)
    n_body_simulation.run_simulation()
    pygame.display.flip()
