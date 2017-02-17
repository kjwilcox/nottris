import copy

class Field:
    """ The field containing the fallen pieces. """

    
    def __init__(self, cData=[[-1 for i in range(10)] for i in range(22)]):
        # changed default value of cData from [[False]*10]*22 to the current
        # this caused a terrible bug. i promise to be super-careful with
        # python's shallow copying tendancy
        self.data = copy.deepcopy(cData) # this got me good


    def addPiece(self, piece):
        """ Adds the piece provided into the field array. """
        
        pData = piece.data() # the 4x4 grid of block data
        y, x = 0, 1 # just a handy way to reference the offsets
        
        for j in range(4): # vertical
            for i in range(4): # horizontal

                if ((piece.pos[y] + j) in range(22)) and ((piece.pos[x] + i) in range(10)): # piece in range
                    
                    #if (self.data[piece.pos[y] + j][piece.pos[x] + i] > -1): # field sector is already occumpied
                    #    pass # leave sector alone

                    if pData[j][i]: # field sector is empty
                        self.data[piece.pos[y] + j][piece.pos[x] + i] = piece.type # add color block

                else: # piece out of range
                    if (pData[j][i] == True): # block sector filled
                        print "error: tried to add a block outside field bounds."
                    else:
                        pass # no problems

        return piece.score


    def clearLines(self, level=0):
        """ Clears full lines and returns the score and lines. """
        score = 0
        fullLines = []

        for line in range(22):
            empty = 0
            for sector in self.data[line]:
                if sector < 0: # if the block is empty
                    empty += 1
            if empty == 0: # no empties, line is full
                fullLines.append(line)


        # the magic formula!
        numLines = len(fullLines)
        
        if numLines == 1:
            score = 40 * (level + 1)
        elif numLines == 2:
            score = 100 * (level + 1)
        elif numLines == 3:
            score = 300 * (level + 1)
        elif numLines == 4:
            score = 1200 * (level + 1)
        elif numLines > 4:
            print "this must be an error, can't clear more than 4 lines"

        for line in fullLines:
            del self.data[line] # clear the line
            self.data.insert(0, [-1]*10) # add a new line on top

        return (score, numLines)
                
