from slow_print import slow_print

numberOfBottles = 99

def take_one_down(bottleCount = 0):
    """
    Handles the verse structure for the song and tries hard to have the correct grammar.
    """
    if bottleCount > 1:
        verseFormat = f"""
        {bottleCount} bottles of glass on the wall!
        {bottleCount} bottles of glass!
        If one of them bottles should happen to fall:
        {bottleCount - 1} bottles of glass on the wall.
        """
    else:
        verseFormat = f"""
        {bottleCount} bottle of glass on the wall!
        {bottleCount} bottle of glass!
        If that dang bottle should happen to fall:
        {bottleCount - 1} bottles of glass on the wall.
        """
    return verseFormat

if __name__ == "__main__":
    while numberOfBottles > 0:
        slow_print(take_one_down(numberOfBottles))
        numberOfBottles -= 1
