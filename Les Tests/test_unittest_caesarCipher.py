import unittest
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

class TestCaesarCipher(unittest.TestCase):
    def testRotateABy0SameOutputAsInput(self):
        self.assertEqual(rotate("a", 0), "a")

    def testRotateABy1(self):
        self.assertEqual(rotate("a", 1), "b")

    def testRotateMBy13(self):
        self.assertEqual(rotate("m", 13), "z")

    def testRotateNBy13WithWrapAroundAlphabet(self):
        self.assertEqual(rotate("n", 13), "a")

    def testRotateCapitalLetters(self):
        self.assertEqual(rotate("OMG", 5), "TRL")

    def testRotateSpaces(self):
        self.assertEqual(rotate("O M G", 5), "T R L")

    def testRotateNumbers(self):
        self.assertEqual(rotate("Test 1 2 3 test", 4), "Xiwx 1 2 3 xiwx")

    def testRotatePunctuation(self):
        self.assertEqual(rotate("Let's eat, Grandma!", 21), "Gzo'n zvo, Bmviyhv!")

    def testRotateAllLetters(self):
        self.assertEqual(
            rotate("Allo McFly, y'a personne au bout du fil ! Faut réfléchir McFLy !", 13), "Nyyb ZpSyl, l'n crefbaar nh obhg qh svy ! Snhg eésyépuve ZpSYl !"
        )

#--------------------------------------------------------

if __name__ == "__main__":
    unittest.main()