image Rika icon1 = "Rika_Transparent.png"
image Santa icon1 = "Jultomten_Transparent.jpg"
image Tree = "Tree.png"

define audio.boo = "audio/Happy.mp3"


define r = Character("Rika", color="#00f9e5")

define s = Character("Santa", color="#deea00")


label start:

    scene Tree

    play music boo

    show Rika icon1 at center

    show Santa icon1 at left


    r "REEEEEE"

    s "Have you been naughty or nice?"

    return
