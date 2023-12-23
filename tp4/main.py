import arcade
import random

#VARIABLES
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []





    

        

           
       
class rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rayon = random.randint(10,30)
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.angle = random.randint(3, 150)
        self.vitesse_x = random.randint(-100,100)
        self.vitesse_y = random.randint(-100,100)
    def changement_vitesse(self, new_x, new_y):
        self.x += new_x
        self.y += new_y
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.rayon,self.angle, self.color, 56)
    
        
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
            rayon = random.randint(10,30)
            color = random.randint(0,255), random.randint(0,255), random.randint(0,255)
            vitesse_x = random.randint(-100, 100)
            vitesse_y = random.randint(-100, 100)
            self.list_cercle.append([x, y, rayon, color, vitesse_x, vitesse_y])
            
        if button == arcade.MOUSE_BUTTON_RIGHT:
            
            self.liste_rectangle.append(rectangle(x,y))
            
   def on_update(self, delta_time):
           
       for cercle in self.list_cercle:
           if cercle[0] < 5 or cercle[0] > 795:
            cercle[4] *= -1
           if cercle[1] < 5 or cercle[1] > 595:
            cercle[5] *= -1
           cercle[0] += cercle[4] * delta_time
           cercle[1] += cercle[5]* delta_time  
       for rectangle in self.liste_rectangle:
           if rectangle.x < 5 or rectangle.x > 795:
            rectangle.vitesse_x *= -1
           if rectangle.y < 5 or rectangle.y > 595:
            rectangle.vitesse_y *= -1
           rectangle.x += rectangle.vitesse_x * delta_time
           rectangle.y += rectangle.vitesse_y * delta_time
                   


   def on_draw(self):
        
        arcade.start_render()
        for cercle in self.list_cercle:
            arcade.draw_circle_filled(cercle[0], cercle[1], cercle[2], cercle[3])
        for rectangle in self.liste_rectangle:
            rectangle.draw()
        arcade.finish_render()

def main():
   my_game = MyGame()
   my_game.setup()
   
   
   arcade.run()


main()


