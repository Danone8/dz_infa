from random import randint

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""


def calculate_angular_velocity(body, star):
    dx = body.x - star.x
    dy = body.y - star.y
    vx = body.Vx - star.Vx
    vy = body.Vy - star.Vy
    r2 = dx**2 + dy**2
    body.omega = (dx * vy - dy * vx) / r2
    body.area_speed = (dx * vy - dy * vx) / 2
    if not hasattr(body, 'initial_area_speed'):
        body.initial_area_speed = body.area_speed
        body.max_error = 0

    if body.initial_area_speed != 0:
        error = abs((body.area_speed - body.initial_area_speed) / body.initial_area_speed) * 100
        body.max_error = max(body.max_error, error)
        print(f'ω = {body.omega:.6e} рад/с; dS/dt = {body.area_speed:.6e} м²/с; отклонение до {body.max_error:.3e}%')
    else:
        print(f'ω = {body.omega:.6e} рад/с; dS/dt = {body.area_speed:.6e} м²/с')
    
def calculate_force(body, space_objects):
    body.Fx = 0
    body.Fy = 0

    for obj in space_objects:
        if body is obj:
            continue
        dx = obj.x - body.x
        dy = obj.y - body.y
        r = (dx**2 + dy**2)**0.5
        k = gravitational_constant * body.m * obj.m / r**3
        body.Fx += k * dx
        body.Fy += k * dy


def move_space_object(body, dt):
    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.Vx += ax * dt
    body.Vy += ay * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    star = None
    for body in space_objects:
        if body.type == 'star':
            star = body
            break
    if star is not None:
        for body in space_objects:
            if body.type == 'planet':
                calculate_angular_velocity(body, star)

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)

if __name__ == "__main__":
    print("This module is not for direct call!")