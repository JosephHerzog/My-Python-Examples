"""'Tetris' ship types for the Battleship game.

   Author: Russ Lewis

   Defines a series of functions, producing ships which are shaped like
   the classic pieces from Tetris.  In all cases, (0,0) is included as
   one of the points in the set.

   As with the standard ship functions, these all accept a 'rot'
   parameter, which is used to rotate the ship as it is being created.

   Primary functions:
      Tee     (rot)
      R_ZigZag(rot)
      L_ZigZag(rot)
      L_Boot  (rot)
      R_Boot  (rot)
      Square  (rot)
      Bar     (rot)
"""



from battleship     import Ship



def Tee(rot):
    """Tetris Ship 'Tee'
       .
       .        T
       Shape: T T T
    """

    retval = Ship("Tee", [(0,0), (1,0), (0,1), (-1,0)] )
    retval.rotate(rot)
    return retval

def R_ZigZag(rot):
    """Tetris Ship 'Right ZigZag'
       .
       .        R
       .      R R
       Shape: R
    """

    retval = Ship("R Zig-Zag", [(0,0), (0,1), (1,1), (1,2)] )
    retval.rotate(rot)
    return retval

def L_ZigZag(rot):
    """Tetris Ship 'Left ZigZag'
       .
       .      L
       .      L L
       Shape:   L
    """

    retval = Ship("L Zig-Zag", [(0,0), (0,1), (-1,1), (-1,2)] )
    retval.rotate(rot)
    return retval

def L_Boot(rot):
    """Tetris Ship 'Left Boot'
       .
       .      L
       .      L
       Shape: L L
    """

    retval = Ship("L Boot", [(0,0), (1,0), (0,1), (0,2)] )
    retval.rotate(rot)
    return retval

def R_Boot(rot):
    """Tetris Ship 'Right Boot'
       .
       .        R
       .        R
       Shape: R R
    """

    retval = Ship("R Boot", [(0,0), (-1,0), (0,1), (0,2)] )
    retval.rotate(rot)
    return retval

def Square(rot):
    """Tetris Ship 'Square'
       .
       .      S S
       Shape: S S
    """

    retval = Ship("Square", [(0,0), (1,0), (0,1), (1,1)] )
    retval.rotate(rot)
    return retval

def Bar(rot):
    """Tetris Ship 'Bar'
       .
       Shape: B B B B
    """

    retval = Ship("Bar", [(0,0), (1,0), (2,0), (3,0)] )
    retval.rotate(rot)
    return retval


