""" File: battleship.py
    Author: Joseph Herzog
    Course: CSC 120
    Purpose: This file provides 2 classes for the interactive.py file,
             which are Board() and Ship() to represent the board and ships
             of the battleship game.
"""
class Board:
    """ This class represents one side of the board of a battleship game.
        The constructor builds an empty board, and the data of hits, shots,
        and sinks are stored in their own arrays.

        Methods:
        add_ship()
        print()
        has_been_used()
        attempt_move()
    """
    def __init__(self, size):
        assert type(size) == int
        assert size > 0
        self._size = int(size)
        self._shots = []
        self._hits = []
        self._sunk_squares = []
        self._ship_squares = []
        self._ships = []

    def add_ship(self, ship, position):
        """ This function adds a ship to the board at any position
            Arguments: Ship - the shape of the ship, stored as a
                              list of tuple coordinates
                       Position - x,y tuple of the reference point

            Note: The ship rotate method is called before the ship is
                  added to the board.
        """
        x_bounds = [0,0]
        y_bounds = [0,0]

        # get actual positions of the ship on the board
        new_squares= []

        for pos in ship._squares:
            pos = (pos[0]+position[0], pos[1]+position[1])
            new_squares.append(pos)
            ship._squares = new_squares

        # check to ensure that the ship will
        # reside in the square
        for coord in ship._squares:
            if coord[0] > x_bounds[1]:
                x_bounds[1] = coord[0]
            elif coord[0] < x_bounds[1]:
                x_bounds[0] = coord[0]
            if coord[1] > y_bounds[1]:
                y_bounds[1] = coord[0]
            elif coord[1] < y_bounds[1]:
                y_bounds[0] = coord[0]

        for bound in x_bounds:
            assert bound < self._size and bound >= 0
        for bound in y_bounds:
            assert bound < self._size and bound >= 0

        # check to ensure that the ship does not
        # overlap any other ships.
        for square in ship._squares:
            assert square not in self._ship_squares

        # sanity checks complete, add the ship
        self._ships.append(ship)
        for square in ship._squares:
            self._ship_squares.append(square)

    def print(self):
        """ Print the current state of the board. Sunk ships
            will appear as just X's, and hits are marked as *'s.
            Misses are marked as O's.
        """


        print("   +" + "-" * (self._size*2+1) + "+")

        for i in reversed(range(self._size)):
            if i >= 10:
                print(str(i) + " |", end="")
            else:
                print(" " + str(i) + " |", end="")
            for j in range(self._size):
                print(" ", end="")
                point = (j,i)
                if point in self._sunk_squares:
                    print("X", end="")
                elif point in self._hits:
                    print("*", end="")
                elif point in self._ship_squares:
                    for ship in self._ships:
                        if point in ship._squares:
                            print(ship._name[0],end="")
                            break
                elif point in self._shots:
                    print("o", end="")
                else:
                    print(".", end="")
            print(" |")
        print("   +" + "-" * (self._size*2+1) + "+")

        if self._size>10:
            print(" " * 5, end="")
            for i in range(self._size):
                if i / 10 >= 1:
                    print(str(i // 10) + " ", end="")
                else:
                    print("  ",end="")
            print()

        print(" " * 5, end="")
        for i in range(self._size):
            print(str(i%10) + " ", end="")
        print()

    def has_been_used(self, position):
        if position in self._shots:
            return True
        return False

    def attempt_move(self, position):
        """ This function will attempt a shot by a player. It checks to
            ensure that the shot is on the board dimensions, and then
            adds the shot to the history of shots.
            Arguments: position - the x,y tuple location of the shot
            Returns: A string of the result of the hit. (Sunk, Hit, Miss)
        """
        # ensure that the shot lies within the board and hasn't been used before
        assert position[0] <= self._size
        assert position[1] <= self._size
        assert self.has_been_used(position) == False

        self._shots.append(position)

        if position in self._ship_squares:
            for ship in self._ships:
                if position in ship._squares:
                    ship._hits.append(position)
                    self._hits.append(position)
                    if ship.is_sunk():
                        self._sunk_squares += ship._squares
                        return str("Sunk (" + ship._name +")")
            return "Hit"
        return "Miss"



class Ship:
    """ This class represents
    """
    def __init__(self, name, shape):
        """ shape is the shape of the ship, stored as a
            list of tuple coordinates
        """
        self._hits = []
        self._name = name
        self._squares = shape

    def print(self):
        """ Prints out a single line of output,
            summarizing the state of the ship.
            Example:  AA**AA       Aircraft Carrier
            Note: Sunk ships are notated as all *'s
        """
        for square in self._squares:
            if square in self._hits:
                print("*", end="")
            else:
                print(self._name[0], end="")
        print(" " * (10-len(self._squares)) + self._name)

    def is_sunk(self):
        # return True if sunk, otherwise False
        return len(self._hits) == len(self._squares)

    def rotate(self, amount):
        """ Rotate the ship by creating a new shape array
            for the object Ship. Each coordinate

            Arguments: amount - each 1 meants rotate 90
            degrees clockwise for each amount. 1 = 90, 2 = 180
        """
        new_shape = []
        if amount == 0:
            return
        if amount == 1:
            for square in self._squares:
                new = (square[1], -square[0])
                new_shape.append(new)
        elif amount == 2:
            for square in self._squares:
                new = (-square[0],-square[1])
                new_shape.append(new)
        elif amount == 3:
            for square in self._squares:
                new = (-square[1], square[0])
                new_shape.append(new)

        self._squares = new_shape
