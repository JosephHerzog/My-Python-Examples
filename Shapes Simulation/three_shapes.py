# Write your code here :-)
from three_shapes_game import *
import random

class Circle:
    """ self.size refers to the width, or full size, of the ball.
    """
    def __init__(self, game_width, game_height):
        self.size = random.randint(50,100)
        self.x = random.randint(0+self.size,game_width-self.size)
        self.y = random.randint(0+self.size,game_height-self.size-100)
        self.x_velocity = random.randint(0,10)
        self.y_velocity = 0
        self.accel = 0.5
        self.rgb = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        # define if ball is moving left (-1) or right (1)
        temp = random.random()
        if temp < 0.5:
            self.direction = -1
        else:
            self.direction = 1

    def __str__(self):
        return "Circle"

    def get_xy(self):
        return ( self.x , self.y )

    def get_radius(self):
        return self.size//2

    def nearby(self, other, dist, game):
        if str(other) == "Square":
            if dist < self.size+50:
                game.remove_obj(self)

    def edge(self, edge, position):
        if edge == "top" or edge == "bottom":
            self.y_velocity = -(self.y_velocity)
        elif edge == "left" or edge == "right":
            self.x_velocity = -self.x_velocity

    def move(self, game):
        t = 1
        self.y = self.y + self.y_velocity*t + 0.5*((self.accel)**2)
        self.x = self.x + self.x_velocity*t
        self.y_velocity = self.y_velocity + self.accel*t

    def draw(self, win):
        color = win.get_color_string(self.rgb[0],self.rgb[1],self.rgb[2])
        win.ellipse(self.x,self.y,self.size,self.size,color)

class Triangle:
    def __init__(self, game_width, game_height):
        self.size = random.randint(50,100)
        self.x = random.randint(0+self.size,game_width-self.size)
        self.y = random.randint(0+self.size,game_height-self.size)
        self.wid = game_width
        self.hei = game_height

    def __str__(self):
        return "Triangle"

    def get_xy(self):
        return ( self.x , self.y )

    def get_radius(self):
        return self.size//2

    def nearby(self, other, dist, game):
        # Triangles should not be close to each other
        if str(self) == str(other):
            if dist < 20:
                self.move(self)
        if str(other) == "Circle":
            if dist < other.size+50:
                game.remove_obj(self)

    def edge(self, edge, position):
        self.x = random.randint(0+self.size,self.wid-self.size)
        self.y = random.randint(0+self.size,self.hei-self.size)

    def move(self, game):
        self.x, self.y = self.x+random.randint(-3,3), self.y+random.randint(-10,10)

    def draw(self, win):
        win.triangle(self.x,self.y+20,self.x+15,self.y-10,self.x-15,self.y-10,"red")

class Square:
    def __init__(self,game_width,game_height):
        self.size = random.randint(20,80)
        self.x = random.randint(0+self.size,game_width-self.size)
        self.y = random.randint(0+self.size,game_height-self.size-100)
        self.x_velocity = random.randint(0,10)
        self.y_velocity = random.randint(0,10)
        self.accel = 0
        # define if ball is moving left (-1) or right (1)
        temp = random.random()
        if temp < 0.5:
            self.direction = -1
        else:
            self.direction = 1

    def get_xy(self):
        return ( self.x , self.y )

    def get_radius(self):
        return self.size//2

    def __str__(self):
        return "Square"

    def nearby(self, other, dist, game):
        if str(other) == "Triangle":
            if dist < self.size:
                game.remove_obj(self)

    def edge(self, edge, position):
        if edge == "top" or edge == "bottom":
            self.y_velocity = -(self.y_velocity)
        elif edge == "left" or edge == "right":
            self.x_velocity = -self.x_velocity

    def move(self, game):
        t = 1
        self.y = self.y + self.y_velocity*t + 0.5*((self.accel)**2)
        self.x = self.x + self.x_velocity*t
        self.y_velocity = self.y_velocity + self.accel*t
    def draw(self, win):
        color = win.get_color_string(50,50,50)
        win.rectangle(self.x,self.y,self.size//2,self.size//2,color)


def spawn(game, wid, hei):
    for i in range(random.randint(5,10)):
        new_circle = Circle(wid,hei)
        game.add_obj(new_circle)
    for i in range(random.randint(5,10)):
        new_triangle = Triangle(wid,hei)
        game.add_obj(new_triangle)
    for i in range(random.randint(5,10)):
        new_square = Square(wid,hei)
        game.add_obj(new_square)

def spawn_more(game, wid, hei):
    if random.random() < 0.05:
        spawn(game, wid, hei)

def main():
    # This is the size of the window; feel free to tweak it. However,
    # please don’t make this gigantic (about 800x800 should be max),
    # since your TA may not have a screen with crazy-large resolution.
    wid = 400
    hei = 600

    # This creates the Game object. The first param is the window name;
    # the second is the framerate you want (20 frames per second, in this# example); the last two are the window / game space size.
    game = Game("Three Shapes", 60, wid,hei)

    # This affects how the distance calculation in the "nearby" calls
    # works; the default is to measure center-to-center. But if anybody
    # wants to measure edge-to-edge, they can turn on this feature.
        # game.config_set("account_for_radii_in_dist", True)
    # You get to decide what spawn() does. This sets up the initial
    # objects that you want to create, at the beginning of the game (if
    # any). Of course, you can remove this is you want to create objects
    # some other way.
    spawn(game, wid,hei)

    # game loop. Runs forever, unless the game ends.
    while not game.is_over():
        game.do_nearby_calls()
        game.do_move_calls()
        game.do_edge_calls()
        game.draw()

        # You get to decide what spawn_more() does (if anything). This
        # allows you to spawn additional objects over time. It is
        # called once per game tick.
        spawn_more(game, wid,hei)

main()
