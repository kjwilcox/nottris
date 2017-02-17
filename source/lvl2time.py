
import datetime
def lvl2time(level):
    """ Uses an algebraic fomula to derive a deltatime from a level. """
    #return (level^2 + 1)
    if level > 20:
        return datetime.timedelta(seconds=.1)
    return datetime.timedelta(seconds=(-.02*level)+.5)
