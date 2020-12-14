## Makes images usable in game.
image hobo = "Random_Hobo.png"
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
image road = "Road.png"
image dark = "Black.png"
image tent = "Tent.png"
image percius = "Percius.png"
image Creat = "Cave_c.png"
image clown = "Clown.png"
image dead_mom = "Dead_mom.png"
define audio.music1 = "audio/Jul_spel_musik(1).mp3"

##Defines letter into characters
define n = Character("Narrator",color="#000000")
define r = Character("Rika", color="#000000")
define s = Character("Santa", color="#000000")
define g = Character("Mother", color="#000000")
define a = Character("???", color="#FF0004")
define l = Character("Random Hobo", color="#000000")
define p = Character("Percius", color="#000000")
define c = Character("Clown", color="#000000")
define m = Character("Creature", color="#000000")

label start:
    a "This game contains graphic material and a harsh story line"
    a "Play at your own discretion"
    menu:
        "continue":
            jump continu
    label continu:
        play music music1

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
        n "And her father went out to by a margarita 5 years ago and never returned."
        r "SHUT UP HEAD I ALREADY KNOW MY BACKSTORY"
        n "Rika, if you are nice santa will give you presents."
        n "Yes or No?"

        menu:
            "yes":
                jump nice

            "No":
                jump NO

        label nice:
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
                ".:. Bad Ending(2/6)"
                return

            label nope:
                r "Nope don't wanna know"
                n "Wise decision young one"
                n "I want you to chose if you want to go to the circus"
                n "OR the strange cavern in the mountains"
                n "After that I will leave you for a time"
                menu:
                    "CIRCUS":
                        jump circus

                    "CAVE":
                        jump cave

                label circus:
                    r "I have chosen the CIRCUS"
                    r "Mom, I am going to the circus"
                    g "Stay there when you get there"
                    r "Okay love you bye"

                    scene road with fade

                    show Rika icon1
                    with dissolve

                    r "Why did I choose the circus it's five miles away from home"

                    show hobo at right
                    with dissolve

                    l "AOUH, STOUP COMPlANING LiTtLE GURL"
                    l "YoU HaVe It BEATA THAN ME"
                    r "Who are you?"
                    l "I am..."

                    hide hobo
                    with dissolve

                    "Uncovers cloak"

                    show percius at right
                    with dissolve

                    p "Sir Percius but you may call me Percius and whats yours fair maiden."
                    r "Rika, S-s-sir."
                    p "So you are going to the circus. May I join your quest."
                    menu:
                        "yes":
                            jump along
                        "no":
                            jump alone

                    label along:
                        r "You m-may join."
                        p "thank you madame"

                        "Rika and Percius walk along the road and reach the tent"

                        scene tent with fade

                        show Rika icon1 at center
                        with dissolve

                        show percius at right
                        with dissolve

                        r "So this is the circus I wonder if I can see any clowns"
                        p "You might be able too, What is that orange cloud over there"
                        r "Don't know lets check it out"

                        show clown at left
                        with dissolve

                        c "I ain't no gosh darn cloud"
                        p "Sorry mister clown our mistake"
                        c "No problem happens more often than one would excpect"
                        r "Need any help with the prep work before the show"
                        c "Actually I do"
                        r "With what"
                        c "Water ballon testing"
                        p "In the middle of winter!"
                        c "That's why I need help non of my friends wants to be hurt befroe the show"
                        r "Okay we'll do it's christmas after all"
                        "And they did do it"
                        r "AGHHHHHHHH"
                        p "IT HURTS"
                        c "HAHAHAHHAHAHHAHHAHAH"
                        "Sometime later"
                        c "Thank you so much Merry Christmas"
                        r "Merry Christmas see you again sometime"
                        p "Merry Christmas"
                        "So they left"

                        scene road with fade

                        n "Invite him over for christmas"

                        menu:
                            "Invite him":
                                jump invite

                            "Do not":
                                jump sucker

                        label invite:

                            show Rika icon1 at center
                            with dissolve

                            show percius at right
                            with dissolve

                            show nar icon1 at left
                            with dissolve

                            r "So percius"
                            p "Yeah"
                            r "Wanna tag along"
                            p "Wait you're inviting me to your house on christmas"
                            r "Yes"
                            p "I'm in"
                            r "Okay let's go"

                            scene inside

                            show Rika icon1 at center
                            with dissolve

                            show percius at left
                            with dissolve

                            r "Mother I have returned"

                            g "Oh lord why have ypu forsaken me"

                            show mo icon1 at right
                            with dissolve

                            g "Who is he and why is he in my home"
                            r "He is a friend from the road"
                            p "Hello, mam sorry for not calling before"
                            g "I am not letting this slide"
                            g "Either he leaves or you both do"
                            menu:
                                "don't leave":
                                    jump donotleave

                                "leave":
                                    jump leave

                            label donotleave:
                                r "Percius leave, I can't defy mother"
                                p "I understand"
                                s "I don't..."
                                hide percius
                                with dissolve

                                show Santa icon1 at left
                                with dissolve
                                s "I don't understand how you can say such stuff"
                                s "Asking him to leave sure, but your manor of doing so is terrible"
                                r "I am sorry Santa"
                                s "I hope you are"

                                scene dead with fade
                                ".:. Bad ending 6/6"
                                return



                            label leave:
                                r "Percius were leaving"
                                p "Okay, you're mother seems to be in a crank mood"
                                r "She is ALWAYS this way"
                                g "I can hear you"
                                r "That was the point of it"
                                g "You little"
                                s "I wouldn't do that if I was you"
                                g "WHOOOO?"

                                scene dead_mom
                                scene inside

                                show Santa icon1 at left
                                with dissolve

                                s "Me"
                                r "Santa thank you"
                                s "You are now free from suffering"
                                ".:.good ending?"
                                return

                        label sucker:

                            show Rika icon1 at center
                            with dissolve

                            show percius at right
                            with dissolve

                            show nar icon1 at left
                            with dissolve

                            r "I am going home now"
                            p "I don't have a family can I join you"
                            r "No"
                            p "Okay, alcohol here I go"

                            hide percius
                            with dissolve

                            show hobo
                            with dissolve

                            n "Now you've done it"
                            r "Well it was either him or me"
                            s "There is always room for more people on christmas"
                            show santa
                            with dissolve
                            r "Not in my home"
                            s "Well, you still could have been nicer about it"
                            scene dead with fade
                            ".:. Bad ending (5/6)"
                            return

                    label alone:
                        r "No, I will leave all alone since I don't know you."
                        p "Fine I don't need you anyways I have alcohol"

                        hide percius
                        with dissolve

                        show hobo at right
                        with dissolve

                        show nar icon1 at left
                        with dissolve

                        n "Rika you just turned that gentleman to drinking"
                        r "So what I don't want to help a drunkie"
                        n "You know santa will remember that"
                        r "Yeah yeah so you say"

                        hide hobo
                        with dissolve

                        "Rika continued down the road"

                        scene tent with fade

                        show Rika icon1 at center
                        with dissolve

                        r "Hey clowns where ya at"

                        show clown at right
                        with dissolve

                        c "Why are you here we don't start in three hours"
                        r "Just wanted to see your red nose"
                        c "You know little lady you sure are rude"
                        r "If I am the rude one you're the boring one"
                        "I've seen enough, move clown"

                        hide clown
                        with dissolve

                        show Santa icon1 at right
                        with dissolve

                        r "Here we go what did I do wrong"
                        s "You turned a man to alcohol"
                        r "Too be truthful so was he like that when I found him"
                        s "Let me finish... and you harrassed a clown for no reason"
                        r "When you put it like that I understand, will you let me go?"
                        s ".......No"

                        scene dead with fade
                        ".:. Bad ending(3/6)"
                        return

                label cave:
                    r "I have chosen to adventure deep into the caverns of HELL"
                    r "Mom, I am going to the strange cave in the mountains"
                    g "Good"
                    r "Okay love you bye"

                    scene dark with fade

                    show Rika icon1 at center
                    with dissolve

                    show Creat at right
                    with dissolve

                    m "Wha yu wa wi mi"
                    r "I just wanted to see if there was something in this cave"
                    m "Wel it jus b mi"
                    r "I can see that so who are you exactly"
                    m "Don't remember"

                    show nar icon1 at left
                    with dissolve

                    n "Help him"
                    menu:
                        "help him":
                            jump help

                        "leave and go to the circus whilst forgetting this encounter":
                            jump tried

                    label help:

                        r "Okay I'll help you"
                        m "Ya tank yu mam"
                        r "So what's the last thing you remember"
                        m "B-b-ba-ba-bar"
                        r "So you went a bar"
                        m "Tr-tri-tried"
                        r "You tried to do what?"
                        m "G-go Go home"
                        r "You tried to get home and got lost"
                        m "Ya, tr-tra-trapped"
                        r "Who trapped you"
                        m "Wife"
                        r "Did you have a child"
                        m "Ya, R-r-r-ika"
                        r "RIKA? Dad?"
                        m "Smile mi plz"
                        "Rika smiles"
                        m "*Cough Cough* Mi daugter mi happy you came"
                        r "Did mom do this"
                        m "Ya"
                        r "Celebrate crimbo with me plz"
                        m "okay"
                        r "We live in the same place"
                        m "Were"
                        "Rika picks up a piece of coal and rips her shirt to draw a map"
                        r "Here you go"
                        "Rika gives her father the map"
                        m "Tank yu"
                        r "Dad I am going to the circus"
                        r "I am so sorry to have to leave you in this state"
                        m "It fine go have fun"

                        menu:
                            "go to the circus":
                                jump circus2

                        label circus2:

                            scene road with fade

                            "Rika left her faher and headed to the circus"

                            show Rika icon1
                            with dissolve

                            r "Why did I choose the circus it's five miles away from home"

                            show hobo at right
                            with dissolve

                            l "AOUH, STOUP COMPlANING LiTtLE GURL"
                            l "YoU HaVe It BEATA THAN ME"
                            r "Who are you?"
                            l "I am..."

                            hide hobo
                            with dissolve

                            "Uncovers cloak"

                            show percius at right
                            with dissolve

                            p "Sir Percius but you may call me Percius and whats yours fair maiden."
                            r "Rika, S-s-sir."
                            p "So you are going to the circus. May I join your quest."
                            menu:
                                "yes":
                                    jump along2
                                "no":
                                    jump alone2

                            label along2:
                                r "You m-may join."
                                p "thank you madame"

                                "Rika and Percius walk along the road and reach the tent"

                                scene tent with fade

                                show Rika icon1 at center
                                with dissolve

                                show percius at right
                                with dissolve

                                r "So this is the circus I wonder if I can see any clowns"
                                p "You might be able too, What is that orange cloud over there"
                                r "Don't know lets check it out"

                                show clown at left
                                with dissolve

                                c "I ain't no gosh darn cloud"
                                p "Sorry mister clown our mistake"
                                c "No problem happens more often than one would excpect"
                                r "Need any help with the prep work before the show"
                                c "Actually I do"
                                r "With what"
                                c "Water ballon testing"
                                p "In the middle of winter!"
                                c "That's why I need help non of my friends wants to be hurt befroe the show"
                                r "Okay we'll do it's christmas after all"
                                "And they did do it"
                                r "AGHHHHHHHH"
                                p "IT HURTS"
                                c "HAHAHAHHAHAHHAHHAHAH"
                                "Sometime later"
                                r "Clown, Guess what"
                                c "What has somthing good happend"
                                r "Yes, My father came back after five years"
                                c "I'm so happy for you"
                                p "Me too Rika"
                                r "So it seems like miracles really can happen"
                                c "Thank you so much for the help, Merry Christmas"
                                r "Merry Christmas see you again sometime"
                                p "Merry Christmas"
                                "So they left"

                                scene road with fade

                                show nar icon1 at left
                                with dissolve

                                n "Invite him over for christmas"

                                menu:
                                    "Invite him":
                                        jump invite2

                                    "Don't":
                                        jump sucker2

                                label invite2:

                                    show Rika icon1 at center
                                    with dissolve

                                    show percius at right
                                    with dissolve

                                    r "So Percius wanna you wanna come over"
                                    p "Are you sure taht you would want that"
                                    p "With your father coming over and all"
                                    r "Yeah I am sure"

                                    "And so they made their way home to Rika"

                                    scene dark with fade

                                    show Rika icon1 at center
                                    with dissolve

                                    r "Hey why is it so dark in here"
                                    r "Percius the light switch is at the door"

                                    scene dead_mom with fade

                                    r "Omg what the actual"
                                    p "Uhm I am guessing that's your mother"
                                    r "Yes that's right"
                                    p "Uhm, Hello"

                                    scene inside with fade

                                    show Rika icon1 at center
                                    with dissolve

                                    show percius at left
                                    with dissolve

                                    r "Father, show yourself"

                                    show Creat at right
                                    with dissolve

                                    m "Hi, dear"
                                    r "Did you kill mom"
                                    m "Yes but she deserved it"
                                    p "Santa might not be a happy with your behavior."
                                    s "You don't know me"
                                    m "Who is the wonderus lad"
                                    r "Percius, but if santa is happy are we happy"
                                    p "Latóm, seems that way"
                                    m "Is he staying with us"
                                    r "Yes, yes he is"
                                    m "Wonderful"

                                    scene black with fade

                                    "With the hag gone the family could finally enjoy life"
                                    show 1 icon1 at center
                                    with dissolve
                                    a "But will that enjoyment last"
                                    a "Only I truly know"

                                    ".:. True ending"
                                    return

                                label sucker2:

                                    show Rika icon1 at center
                                    with dissolve

                                    show percius at right
                                    with dissolve

                                    show nar icon1 at left
                                    with dissolve

                                    r "I am going home now"
                                    p "I don't have a family can I join you"
                                    r "No"
                                    p "Okay I understand you want spend time with your father"
                                    p "My only father is alcohol"

                                    hide percius
                                    with dissolve

                                    show hobo
                                    with dissolve

                                    n "Now you've done it"
                                    r "Well it was either him or me"
                                    s "There is always room for more people on christmas"
                                    show santa
                                    with dissolve
                                    r "Not in my home and with my father hom there is even less than before"
                                    s "Well, you still could have been nicer about it"
                                    scene dead with fade
                                    ".:. Bad ending (5/6)"
                                    return

                            label alone2:
                                r "No, I will leave all alone since I don't know you."
                                p "Fine I don't need you anyways I have alcohol"

                                hide percius
                                with dissolve

                                show hobo at right
                                with dissolve

                                n "Rika you just turned that gentleman to drinking"
                                r "So what I don't want to help a drunkie"
                                n "You know santa will remember that"
                                r "Yeah yeah so you say"

                                hide hobo
                                with dissolve

                                "Rika continued down the road"

                                scene tent with fade

                                show Rika icon1 at center
                                with dissolve

                                r "Hey clowns where ya at"

                                show clown at right
                                with dissolve

                                c "Why are you here we don't start in three hours"
                                r "Just wanted to see your red nose"
                                c "You know little lady you sure are rude"
                                r "If I am the rude one you're the boring one"
                                "I've seen enough, move clown"

                                hide clown
                                with dissolve

                                show Santa icon1 at right
                                with dissolve

                                r "Here we go what did I do wrong"
                                s "You turned a man to alcohol"
                                r "Too be truthful so was he like that when I found him"
                                s "Let me finish... and you harrassed a clown for no reason"
                                r "When you put it like that I understand, will you let me go?"
                                s ".......No"

                                scene dead with fade
                                ".:. Bad ending(3/6)"
                                return
                    label tried:
                        scene black
                        with fade

                        show Rika icon1
                        with dissolve

                        "What are you doing leaving him all alone in his state"
                        r "I don't have time to sit around with this demetented creature"

                        show Santa icon1 at right

                        s "Yes you do and you will"
                        r "I will leave one way or another"
                        s "Yes and all of those are in a casket"

                        scene dead with fade
                        ".:. Bad ending(4/5)"
                        return
        label NO:
            r "NO, I won't be nice"
            n "So you have chosen death, SANTA!!!"
            show Santa icon1 at right
            with dissolve
            s "You will die now little girl."
            scene dead with fade
            ".:. Bad ending(1/6)"
            return
