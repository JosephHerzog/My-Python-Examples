# Write your code here :-)
from three_shapes_game import *
import random

class Bacteria:
    def __init__(self, wid, hei):
        self.size = random.randint(20,30)
        self.x = random.randint(0+self.size+10,wid-self.size-10)
        self.y = random.randint(0+self.size+10,hei-self.size-10)
        self.x_velocity = random.randint(-5,5)
        self.y_velocity = random.randint(-5,5)
        self.accel = 0

        colors = ['forestgreen','limegreen','darkgreen','green','lime','seagreen','springgreen','turquoise','aqua','cyan']
        temp = random.randint(0,len(colors)-1)
        self.color = colors[temp]

    def __str__(self):
        return "Bacteria"
    def get_xy(self):
        return ( self.x, self.y )

    def get_radius(self):
        return (self.size+self.size)//4



    def nearby(self, other, dist, game):
        if str(other) == "Bacteria":
            if dist < (self.size+other.size)//2:
                if self.size >= other.size:
                    self.size += other.size//2
                    game.remove_obj(other)
                else:
                    other.size += self.size//2
                    game.remove_obj(self)




    def edge(self, edge, position):
        if edge == "top" or edge == "bottom" or edge == "left" or edge == "right":
            self.y_velocity = 0
            self.x_velocity = 0



    def move(self, game):
        t = 1
        self.y = self.y + self.y_velocity*t + 0.5*((self.accel)**2)
        self.x = self.x + self.x_velocity*t
        self.y_velocity = self.y_velocity + self.accel*t



    def draw(self, win):
        win.ellipse(self.x, self.y, self.size//2, self.size//2, self.color)

class Poison:
    def __init__(self, wid, hei):
        self.wid = wid
        self.hei = hei
        self.radius = 5
        self.x = random.randint(0+self.radius+10,wid-self.radius-10)
        self.y = random.randint(0+self.radius+10,hei-self.radius-10)

    def get_xy(self):
        return ( self.x , self.y )

    def get_radius(self):
        return self.radius

    def nearby(self, other, dist, game):
        if str(other) == "Bacteria":
            if dist <= (self.radius+other.size)//2:
                game.remove_obj(other)
            elif dist <= other.size-self.radius:
                game.remove_obj(other)

    def edge(self, edge, position):
        self.radius = 6

    def move(self, game):
        if random.random() < 0.005:
            self.x = random.randint(0+self.radius+10,self.wid-self.radius-10)
            self.y = random.randint(0+self.radius+10,self.hei-self.radius-10)

    def draw(self, win):
        win.ellipse(self.x, self.y, self.radius, self.radius, "purple")


def spawn(game, wid, hei):
    for i in range(random.randint(5,10)):
        new_bacteria = Bacteria(wid,hei)
        game.add_obj(new_bacteria)
    for i in range(random.randint(5,10)):
        new_poison = Poison(wid,hei)
        game.add_obj(new_poison)

def spawn_more(game, wid, hei):
    if random.random()*100 < 20: # percent chance of spawning per tick
        for i in range(random.randint(0,3)):
            new_bacteria = Bacteria(wid,hei)
            game.add_obj(new_bacteria)

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
