image nar icon1 = "Narrator.png"
image Rika icon1 = "Rika_Transparent.png"
image Santa icon1 = "Jultomten_Transparent.png"
image Tree = "Tree.png"
image house = "real house.png"
define audio.boo = "audio/Happy.mp3"

define n = Character("Narrator",color="#FF7B00")
define r = Character("Rika", color="#00f9e5")
define s = Character("Santa", color="#deea00")

label start:

    scene house
    show nar icon1 at left
    n "Here is the house where our unknowing hero story will begin."
    n "Our unlikely hero’s name is Rika Martinez with you as her conscience what could go wrong."
    with fade

    scene Tree

    play music boo
    show Rika icon1 at center with fade

    with fade
    show Santa icon1 at left

    r "I wish Santa was here"

    s "Have you been naughty or nice?"

    menu:
        "Nice":
            jump Nice

        "No":
            jump No

    label Nice:
        r "Nice, Santa always."

        s "Good girl, keep at it."

        ".:. Good ending."
        return

    label No:
        r "NO!"

        s "So you have been a naughty girl, That means I am going to have to spank."

        ".:. Bad ending"
        return
