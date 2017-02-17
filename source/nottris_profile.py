

import bag, piece, field, pieceOcc, rotData, stopwatch, lvl2time
import datetime, time, sys
import pygame
from pygame.locals import *

import cProfile

class Game:
    def __init__(self, cSpeed=0, cHeight=0, cMusic='a', ):
        self.speed = self.startSpeed = cSpeed # 0-9
        self.startHeight = cHeight # 0-5
        self.score = 0
        self.bag = bag.bag(7)
        self.lines = 0
        self.timer = stopwatch.Stopwatch()
        self.pause = False
        
        # generate height garbage

        self.field = field.Field()

        # populate blocks
        self.currPiece = piece.Piece(self.bag.grab())
        self.nextPiece = piece.Piece(self.bag.grab())

        
    def newPiece(self):
        """ Rotates next piece to current piece, makes new next piece. """
        self.currPiece, self.nextPiece = self.nextPiece, piece.Piece(self.bag.grab())
        if self.currPiece.type == 5:
            self.currPiece.pos[0] -= 1
        if pieceOcc.pieceOcc(self.currPiece, self.field):
            return True
        else:
            return False

            
    def clearLines(self, incoming):
        """ Clears full lines and increments score. """
        self.score += incoming[0]
        self.lines += incoming[1]

        
    def recieve(self, score):
        """ Recieves soft-drop bonus. """
        self.score += score
        
      
    def render(self, bg=False, blocks=True, piece=True, time=True, score=False, lines=False, next=False, intro=False):
        """ Render the damn board. """

        if bg:
            # redraw the pretty background
            self.screen.blit(self.resources.field, (0,0))


        if blocks or piece:
            # clear field area field area
            #self.screen.fill((0,0,0), pygame.Rect(375,56,320,640))
            self.screen.fill((0,0,0), pygame.Rect(342,47,320,640))

        if blocks:
            #render the dead blocks
            for line in range(2, 22):
                for block in range(10):
                    blockType = self.field.data[line][block]
                    if blockType > -1: # block isn't empty
                        self.screen.blit(self.resources.blocks[blockType], (32 * block + 342, 32 * line - 17))

        # this function could be updated by using the data() function
        if piece:
            # render the current piece
            temp = self.currPiece
            data = (temp.pos, rotData.rotData[temp.type][temp.rot])
    
            for y in range(4):
                for x in range(4):
                    if data[1][y][x]:
                        if data[0][0] + y > 1:
                            # y, x = 0, 1   just a handy way to reference the offsets
                            self.screen.blit(self.resources.blocks[temp.type], (32 * (data[0][1] + x) + 342, 32 * (data[0][0] + y) - 17 ))

        if time:
            # render the time
            self.screen.fill((0,0,0), pygame.Rect(66,263,180,50))
            self.screen.blit(self.resources.font.render(self.timer.check().__str__().split('.')[0], True, (255,255,255), (0,0,0)), (69,270))

        if score:
            # render the score
            self.screen.fill((0,0,0), pygame.Rect(72,425,190,40))
            self.screen.blit(self.resources.font.render(self.score.__str__(), True, (255,255,255), (0,0,0)), (75,430))

        if lines:
            # render the line count
            self.screen.fill((0,0,0), pygame.Rect(76,106,137,47))
            self.screen.blit(self.resources.font.render(self.lines.__str__(), True, (255,255,255), (0,0,0)), (76,106))

        if next:
            # display the next block
            self.screen.fill((0,0,0), pygame.Rect(92,583,128,128)) # clear location
            nextPieceData = self.nextPiece.data()
            nextPieceColor = self.nextPiece.type
            for y in range(4):
                for x in range(4):
                    if nextPieceData[y][x]:
                        self.screen.blit(self.resources.blocks[nextPieceColor], (92 + 32 * x, 583 + 32 * y))

        if intro:
            # show controls
            self.screen.blit(self.resources.controls, (0,0))

        pygame.display.flip()
   
    
    def play(self):
        """ Actually play the game. """
        print "pygame initializing...",
        pygame.init()
        print "done"
        
        self.screen = pygame.display.set_mode((750, 750))
        pygame.display.set_caption("Kyle's Nottris")
        # load resources
        class Resources:
            pass
        print "image loading..."
        self.resources = Resources()
        print " instructions...",
        self.resources.controls = pygame.image.load('images/instructions.png').convert()
        print "done"
        self.resources.blocks = []
        print " blocks...",
        self.resources.blocks.append(pygame.image.load('images/t.png').convert())
        print "t,",
        self.resources.blocks.append(pygame.image.load('images/l.png').convert())
        print "l,",
        self.resources.blocks.append(pygame.image.load('images/j.png').convert())
        print "j,",
        self.resources.blocks.append(pygame.image.load('images/s.png').convert())
        print "s,",
        self.resources.blocks.append(pygame.image.load('images/z.png').convert())
        print "z,",
        self.resources.blocks.append(pygame.image.load('images/i.png').convert())
        print "i,",
        self.resources.blocks.append(pygame.image.load('images/o.png').convert())
        print "o"

        print " loading field...",
        self.resources.field = pygame.image.load('images/field.png').convert()
        print "done"
        print "loading font...",
        self.resources.font = pygame.font.get_default_font()
        self.resources.font = pygame.font.Font(self.resources.font, 28)
        print "done"

        print "loading complete"
        counter = stopwatch.Stopwatch()

        # show controls and wait for enter
        self.render(bg=False, blocks=False, piece=False, time=False, score=False, lines=False, next=False, intro=True)
        while True:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    break
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        dirty = True
        self.timer.start()

        while self.newPiece(): # possible to spawn a new block (and do it)
            self.render(bg=True, score=True, lines=True, next=True)
            while self.currPiece.goDrop(self.field):
                drop = False
                dropTime = lvl2time.lvl2time(self.speed)
                counter.start()
                while counter.check() < dropTime:
                    pygame.time.wait(5) # share the processor
                    # event handling
                    event = pygame.event.poll()
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                            self.currPiece.goLeft(self.field)
                            dirty = True
                        if event.key == K_RIGHT:
                            self.currPiece.goRight(self.field)
                            dirty = True
                        if event.key == K_z or event.key == K_UP:
                            self.currPiece.goRotCW(self.field)
                            dirty = True
                        if event.key == K_x:
                            self.currPiece.goRotCCW(self.field)
                            dirty = True
                    if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                    if dirty:
                        self.render()
                        dirty = False

                    # soft drop
                    keys = pygame.key.get_pressed()
                    if keys[K_DOWN]:
                        drop = True
                    if drop: # and counter.check() > datetime.timedelta(seconds=.05):
                        pygame.time.wait(5)
                        self.currPiece.score += 1
                        break

                self.render()

            self.recieve(self.field.addPiece(self.currPiece))
            self.clearLines(self.field.clearLines(self.speed))
            #self.speed += 1
            if self.lines > self.speed * 10 - 1: # every ten lines gives speed lvl-up
                self.speed += 1


if __name__ == "__main__":

    main = Game()
    cProfile.run('main.play()')
