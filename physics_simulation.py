from typing import Union
import math
from body import Body
from constants import *


class N_Body_Simulation:
    def __init__(self, bodies: list[Body]):
        self.bodies = bodies

    def run_simulation(self) -> None:
        self.update_force()
        self.update_accerlation()
        self.update_velocity()
        self.update_position()

    def update_force(self) -> None:
        for body in self.bodies:

            total_force_x: int = 0
            total_force_y: int = 0

            for other_body in self.bodies:
                if other_body == body:
                    continue
                force_x, force_y = self.calculate_force(body, other_body)
                total_force_x += force_x
                total_force_y += force_y

            body.force_x = total_force_x
            body.force_y = total_force_y

    def update_accerlation(self):
        for body in self.bodies:
            body.acc_x, body.acc_y = self.calculate_acceleration(body)

    def update_velocity(self) -> None:
        for body in self.bodies:
            self.calculate_velocity(body)

    def update_position(self) -> None:
        for body in self.bodies:
            print(body)
            body.x += body.vel_x * TIMESTEP
            body.y += body.vel_y * TIMESTEP

    def calculate_force(self, body1: Body, body2: Body) -> tuple[float, float]:
        distance: float = self.calculate_distance(body1, body2)

        gravitational_force: float = self.calculate_gravitational_force(
            body1, body2, distance
        )
        angle: float = self.calculate_angle(body1, body2)

        return self.calculate_force_x_y(gravitational_force, angle)

    def calculate_velocity(self, body: Body) -> float:
        body.vel_x += body.acc_x * TIMESTEP
        body.vel_y += body.acc_y * TIMESTEP

    def calculate_acceleration(self, body: Body) -> float:
        return body.force_x / body.mass, body.force_y / body.mass

    def calculate_distance(self, body1: Body, body2: Body) -> float:
        """
        Calculates the distance between two bodies by using Pythagorean theorem
        """
        return math.sqrt((body2.x - body1.x) ** 2 + (body2.y - body1.y) ** 2)

    def calculate_gravitational_force(
        self, body1: Body, body2: Body, distance: Union[int, float]
    ) -> float:
        """
        Calculates the gravitational force by using the formula (G * m1 * m2)/(distance**2)
        """
        return (G * body1.mass * body2.mass) / (distance ** 2)

    def calculate_angle(self, body1: Body, body2: Body) -> float:
        """
        Calculates the angle between two planets by using trigonometry
        """
        return math.atan2(body2.y - body1.y, body2.x - body1.x)

    def calculate_force_x_y(self, force: float, angle: float) -> tuple[float, float]:
        return math.cos(angle) * force, math.sin(angle) * force
