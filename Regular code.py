## Makes images usable in game.
image nar icon1 = "Narrator.png"
image nar icon2 = "Narrator_closed_mouth.png"
image nar icon3 = "Narrator_embaressed.png"
image Rika icon1 = "Rika.png"
image Santa icon1 = "Jultomten_Transparent.png"
image mo icon1 = "Gertrude.png"
image 1 icon1 = "1.png"
image inside = "Inside.png"
image dead = "Dead_rika.png"
image house = "real house.png"
define audio.boo = "audio/Happy.mp3"

##Defines letter into characters
define n = Character("Narrator",color="#000000")
define r = Character("Rika", color="#000000")
define s = Character("Santa", color="#000000")
define g = Character("Mother", color="#000000")
define a = Character("???", color="#FF0004")

label start:
    play music boo
    scene house
    with fade
    show nar icon1 at left
    with dissolve
    n "Here is the house where our unknowing hero's story will begin."
    show nar icon2 at left
    n "(In brain) What was I going to say, OH RIGHT."
    show nar icon1 at left
    n "Our unlikely hero’s name is Rika Martinez with you as her conscience what could go wrong."
    show nar icon2 at left

    scene inside
    with fade
    show Rika icon1 at center
    with dissolve
    r "I want presents, presents, presents, presents!!"

    show nar icon1 at left
    with dissolve
    n "It seems our hero is being a little brat."
    n "I am going to have to break the 4th wall in for a second."
    n "RIKA, LISTEN YOU LITTLE BRAT!"
    n "YOU WILL NEVER GET PRESENTS LIKE THIS!!!"
    r "MOM!!, I hear voices in my head again."

    show mo icon1 at right
    with dissolve
    g "SHUT UP OR I WON'T TAKE YOUR ANNOYANCE ANYMORE!!"
    hide mo icon1
    with dissolve
    n "As you can see Rika gets bullied at home."
    n "And her father disapered"
    r "SHUT UP HEAD"
    show 1 icon1 at right
    with dissolve
    a "Yes, shut up head"
    n "Who are you?"
    a "You do not need to worry about me....yet"
    hide 1 icon1
    with dissolve
    n "Rika, if you are nice santa will give you presents."
    n "Yes or No?"

    menu:
        "yes":
            jump yes

        "No":
            jump NO

    label yes:
        r "Yes, I will be nice"
        n "Good girl, Santa won't hurt you for now then"
        r "Wait what?!"
        n "Nothing"
        n "Or do you want know"
        menu:
            "Sure":
                jump sure

            "Nope":
                jump nope


        label sure:
            r "Sure tell me"
            n "Everytime Santa finds that you did something bad you will die"
            r "So I am dead"
            show Santa icon1 at right
            with dissolve
            s "Yes VERY"

            scene dead with fade
            ".:. Bad Ending(2/2)"
            return

        label nope:
            r "Nope don't wanna know"
            n "Wise decision young one"
            return

    label NO:
        r "NO, I won't be nice"
        n "So you have choosen death. SANTA!!!"
        show Santa icon1 at right
        with dissolve
        s "You will die now little girl."
        scene dead with fade
        ".:. Bad ending(1/2)"
        return