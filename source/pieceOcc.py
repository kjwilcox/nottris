
import piece
import field

def pieceOcc(piece, field):
    """ Returns whether or not a piece can occupy the given space. """

    y, x = 0, 1 # just a handy way to reference the offsets

    pData = piece.data()
    fData = field.data

    for j in range(4): # y coord
        for i in range(4): # x coord
            if (piece.pos[x] + i) in range(10) and (piece.pos[y] + j) in range(22): # field part in range
                if pData[j][i] and (fData[piece.pos[y] + j][piece.pos[x] + i] > -1):
                    return False # blocks overlap, collide
            else: # field out of range
                if pData[j][i]:
                    return False # block is on out of range, collide

    return True # piece fits
