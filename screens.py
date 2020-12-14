textbutton _("Patch Notes") action ShowMenu("patch_notes")

text _("-----------------------------------------------------------------------")
            text _("(Made by Erik Johansson for Programming 1.)")

screen patch_notes():

    tag menu

    use game_menu(_("Patch Notes"), scroll="viewport"):

        has vbox:
            spacing 20
        text _("{b}Patch 1.4a:{/b} Bug fixes")

        text _("{b}Patch 1.3b:{/b} Added the final ending")

        text _("{b}Patch 1.3a:{/b} Added a good ending")

        text _("{b}Patch 1.2c:{/b} Added the cave and a inabitant of such cave")

        text _("{b}Patch 1.2b:{/b} Added the tent and a new bad ending along one of the paths")

        text _("{b}Patch 1.2a:{/b} Added the road to the circus, the random hobo, the clown and the hobos alterego ")

        text _("{b}Patch 1.1e:{/b} Added more dialogue a new bad ending, a new 'fancy' background and more info in the about page.")

        text _("{b}Patch 1.1d:{/b} Added patch notes screen, changed the window icon and a mysterious figure.")

        text _("{b}Patch 1.1c:{/b} Added a bad ending, rika's mother and changed the name of preferences too settings.")

        text _("{b}Patch 1.1b:{/b} Changed the main menu and pause screen background and added nice textboxes, the narrator and dialogue.")

        text _("{b}Patch 1.1a:{/b} Added Rika, Santa, two backgrounds and test dialogue ")