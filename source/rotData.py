# 100% perfection, guaranteed

"""
rotData is a giant boolean array describing the rotation behavior of nottris
blocks. It is accesed like so, where:

blockType = the block type
blockRot = the block rotational position
row = the y coord of desired square
column = the z coord of desired square

rotData[blockType][blockRot][row][column] = value

It was a horrible ordeal converting this from a crappy C array to this one.

- Kyle
"""

rotData = [ 
    # T block
    [ 
        # position 0
        [ 
        [False, False, False, False,], 
        [True,  True,  True,  False,], 
        [False, True,  False, False,], 
        [False, False, False, False,], 
        ], 
        
        # position 1
        [ 
        [False, True,  False, False,], 
        [True,  True,  False, False,], 
        [False, True,  False, False,], 
        [False, False, False, False,], 
        ], 
        
        # position 2
        [ 
        [False, True,  False, False,], 
        [True,  True,  True,  False,], 
        [False, False, False, False,], 
        [False, False, False, False,], 
        ], 
        
        # position 3
        [ 
        [False, True,  False, False,], 
        [False, True,  True,  False,], 
        [False, True,  False, False,], 
        [False, False, False, False,], 
        ], 
    ], 

    # L block
    [ 
        # position 0
        [ 
        [False, False, False, False,], 
        [True,  True,  True,  False,], 
        [True,  False, False, False,], 
        [False, False, False, False,], 
        ], 

        # position 1
        [ 
        [True,  True,  False, False,], 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        [False, False, False, False,], 
        ], 

        # position 2
        [ 
        [False, False, True,  False,], 
        [True,  True,  True,  False,], 
        [False, False, False, False,], 
        [False, False, False, False,], 
        ], 

        # position 3
        [ 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        [False, True,  True,  False,], 
        [False, False, False, False,], 
        ], 
    ], 

    # J block
    [ 
        # position 0
        [ 
        [False, False, False, False,], 
        [True,  True,  True,  False,], 
        [False, False, True,  False,], 
        [False, False, False, False,], 
        ], 

        # position 1
        [ 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        [True,  True,  False, False,], 
        [False, False, False, False,], 
        ], 

        # position 2
        [ 
        [True,  False, False, False,], 
        [True,  True,  True,  False,], 
        [False, False, False, False,], 
        [False, False, False, False,], 
        ], 

        # position 3
        [ 
        [False, True,  True,  False,], 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        [False, False, False, False,], 
        ], 
    ], 
    
    # S block
    [ 
        # position 0
        [ 
        [False, False, False, False,], 
        [False, True,  True,  False,], 
        [True,  True,  False, False,], 
        [False, False, False, False,], 
        ], 

        # position 1
        [ 
        [True,  False, False, False,], 
        [True,  True,  False, False,], 
        [False, True,  False, False,], 
        [False, False, False, False,], 
        ], 

        # position 0
        [ 
        [False, False, False, False,], 
        [False, True,  True,  False,], 
        [True,  True,  False, False,], 
        [False, False, False, False,], 
        ], 

        # position 1
        [ 
        [True,  False, False, False,], 
        [True,  True,  False, False,], 
        [False, True,  False, False,], 
        [False, False, False, False,], 
        ], 
    ], 

    # Z block
    [ 
        # position 0
        [ 
        [False, False, False, False,], 
        [True,  True,  False, False,], 
        [False, True,  True,  False,], 
        [False, False, False, False,], 
        ], 

        # position 1
        [ 
        [False, True,  False, False,], 
        [True,  True,  False, False,], 
        [True,  False, False, False,], 
        [False, False, False, False,], 
        ], 

        # position 0
        [ 
        [False, False, False, False,], 
        [True,  True,  False, False,], 
        [False, True,  True,  False,], 
        [False, False, False, False,], 
        ], 

        # position 1
        [ 
        [False, True,  False, False,], 
        [True,  True,  False, False,], 
        [True,  False, False, False,], 
        [False, False, False, False,], 
        ], 
    ], 
    
    # I block
    [ 
        # position 0
        [ 
        [False, False, False, False,], 
        [False, False, False, False,], 
        [True,  True,  True,  True, ], 
        [False, False, False, False,], 
        ], 

        # position 1
        [ 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        ], 

        # position 0
        [ 
        [False, False, False, False,], 
        [False, False, False, False,], 
        [True,  True,  True,  True, ], 
        [False, False, False, False,], 
        ], 

        # position 1
        [ 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        [False, True,  False, False,], 
        ], 
    ], 

    # O block
    [ 
        # position 0
        [ 
        [False, False, False, False,], 
        [False, True,  True,  False,], 
        [False, True,  True,  False,], 
        [False, False, False, False,], 
        ], 

        # position 0
        [ 
        [False, False, False, False,], 
        [False, True,  True,  False,], 
        [False, True,  True,  False,], 
        [False, False, False, False,], 
        ], 

        # position 0
        [ 
        [False, False, False, False,], 
        [False, True,  True,  False,], 
        [False, True,  True,  False,], 
        [False, False, False, False,], 
        ], 

        # position 0
        [ 
        [False, False, False, False,], 
        [False, True,  True,  False,], 
        [False, True,  True,  False,], 
        [False, False, False, False,], 
        ], 
    ], 
] # phew! :)



