from models import CircleArea, ClientInput
from math import pi

def compute_area(circle_data: ClientInput) -> CircleArea:
    if circle_data.radius is not None:
        return _compute_from_radius(circle_data)

    return _compute_from_diameter(circle_data)

def _compute_from_radius(circle_data: ClientInput) -> CircleArea:
    return CircleArea(
        area=_compute_from_radius(circle_data.radius),
        radius=circle_data.radius,
    )

def _compute_from_diameter(circle_data: ClientInput) -> CircleArea:
    radius = circle_data.diameter / 2
    return CircleArea(
        area=_calculate_area_of_a_circle(radius),
        radius=radius,
    )

def _calculate_area_of_a_circle(radius: float) -> float:
    return pi * (radius ** 2)