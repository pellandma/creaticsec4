import arcade
import random

# VARIABLES
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []


class cercle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rayon = random.randint(0, 30)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.angle = random.randint(0, 30)
        self.vitesse_x = random.randint(-100, 100)
        self.vitesse_y = random.randint(-100, 100)

    def update(self, delta_time):
        if self.x < 5 or self.x > 795:
            self.vitesse_x *= -1
        if self.y < 5 or self.y > 595:
            self.vitesse_y *= -1
        self.x += self.vitesse_x * delta_time
        self.y += self.vitesse_y * delta_time

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color, 56)

class rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rayon = random.randint(0, 30)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.angle = random.randint(0, 30)
        self.vitesse_x = random.randint(-100, 100)
        self.vitesse_y = random.randint(-100, 100)

    def update(self, delta_time):
        if self.x < 5 or self.x > 795:
            self.vitesse_x *= -1
        if self.y < 5 or self.y > 595:
            self.vitesse_y *= -1
        self.x += self.vitesse_x * delta_time
        self.y += self.vitesse_y * delta_time

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.rayon, self.angle, self.color, 56)


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.list_cercle = []
        self.liste_rectangle = []
        self.flag = True
        self.vitesse = 100
        pass

    def setup(self):

        pass

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.list_cercle.append(cercle(x,y))

        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.liste_rectangle.append(rectangle(x, y))

    def update(self, delta_time):

        for cercle in self.list_cercle:
            cercle.update(0.1)

        for rectangle in self.liste_rectangle:
            rectangle.update(0.1)

    def on_draw(self):

        arcade.start_render()
        for cercle in self.list_cercle:
            cercle.draw()
        for rectangle in self.liste_rectangle:
            rectangle.draw()
        arcade.finish_render()


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
