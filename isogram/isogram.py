def is_isogram(string):
    for i in string:
        if string.lower().count(i) > 1 and i not in [' ', '-']:
            return False

    return True
