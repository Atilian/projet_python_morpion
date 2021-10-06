#!/usr/bin/python3


class Joueur:

    def __init__(self, Pseudo, Token):

        self.Pseudo = Pseudo
        self.Token = Token


def WinMorpion(listXO):
    """
    Check colomne, row and axe

    Arrgs:
        List(Game board)

    Return:
        Win:
            "O" / "X"
        None:
            "."
    """

    choices = ["O", "X"]

    for OX in choices:

        # Colomne LEFT
        if (listXO[0] == OX and listXO[3] == OX and listXO[6] == OX):
            return OX
        # Colomne RIGHT
        if (listXO[2] == OX and listXO[5] == OX and listXO[8] == OX):
            return OX

        # Row TOP
        if (listXO[0] == OX and listXO[1] == OX and listXO[2] == OX):
            return OX
        # Row MID
        if (listXO[3] == OX and listXO[4] == OX and listXO[5] == OX):
            return OX
        # Row BOT
        if (listXO[6] == OX and listXO[7] == OX and listXO[8] == OX):
            return OX

        # Axe LEFT
        if (listXO[0] == OX and listXO[4] == OX and listXO[8] == OX):
            return OX
        # Axe RIGHT
        if (listXO[2] == OX and listXO[4] == OX and listXO[6] == OX):
            return OX

    return "."


def DisplayPlateau(listXO):

    print("\n %s | %s | %s \n"
          "---|---|---\n"
          " %s | %s | %s \n"
          "---|---|---\n"
          " %s | %s | %s " % (listXO[0], listXO[1], listXO[2], listXO[3], listXO[4], listXO[5], listXO[6], listXO[7], listXO[8]))


def EmptyBoard(listXO):

    for index in listXO:

        if (index != "O" and index != "X"):
            
            return True
    
    return False


def main():

    while True:

        print("*********")
        print("*Morpion*")
        print("*********\n")

        NameJ1 = (input("Pseudo Joueur 1 : "))
        NameJ2 = input("\nPseudo Joueur 2 : ")

        print("\n%s aura les ronds (O)" % (NameJ1))
        print("%s aura les croix (X)" % (NameJ2))

        J1 = Joueur(NameJ1, "O")
        J2 = Joueur(NameJ2, "X")

        print("\nChaqu'un votre tour vous devrez donner l'index de la case que vous voulez exemple ci-dessous\n\n")

        listXO = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        DisplayPlateau(listXO)

        listJoueurs = [J1, J2]

        win = False

        while True:

            for J in listJoueurs:

                if (EmptyBoard(listXO) == True):

                    while True:

                        choice = int(
                            input("\n%s veuillez choisir un indice : " % (J.Pseudo)))

                        if (listXO[choice - 1] != "O" and listXO[choice - 1] != "X"):

                            listXO[choice - 1] = J.Token
                            break

                        else:

                            print("Index deja pris")

                else:

                    print("\nMatch null\n")
                    break

                if (WinMorpion(listXO) == J.Token):

                    print("Bravo %s vous avez gagner !" % (J.Pseudo))
                    win = True
                    break

                DisplayPlateau(listXO)

            if (win == True or EmptyBoard(listXO) == False):
                break

        replay = input("Replay Y/N : ")

        if (replay.upper() == "N"):
            break


main()
