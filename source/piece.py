# done, not extensively tested.

import rotData
import pieceOcc
import copy

class Piece:
    """ A falling nottris piece. """

    
    def __init__(self, cType, cRot=0, cPos=[1,3]):
        self.type = cType
        self.rot = cRot
        if self.rot > 3:
            self.rot = 0
        if self.rot < 0:
            self.rot = 3
        self.pos = copy.deepcopy(cPos)

        self.alive = True
        self.score = 0 # Extra points block will grant, due to soft drops.


    def canLeft(self, fLoc):
        """ Returns ability of block to move left. """
        return pieceOcc.pieceOcc(Piece(self.type, self.rot, [self.pos[0], self.pos[1] - 1]), fLoc)
    def canRight(self, fLoc):
        """ Returns ability of block to move right. """
        return pieceOcc.pieceOcc(Piece(self.type, self.rot, [self.pos[0], self.pos[1] + 1]), fLoc)
    def canDrop(self, fLoc):
        """ Returns ability of block to move down. """
        return pieceOcc.pieceOcc(Piece(self.type, self.rot, [self.pos[0] + 1, self.pos[1]]), fLoc)
    def canRotCW(self, fLoc):
        """ Returns ability of block to rotate clockwise. """
        return pieceOcc.pieceOcc(Piece(self.type, self.rot + 1, self.pos), fLoc)
    def canRotCCW(self, fLoc):
        """ Returns ability of block to move counter-clockwise. """
        return pieceOcc.pieceOcc(Piece(self.type, self.rot - 1, self.pos), fLoc)


    def goLeft(self, fLoc):
        """ Attempts to move block left. """
        if self.canLeft(fLoc):
            self.pos = [self.pos[0], self.pos[1] - 1]
            return True
        return False
    def goRight(self, fLoc):
        """ Attempts to move block right. """
        if self.canRight(fLoc):
            self.pos = [self.pos[0], self.pos[1] + 1]
            return True
        return False
    def goDrop(self, fLoc):
        """ Attempts to move block down. """
        if self.canDrop(fLoc):
            self.pos = [self.pos[0] + 1, self.pos[1]]
            return True
        return False
    def goRotCW(self, fLoc):
        """ Attempts to rotate block clockwise. """
        if self.canRotCW(fLoc):
            self.rot += 1
            if self.rot > 3:
                self.rot = 0
            return True
        return False
    def goRotCCW(self, fLoc):
        """ Attempts to move block counter-clockwise. """
        if self.canRotCW(fLoc):
            self.rot -= 1
            if self.rot < 0:
                self.rot = 3
            return True
        return False


    def data(self):
        """ Returns the 4x4 grid of the actual piece data. """
        global rotData
        return rotData.rotData[self.type][self.rot]
    
