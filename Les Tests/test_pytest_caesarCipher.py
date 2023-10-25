from string import ascii_lowercase, ascii_uppercase

#------------------ Méthodes à tester -------------------

def makeTable(characters, key):
    key %= 26
    return str.maketrans(characters, characters[key:] + characters[:key])

def rotate(text, key):
    table = {**makeTable(ascii_lowercase, key), **makeTable(ascii_uppercase, key)}
    return text.translate(table)

#--------------------------------------------------------

#------------------------ Test --------------------------

def testRotateABy0SameOutputAsInput():
    assert rotate("a", 0) == "a"

def testRotateABy1():
    assert rotate("a", 1) == "b"

def testRotateMBy13():
    assert rotate("m", 13) == "z"

def testRotateNBy13WithWrapAroundAlphabet():
    assert rotate("n", 13) == "a"

def testRotateCapitalLetters():
    assert rotate("OMG", 5) == "TRL"

def testRotateSpaces():
    assert rotate("O M G", 5) == "T R L"

def testRotateNumbers():
    assert rotate("Test 1 2 3 test", 4) == "Xiwx 1 2 3 xiwx"

def testRotatePunctuation():
    assert rotate("Let's eat, Grandma!", 21) == "Gzo'n zvo, Bmviyhv!"

def testRotateAllLetters():
    assert (
        rotate("Allo McFly, y'a personne au bout du fil ! Faut réfléchir McFLy !", 13) == "Nyyb ZpSyl, l'n crefbaar nh obhg qh svy ! Snhg eésyépuve ZpSYl !"
    )

#--------------------------------------------------------