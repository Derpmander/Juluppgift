textbutton _("Patch Notes") action ShowMenu("patch_notes")

text _("-----------------------------------------------------------------------")
            text _("(Made by Erik Johansson for Programming 1.)")

screen patch_notes():

    tag menu

    use game_menu(_("Patch Notes"), scroll="viewport"):

        has vbox:
            spacing 20
