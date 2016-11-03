# Event content for all the events that can happen in the evening,
# where we relax together

# Relationship Focus Events

# Put together a barn
label relax_together_0:
    call play_scene_music
    scene bg farm_interior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve
    
    "Everything here seemed to take ten times as much time and effort. It took twenty minutes just to boil water, because of the increased atmospheric pressure compared to Earth."
    show her concerned
    "So, after finally finishing up the dinner dishes, I was exhausted. I just wanted to snuggle on the couch and watch a movie or something."
    him "Hey, want to help me setup the barn? I got the walls from the shuttle yesterday."
    her surprised "Now?!"
    him normal "Yeah, the sooner the better. Lettie needs a place to sleep, you know."
    menu:
        "What should I say?"
        "No way.":
            her concerned "Sorry, I'm way too tired for that."
            him concerned "Oh, okay. Well, I can probably get someone else to help..."
            her normal "Okay."
            $ relaxed += 3
            return
        "I can help you tomorrow.":
            $ relaxed += 2
            $ loved += 2
            her concerned "Can it wait until tomorrow? I'll have more time to help you then."
            him "Sure, let's do it tomorrow."
            "I was tired the next day, too, but I helped him out anyway."

        "I guess.":
            $ loved += 5
            her sad "I guess I can help out...."
            him happy "Great! Let's get started!"
            scene bg farm_exterior with fade
            "His enthusiasm was kind of infectious, and once we got started, I could see how important it was to him. It was dark when we finally finished..."
            
    scene bg barn with fade
    $ wearing_dress = False    
    show her normal at midleft
    show him normal at midright
    with dissolve
    her happy "This is a nice little barn!"
    him happy "Yeah, let's see how she likes it!  C'mon Lettie!"
    show lettie at right behind him, her with moveinright
    show her at quarterleft with move
    play bg_sfx "sfx/clipclop.mp3"
    "He led his horse into one of the stalls. She was nervous at first, but soon she was in a stall chewing hay like normal."
    play bg_sfx "sfx/whinny.mp3"
    him normal "Thanks a lot, [her_name]. This is great."
    her normal "You're welcome."

    return

# Onsen
label relax_together_1:
    call play_scene_music
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
        
    "One of the things I missed most about Earth was having my own shower and bath. While we washed up daily with water from the well, we still enjoyed going to the community bath once a week or so to really get clean."
    her concerned "I really need a bath."
    him surprised "Really? You smell great to me."
    "I sniffed the air. All I could smell was hay and compost and sweat."
    her flirt "Ick, you need a bath, too! Let's go tonight."
    him happy "Sure, after dinner and...dessert."
    her happy "You made dessert?! What kind?"
    him flirting "I was thinking we'd make some dessert...together."
    her flirt "Ohhh, {b}that{/b} kind of dessert."
    him surprised "Yes...though we could have dessert first, you know. Sometimes it's fun to break the rules."
    menu:
        "What should I say?"
        "Dinner first.":
            her happy "How about dinner first? You can think of it as an appetizer..."
            him flirting "Hmmm, you're very appetizing."
            "We played footsie under the table while we ate and gave each other suggestive looks. Dinner didn't last very long..."
            $ loved += 2
            $ made_love += 1
        "Dessert first.":
            her laughing "Life is short; eat dessert first!"
            show him laughing
            "And what a dessert it was..."
            $ loved += 2
            $ made_love += 1
        "No dessert tonight.":
            her concerned "I think I'd rather skip dessert tonight..."
            him concerned "Oh...okay. Sure, let's just eat dinner."
            $ loved -= 5
            
    "Afterwards, we packed up our towels and toiletries and headed down to the bathhouse."            
    scene bg bathhouse with fade
    show him normal at midleft
    show her normal at center
    with dissolve
    "We built a fire to heat up one of the tubs of water. Then we washed off and got in the hot water."
    scene bg bathhouse with fade
    $ is_nude = True    
    show him nude sleeping at midleft, squatting
    show her sleeping at center, squatting
    show bathhouse_overlay    
    with dissolve

    play bg_sfx "sfx/splash.mp3"
    "It felt so good to soak and relax together."
    
    if (relaxed < -5):
        $ relaxed = 0
    else:
        $ relaxed += 5
    scene black with fade
    $ is_nude = False
    return

# Skinny dipping!
label relax_together_2:
    call play_scene_music    
    scene bg pond with fade
    show night
    stop music fadeout 1.0
    play bg_sfx "sfx/stream-3.mp3" loop fadein 1.0
    "We went on a moonlight walk to the river. We sat down where the water was deep, slow, and clear. I put my head on his shoulder, breathing in the cool night air."
    show her normal at midleft
    show him normal at center
    her normal "This is so relaxing..."
    him normal "Yeah... "
    show him laughing with dissolve
    extend "Want to go for a swim?"
    her surprised "Are you nuts?!"
    him happy "Yes!"
    show him nude normal at quarterright with move
    "He took off his clothes - all of them - and cannonballed in, splashing me."
    show him nude at squatting with move
    show pond_overlay behind her
    show him nude happy behind pond_overlay
    play sound "sfx/splash.mp3"
    her annoyed "Hey! That's cold!"
    if (skill_physical >= 20):
        "I was a little wary of getting in the water ever since I encountered those pond leeches, but we had never seen any in the fast-moving river water."
    menu:
        "What should I do?"
        "Join him.":
            her flirt "Watch out, here I come!"
            "I undressed slowly. There was enough moonlight that I knew he could see me."
            him nude flirting "Whoo! Alright, [her_name]! Come on in!"
            show her normal at center with move
            show her normal at sitting behind pond_overlay with move 
            $ is_nude = True
            play sound "sfx/splash.mp3"        
            "I decided to get back at him by jumping in right next to him with a big splash, but he didn't seem to mind."
            "The water was cold, but somehow that just made everything more exciting."
            stop music fadeout 1.0
            "When we were done, we got dressed and raced each other home, laughing all the way."
            $ loved += 5
            $ made_love += 1
        "Watch him.":
            her normal "I don't really want to get wet; I'll just watch you."
            him nude flirting "Oh yeah? I better give you a good show, then."
            "He flexed his muscles and then tried to do a handstand on the bottom of the river."
            hide him with moveoutbottom
            her laughing "Ha ha, not bad!"
            show him nude at quarterright, squatting behind pond_overlay with moveinbottom
            stop music fadeout 1.0
            "Soon he got tired of swimming and we headed home together."
            $ loved += 5
        "Leave.":
            stop music fadeout 1.0
            her angry "Ugh, now I'm all wet and cold!"
            him nude flirting "I'll warm you up, [her_nickname]!"
            her annoyed "No thanks, I'm going home."
            stop music fadeout 1.0
            hide her with moveoutleft
            scene black with fade
            "Why did he have to ruin such a nice evening?!"
            $ loved -= 5
    $ relaxed += 3
    stop bg_sfx fadeout 1.0
    scene black with fade
    $ is_nude = False
    return

# Did he only marry [her_name] so he could be a colonist?
label relax_together_3:
    scene bg farm_interior with fade
    show her normal at midright with dissolve
    call play_scene_music("music/You.ogg")
    "One day [his_name] came in from the fields with a big smile on his face."
    show him normal at midleft with moveinleft
    him happy "Ah, [her_nickname], you're such a great part of my life. You've brought me love, joy, and laughter."
    him laughing "You've even brought me to new worlds, literally! There's no way I could have come here without you."
    her surprised "What do you mean?"
    him normal "Well, I mean, it's a colony, right? They want couples, people that are going to have kids, so they can build up the colony."
    her concerned "You mean, you wouldn't have been able to come unless we were married."
    him normal "Probably not. Farmers aren't that hard to find."
    her "You never told me that... So part of the reason you married me was so that you could come to Talaam."
    him serious "No! I mean, that was part of the timing, I guess, but I would have asked you to marry me anyway! That just sort of, made it happen sooner, I guess."
    menu:
        "What should I say?"
        "That makes sense.":
            her normal "That makes sense, I guess. What would it have taken to get you to propose to me, barring extra-terrestrial colonies?"
            him flirting "A tax break, maybe?"
            her annoyed "You're terrible!"
            him happy "I'm kidding, I'm kidding! I guess I was waiting for everything to be just right."
            her normal "Well, I'm glad you did propose, finally. I was wondering if I was going to have to do it."
            him serious "Sorry it took so long - change is hard, you know?"
            her serious"Speaking of which, you should change."
            him surprised "What? What don't you like?"
            her normal "Change out of those clothes! You smell like Lettie."
            him concerned "What's wrong with Lettie?!"
            her flirt "Nothing, but I don't invite Lettie to share my bed."
            him normal "I see your point."
            $ loved += 5
            $ made_love += 1
            $ relaxed += 5

        "That bothers me.":
            her sad "That bothers me. Why didn't you tell me that was one of the factors?"
            him annoyed "Because it's not romantic? It doesn't really sound good to say, 'Hey, I want to be a colonist, and I have to be married, and you're the person I like the most, so want to get married?'."
            her annoyed "Wow, it sounds even worse when you put it like that."
            him serious "Exactly! I wanted to get married either way; the whole colony thing just made me quit stalling and ask you."
            her concerned "I still wish you had told me about that earlier."
            him concerned "I'm sorry, [her_nickname]. But I do love you, no matter what."
            her sad "I love you, too, [his_nickname]. But... never mind."

            $ loved += 2
            $ relaxed += 3

        "That's deceitful.":
            her annoyed "That's deceitful. I feel used."
            him surprised "Why? It's not like I only married you so I could come be a colonist."
            her angry "Really? Because that's exactly what it feels like."
            if (not want_kids):
                her annoyed "Also, we're not ready for kids, and who knows when we will be? You didn't promise them we'd have kids, did you?"
                him serious "No! I mean, it's sort of expected, but-"
                her yelling "And you didn't think that was something I should know?!"
                him angry "I thought it was obvious! And, anyway, who cares what they think?!"
                her concerned "I do! Now I feel like, if we don't have kids soon, we're not keeping up our side of the agreement. Even though it was an agreement I knew nothing about!"
                him annoyed "Sorry, I guess I just assumed we'd have kids eventually and it wouldn't really be a big deal."
                her annoyed "..."
            him annoyed "I don't know what you want me to say. I just told you that I love you and everything you've brought into my life, and somehow you've turned it into a big argument."
            her angry "I've turned it into an argument?! You're the one that didn't tell me this earlier!"
            him angry "I'm sorry, okay?! What more can I say?!"
            her sad "Nothing. Just- don't say anything more right now."
            $ loved -= 5
        
    return

# Massage time!
label relax_together_4:
    call play_scene_music
    scene bg farm_interior with fade
    show him serious at midleft
    show her normal at midright
    with dissolve
    "One day after dinner I noticed [his_name] rubbing his shoulders and grimacing."
    her surprised "Are you okay?"
    him concerned "Yeah, I'm just really sore from all the digging I've been doing lately."
    if (relaxed < 0):
        her concerned "Yeah, I feel pretty tense, too."
        "I could have rubbed his shoulders, I guess, but I was just too tired."
        $ relaxed += 3
    else:
        her happy "Want me to rub your shoulders?"
        him happy "I would love that!"
        show her normal at center, behind him
        show him at squatting
        with move
        "I started off gently. His muscles were so tight, I was amazed he could move at all. I gradually kneaded harder, trying to tell what sorts of massage he liked."
        him serious "Ohhh, that feels so good."
        show him sleeping with dissolve
        "Sometimes he would make sort of painful grunt that let me know he didn't like what I was doing. But he would also sigh with content when I hit a particularly tense spot."
        "I noticed his smell, too - there was a hint of horse (ew), but mostly he smelled like fresh dirt and hard work."
        if (relaxed >= 5 and skill_physical >= 10):
            "After his shoulders, I massaged his arms and hands. It made me think of how hard he had been working all day."
            
            if (skill_physical >= 30):
                "My hands were starting to get a little tired, but I didn't want to stop yet, so I rubbed his legs and feet, too."

        "To finish off I massaged his neck and head. I could tell he really enjoyed it."
        show her at midright
        show him at standing
        with move
        if (loved >= 5):
            him normal "Now it's your turn to get massaged."
            her flirt "Mmmm, really? Are you talking about shoulders, or...?"
            him flirting "I'll massage anything you like."
            her normal "Why don't you start with the shoulders, and then we'll see what happens?"
            show him normal at center, behind her
            show her sleeping at squatting
            with move
            "He copied what I had done earlier, and gave me quite the massage, too. It was so relaxing to just sit and do nothing while he took care of all my tense muscles."
            her sleeping "You take such good care of me..."
            him happy "We take good care of each other."
            $ made_love += 1
        $ relaxed += 5
        $ loved += 5

    return

# go "out" to eat on a picnic
label relax_together_5:
    $ wearing_dress = False
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    call play_scene_music("music/Rain.ogg")
    him happy "Put on your fancy clothes, [her_nickname], because we are going OUT tonight!"
    her surprised "Out where? And I don't have any fancy clothes..."
    him normal "Any clothes look fancy on you! But I can't tell you where we're going; it's a surprise."
    her normal "Okay, let me get ready, then. I can at least brush my hair."
    her surprised "(Where can we be going?)"
    hide her with moveoutright
    $ wearing_dress = True
    show her normal at center with moveinright
    him normal "Now put this blindfold on."
    her surprised "You're not serious, are you?!"
    him happy "I'm totally serious!"
    scene black with fade
    play bg_sfx "sfx/alien-crickets.mp3" loop 
    "I let him blindfold me and we left the house.  He spun me around so I couldn't tell which direction we were going, and then we hiked for about twenty minutes or so, holding hands."
    "With the blindfold on, the sounds of Talaam's strange night critters sounded even louder and stranger."
    "He guided me up and over some large rocks as we climbed and climbed."
    him "We're almost there."
    "Finally, he took off the blindfold."
    scene bg sunset with fade
    "He had setup a small table and two chairs with dishes and utensils. I sat down at the table and he lit the candles.  Then he got some food out of his backpack."
    show her normal at midright
    show him normal at midleft
    with dissolve
    menu:
        "What should I say?"
        "It's so cool!":
            her happy "It's...so romantic! Wow, I didn't know you were planning this!"
            him happy "I'm glad you like it! I just really missed taking you out to eat, so I thought this would be as close as we could get."
            $ loved += 2
        "Looks like a lot of trouble.":
            her concerned "Wow, you went to a lot of trouble to set this all up. I feel bad..."
            him happy "Don't feel bad; just enjoy it!"
            $ relaxed -= 2
        "What a waste.":
            her concerned "This is really pretty, but isn't it kind of a waste?"
            him flirting "My time is never wasted when it's spent on you."
            $ loved -= 2
    "We ate our candlelight dinner and watched the sun setting over the hills. I couldn't even see our house or the town or anything."
    her serious "It's like we're the only two people in the whole universe."
    him serious "Then we have quite a job ahead of us, don't we?"
    her surprised "A job?"
    him flirting "Repopulating the entire universe. We better get started now, don't you think?"
    menu:
        "What should I say?"
        "You always make me laugh.":
            her laughing "Oh, you...! You always make me laugh."
            him normal "I like it when you laugh."
            $ loved += 2
        "Should we get started like this?":
            her flirt "Should we get started like this...?"
            him flirting "Maybe a little bit of this?"
            her concerned "It's too bad there's so many rocks here..."
            $ loved += 2
        "Is everything about sex to you?!":
            her annoyed "Is everything about sex to you?!"
            him laughing "Ha ha, I'm just kidding. And, anyway, sometimes it's hard to think of anything else when you're right here, looking beautiful..."
            her serious "..."
            $ loved -= 2

    "The food wasn't anything special, but somehow it tasted better combined with a beautiful sunset. Afterwards he gathered up the dishes and walked a little ways away."
    him normal "Come sit down over here, it's softer."
    her surprised "Are these our blankets?! Are we spending the night out here?"
    him happy "If you want to. I thought it would be fun."
    menu:
        "What should I say?"
        "You're so romantic.":
            show her normal at center with move
            her happy "You're so romantic. You thought of everything."
            him serious "I love you, [her_name]."
            $ made_love += 1
        "Great idea!":
            show her normal at center with move
            her normal "What a great idea! You really planned this out, didn't you? How long did it take you to hike out here and bring all this stuff?!"
            him normal "Well, it took several trips... but I just kept thinking of how happy it would make you."
            her serious "Thank you, [his_name]."
            him serious "I love you, [her_name]."
            $ made_love += 1
        "That's presumptuous!":
            her angry "That's pretty presumptuous. You think that just because you setup a fancy dinner that you're automatically going to get some?"
            him annoyed "No! I mean, I was thinking it would be a nice end to the evening, but we don't have to. I just thought it might be romantic."
            her annoyed "Well, it's not. You can't just assume things like that."
            him angry "Sorry for assuming my own wife would want to make love to me."
            "I tried to storm off, but I didn't know which way was home."
            her annoyed "Which way back home?"
            him annoyed "That way."
            stop bg_sfx fadeout 1.0
            "I stomped off towards home, leaving him to carry everything back to the house himself. It wasn't that I didn't appreciate what he did; I just didn't like feeling manipulated."
            $ loved -= 5
            scene black with fade
            $ wearing_dress = False
            return

    $ relaxed += 5
    $ loved += 2
    show her sleeping at squatting
    show him sleeping at squatting
    with move
    "We lay there for a long time..."    
    scene black with fade
    stop bg_sfx fadeout 1.0
    scene bg sunset with fade
    $ wearing_dress = False
    "In the morning, it felt so good to wake up next to him, watching the sky lighten. With one final kiss, we got up and carried everything back to the house together."
    return


# Haircuts!
label relax_together_6:
    call play_scene_music
    scene bg farm_interior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve

    her surprised "Wow, your hair is getting long!"
    him happy "Yeah, I guess I'm going for the Shaggy look..."
    menu:
        "What should I say?"
        "I could cut it for you." if ((skill_creative >= 10) or (skill_domestic >= 10)):
            her normal "I could cut it for you."
            him surprised "Yeah? Do you think it'd turn out okay?"
            her annoyed "It's not that hard to just cut your hair shorter."
            him happy "Well, I guess if it's awful I could just shave my head."
            her happy "It'll look fine! Now sit down while I get some scissors."
            hide her with moveoutleft
            show her at center behind him with moveinleft
            show him normal at squatting with move
            "We didn't have haircutting scissors, so I just used regular scissors and a comb."
            play bg_sfx "sfx/scissors.mp3"
            if (skill_creative >= 40):
                "I gave him a haircut kind of like what he had before. It was easier than I thought."
                her happy "Well, what do you think?"
                him surprised "Hey, that looks good!"
                her flirt "Of course it does."
            else:
                "I tried to give him a haircut kind of like what he had before. It was hard to get the sides even. I'd cut it shorter on one side, and then I'd have to cut the other side to match, but I'd cut a little too much..."
                "Finally, I got it balanced, but his hair was a lot shorter than I'd ever seen it."
                her concerned "Well, what do you think?"
                him surprised "Hey, not bad!"
                her happy "Oh good, I'm glad you like it."
            show him at standing
            with move
            him happy "Ahhh, that feels good."
            him serious "Now it's your turn."
            her surprised "For what?"
            him happy "I'll cut your hair!"
            menu:
                "What should I say?"
                "No way.":
                    her annoyed "No way."
                    him annoyed "Hey, I trusted you with my hair."
                    her serious "My hair's different; it's not just a matter of making it shorter."
                    him concerned "All right, whatever you want."
                    $ loved -= 2
                "Okay, just a trim.":
                    her surprised "You know, the ends could definitely use a trim; just don't cut off too much!"
                    him normal "No problem; just leave it to me."
                    "I was a little nervous as I handed him the scissors and sat down."
                    show him normal at center behind her
                    show her serious at midright, squatting
                    with move
                    play bg_sfx "sfx/scissors.mp3"
                    him serious "..."
                    her concerned "..."
                    show him serious at midleft
                    show her concerned at midright, standing
                    with move
                    him concerned "Okay, that should do it."
                    "I went over to look in the mirror."
                    "It mostly looked the same; he just cut off about an inch in the back."
                    her happy "That's great; thank you!"
                    him serious "Good, I was worried you wouldn't like it..."
                    her flirt "Nope, you did a great job. As always."
                    him happy "I wouldn't want to start a hair salon, but cutting hair is actually kind of fun..."
                    her laughing "Don't get too used to it!"
                    $ loved += 2

                "No, thanks.":
                    her normal "No, thanks, I think maybe I'll grow it out."
                    him normal "Okay, let me know if you change your mind."
                    "I had a ton of split ends, but I'd figure something else out. I just didn't trust [his_name] with my hair..."
        "I like it like that.":
            her "Why cut it? I think longer hair looks good on you."
            him flirting "Oh yeah? Should I grow my beard out long, too?"
            her flirt "Only if you braid it like a dwarf."
        "I think you better cut it.":
            her concerned "Yeah, maybe you should cut it."
            him concerned "My mom always cut my hair at home..."
            him serious "But we're not at home anymore, are we? Guess I'll give it a try... if I totally botch it, I can just shave it all off."
            show her surprised
            hide him with moveoutright
            show him serious with moveinright
            "I watched as he got out some scissors, got his hair wet, and sat in front of the mirror. He cut the bangs and sides first, and did a decent job."
            play bg_sfx "sfx/scissors.mp3"
            show her normal
            him normal "Could you get the back for me?"
            her normal "Okay...I guess I just match up what you did on the sides?"
            him "Yeah, just straight across."
            "I tried to match up what he had done, but I accidentally made it too short..."
            menu:
                "Tell him.":
                    her serious "Sorry, but I made it a little too short in the back... I'm just not very good at this."
                    him serious "Where? Oh, I see. It's okay; I'll just make the sides a little shorter to match."
                    $ loved += 2
                "Don't tell him.":
                    him surprised "Does it look okay?"
                    her concerned "(It's in the back; he'll never see it, anyway)"
                    her serious "Yeah, it's fine."
                    $ loved -= 2
            "I guess the exact hair cut he had didn't matter that much, anyway."
            
        "Sara could cut your hair." if (skill_social >= 30):
            her normal "Did you know Sara went to hair school for a while?"
            him surprised "No, really?"
            her happy "Yeah! Maybe she'd cut your hair, and mine."
            him happy "Let's ask her!"
            scene black with fade
            "She was happy to cut our hair, and did a great job."
            "It felt so good to have my hair neat and the way I liked it."
    $ relaxed += 3
    $ loved += 2
    return

# stargazing together
label relax_together_7:
    scene bg stars with fade
    show her normal at midleft
    show him normal at midright
    with dissolve
    call play_scene_music("music/Will.ogg")
    play bg_sfx "sfx/alien-crickets.mp3" loop
    "We went for a walk together under the stars. I brought my computer pad so we could find which one was our old Sun. I didn't see any constellations I recognized, so it was hard to find any reference points, but we finally found which one we thought it was."
    her concerned "It looks so small..."
    him serious "Remember how small Talaam's sun looked from Earth?"
    her serious "That seems so long ago..."
    if (loved >= 0):
        "We held hands and walked together, and though I felt so small in the universe, I knew [his_name] and I had a place with each other."
        
    stop bg_sfx fadeout 1.0
    $ relaxed += 5
    $ loved += 1

    return

# walk around the farm together looking at what you've created together.
label relax_together_8 :
    call play_scene_music
    scene bg fields with fade
    "We walked around the farm together. [his_name] showed me where all the different crops were, and told me about what kind of soil they liked and what the weeds were like."
    show her normal at midright
    show him normal at midleft
    with dissolve
    her normal "This is like your baby, isn't it?"
    him normal "Yeah, it is."
    him laughing "Who's the cutest widdle farm on the planet, huh? You are!"
    "I could tell it meant a lot to him to show me everything he had been working on."
    $ relaxed += 3
    $ loved += 1
    return

label relax_together_9:
    call play_scene_music
    scene bg farm_interior with fade
    "We made a nice dinner together, and talked while we ate slowly, watching the sun go down."
    $ relaxed += 5
    $ loved += 2
    return    

# People probably won't even see these last ones unless they always choose "Do something with [his_name]", so don't put a ton of effort into them.
label relax_together_10:
    call play_scene_music
    scene bg farm_interior with fade
    "We did the dishes together, and then sat together and talked while we worked on little projects."
    show her normal at midright
    show him normal at midleft
    with dissolve
    him happy "I'm so glad we do things together all the time."
    her happy "Me, too. You're not just my [his_nickname]; you're also my best friend."
    $ relaxed += 5
    $ loved += 2
    return


label relax_together_11:
    call play_scene_music
    scene bg bedroom with fade
    $ is_nude = True     
    show him normal nude at midleft, squatting
    show her normal at center, squatting
    show bedroom_covers
    show night
    with dissolve
    "One night we went to bed early and just started talking. I ended up telling him all about my job. Who was hard to work with, things that seemed impossible, the people I helped..."
    "It felt good to have him know what I had been working on, and know that I had his support."
    $ relaxed += 3
    $ loved += 2
    scene black with fade
    $ is_nude = False
    return

label relax_together_12:
    call play_scene_music
    scene bg bedroom with fade
    $ is_nude = True
    show night
    show bedroom_covers behind night        
    show him normal nude at midleft, squatting, behind bedroom_covers
    show her normal at center, squatting, behind bedroom_covers
    with dissolve
    "We snuggled together in bed and talked softly together."
    $ relaxed += 5
    $ loved += 2
    scene black with fade
    $ is_nude = False
    return


# Events that can happen in any order. 

# Play games with Ilian and Sara
label relax_together_a:
    call play_scene_music
    $ wearing_dress = False
    scene bg farm_exterior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve
    him "Hey, [her_name], want to go into town with me?"
    her surprised "You're going to town? That's a rare occasion..."
    him serious "I'm taking a load of extra food to the storehouse."
    her normal "Sure, I'll go with you."

    scene bg path with fade
    show him normal at midright
    show her normal at center
    show lettie at right behind him, her
    with dissolve
    play bg_sfx "sfx/clipclop.mp3"
    "We walked beside Lettie, who was pulling the wagon. We talked and laughed, and when we dropped off the food we saw Ilian and Sara."
    stop bg_sfx fadeout 1.0
    scene bg storehouse with fade
    show sara at quarterright
    show ilian at right
    with dissolve
    show him normal at left
    show her normal at quarterleft
    with moveinleft
    her happy "Hey, Sara!"
    sara "Wow, you got [his_name] to come to town? Did you pretend to be sick or something?"
    her flirt "No, he came on his own, believe it or not."
    him serious "Hey, I'm working hard on the farm, I don't have time to come to town all the time."
    ilian happy "Well, since you're here, would you like to come over and see our house?"
    sara "Yeah, because it's SOO different from all the other prefab houses..."
    ilian normal "I was trying to be nice..."
    sara "Our house is totally boring, but maybe we can play a game or something?"
    her happy "Thanks, that'd be fun! Right, [his_name]?"
    him concerned "..."
    if (loved >= 0):
        him normal "Sure, let's go."
        scene bg farm_interior
        show sara at quarterright
        show ilian at right
        show him normal at left
        show her normal at quarterleft
        with dissolve
        "The four of us played Machine of Death."
        ilian happy "...which is why he never saw it coming when the piano crashed down ten stories onto his head."
        him happy "Ohhh! You got him! That was awesome."
        sara "That was way better than [her_name]'s poison-in-the-toothpaste attempt."
        her annoyed "That would totally work!"
        scene black with fade
        "I think it was good for [his_name]... and I definitely had fun, too."
        $ relaxed += 5
        $ loved += 2
        $ community_level += 2
    else:
        him concerned "Sorry, I've got to do some things at home."
        menu:
            "What should I do?"
            "Go with [his_name].":
                her normal "Yeah, I should probably get going, too. Maybe another time, Sara?"
                sara "Yeah, I'll see you at lunch or something."
                "We both worked hard on our projects at home, but at least we were together."
                $ relaxed += 2
                $ loved += 2
            "Hang out with Ilian and Sara.":
                her normal "Well, I'll come over, if you don't mind."
                sara "Sure, we can play with three people."
                her "Bye, [his_name]."
                him serious "Bye..."
                scene black with fade
                "We played some games together, but I felt a little out of place without [his_name]. Maybe he'd come next time..."
                $ loved -= 2
                $ relaxed += 2
    return
    
label relax_together_b:
    call play_scene_music
    scene bg farm_interior with fade
    "We watched a sports game together. It was hard to get too excited about it, since it happened on Earth four years ago, and I didn't feel as loyal to any of the teams now that I wasn't even on the same planet as them."
    "But it was still fun to see their skill and see how they played so hard."
    $ relaxed += 3
    $ loved += 2
    return

label relax_together_c:
    call play_scene_music
    scene bg farm_interior with fade
    "We played card games and flirted shamelessly. Sometimes I even let him win."
    $ relaxed += 3
    $ loved += 2
    return

label relax_together_d:
    call play_scene_music
    scene bg farm_interior with fade
    play bg_sfx "sfx/rain-02.ogg" loop
    "It was a rainy evening, and we were both reading on our computer pads, sitting near each other."
    "We didn't talk much, but everyone once in a while we would look up and smile at each other."
    "It was nice that we didn't always have to be doing the same thing to spend time together."
    $ relaxed += 3
    $ loved += 2
    stop bg_sfx
    return

label relax_together_e:
    call play_scene_music
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    "We played video games together on our computer pads. We liked to play on the same team."
    her surprised "Oh, that's a great place to put that ice tower!"
    him happy "I know, it just hits them right when they first come in-"
    her happy "...and slows them down so they get hit by my fireballs. Perfect!"
    him flirting "One more level?"
    her normal "I'll probably regret it tomorrow but... bring it on!"
    $ relaxed += 3
    $ loved += 2
    return

# She's "stunning"
label relax_together_f:
    call play_scene_music
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    
    him surprised "...!"
    her surprised "What is it? Is everything okay?"
    him surprised "...!"
    her flirt "Why are you staring at me like that?"
    him surprised "You're just... so stunning... I'm totally stunned."
    her annoyed "You're stunned."
    him surprised "Yup, can't move. Can only... gaze upon... your radiant beauty..."
    her flirt "Hmm, what if... I tickle you?!"
    show her happy at center with move
    him laughing "Oh! Suddenly I can move again!"
    her flirt "You're so silly."
    if (loved >= 0):
        him serious "I'm being completely serious. You're like, sweeter than a hot fudge sundae, and hotter than a habanero, and brighter than any sun, anywhere!"
        her normal "Awww... I love you, [his_name]."
        "He picked me up and spun us around before covering my face in kisses."
        him "And I love you, [her_name]."
    else:
        him serious "I'm being completely serious."
        her annoyed "..."
    
    $ relaxed += 5
    $ made_love += 1
    $ loved += 2
    return


# Midnight lovin'
label relax_together_g:
    call play_scene_music
    scene bg bedroom with fade
    show her flirt at midright
    with dissolve

    "I decided to surprise [his_name] with a few candles lit near our bed and some soft music playing, and I wore the sexiest thing I owned. But it didn't go how I had planned..."
    show him normal at midleft with moveinleft
    him flirting "Oh! Wow, you look really hot..."
    him sad "...but I'm kind of in a hurry, I gotta go fix something before the wind totally breaks it apart."
    her concerned "You don't have fifteen minutes for me?"
    him normal "Well, yeah, if you can wait until I get this done. You don't mind, do you?"
    her yelling "Yes I mind! I've been sitting here waiting for you for hour!"
    him angry "Look, I just can't right now! I'll be back in after I fix this!"
    hide him with moveoutleft
    show her concerned with dissolve
    "He left."
    show her annoyed with dissolve
    "I waited."
    show her angry at squatting
    show bedroom_covers
    with dissolve
    "And waited."
    $ is_nude = True
    show her sleeping at squatting with dissolve

    "And waited."
    scene black with fade
    "Finally, I just went to sleep."
    scene bg bedroom with fade
    show her sleeping at midright, squatting
    show bedroom_covers
    with dissolve
    show him nude serious at center, squatting, behind bedroom_covers with dissolve
    show night
    show bedroom_covers behind night
    play bg_sfx "sfx/cloth.mp3"
    "I half awoke in the middle of the night to [his_name] snuggling up to me and nuzzling my ear."
    her concerned "Wha-huh?"
    him nude normal "I'm home..."
    her annoyed "Welcome home...and good night."
    him nude flirting "You don't want to stay up for just fifteen more minutes?"
    her annoyed "I'm not up to begin with. I'm still asleep. Zzzzzz..."
    show her sleeping
    him nude normal "Mmm, you're so sexy..."
    menu:
        "What should I do?"
        "Wake up for some action.":
            her flirt "I just can't say no to you..."
            him nude flirting "Why would you want to?"
            her surprised "Did you get everything fixed up outside?"
            him nude sad "Yeah, sorry it took so long; that wind is awful."
            her flirt "You're awful, to keep me waiting so long."
            him nude flirting "I know, I better be extra good to you."
            "[his_name] was definitely worth waking up for."
            $ made_love += 1
            $ loved += 3
            $ relaxed += 5
        "Go back to sleep.":
            her concerned "I'm so sleepy..."
            him nude sad "..."
            her normal "But I love you."
            him nude normal "I love you too, [her_name]."
            "He kissed me one last time, and then held me close as I fell back asleep."
            show her sleeping
            show him nude sleeping
            with dissolve
            $ loved += 2
            $ relaxed += 3
        "Tell him off.":
            her angry "You had your chance, but you missed it. Sorry, I can't just wait around all day for you to finally decide to show up and get some action."
            him nude concerned "C'mon, [her_nickname]..."
            her annoyed "Just leave me alone."
            show him nude angry at quarterleft with move
            him "Fine."
            "We lay there, both angry, not saying anything, for a long time, before I finally got back to sleep."
            show him nude sleeping
            with dissolve
            show her sleeping
            with dissolve
            $ loved -= 2
            
    scene black with fade
    $ is_nude = False
    return

# Zombie Dinosaur Movie
label relax_together_h:
    call play_scene_music
    scene bg farm_interior with fade
    "We watched a movie together. It was pretty good, but the ending was terrible."
    show her normal at midright
    show him normal at midleft
    with dissolve
    him happy "See, what they needed was to have the girlfriend show back up at the end--"
    her laughing "--leading a horde of zombie warriors! Oh, that would have been so much better!"
    him surprised "And what about the pterodactyl? They didn't do anything with that."
    her serious "I know, I kept thinking someone was going to ride it."
    him normal "I thought it was going to turn out to be a cyborg pterodactyl."
    her normal "That would have been awesome!"
    "Sometimes talking about the movie is more fun than the actual movie itself..."
    $ relaxed += 3
    $ loved += 2
    return

# Daisy-chain circlet of wildflowers
label relax_together_i:
    call play_scene_music
    $ wearing_dress = False
    scene bg fields with fade
    show her normal at midright
    with dissolve
    "I was weeding in the backyard when I found some wildflowers. They reminded me of clover, so I made a daisy-chain circlet out of them. It was fun."
    show him normal at midleft with moveinleft
    menu:
        "What should I do?"
        "Do a little dance":
            show her happy at right with move
            show her flirt at squatting with move
            show her normal at midright, standing with move
            him happy "Wow, you're like a woodland nymph."
            her flirt "Think you can catch me?"
            show her laughing at right with move
            "I darted away, throwing a teasing smile over my shoulder at [his_name]."
            show him happy at quarterright with move
            show her happy at left with move
            "He ran after me as I hopped over fences and twirled around trees."
            show him laughing at midleft with move
            if (skill_physical >= 60):
                "He was slowing down. I decided it would be more fun to let him catch me."
            show him normal at quarterleft, sitting
            show her flirt at left, sitting
            with move
            "He finally caught up to me and tackled me playfully."
            him flirting "Hmmm, now that I've captured you, what'll you give me?"
            "I draped the flower circlet over his head."
            her flirt "How about that?"
            him serious "How about this?"
            "He kissed me softly on the forehead, then on the cheeks, then finally I grabbed his head and brought our lips together."
            
        "Make matching flower circlets.":
            him surprised "What am I, king of the faeries?"
            her happy "And I'm the queen! All the insects will obey our orders!"
            him flirting "Shall I address you as Queen Mab from now on?"
            her flirt "Yes. I'll fulfill all your wishes... in your dreams."
            him serious "Ooo, harsh. But being with you is like a dream come true, so does that mean you'll fulfill my wishes here?"
            "You get in a tickle fight, and one of your flower bracelets falls off. It was fun while it lasted."
            $ made_love += 1
            
        "Apologize":
            her concerned "Sorry, this is kind of a waste of time, isn't it?"
            if (loved < 0):
                him concerned "Yeah... we really need to get rid of those weeds."
                her sad "Okay."
                him normal "Here, I'll help you."
                her normal "Oh, thanks!"
            else:
                him happy "If it makes you happy, it's not a complete waste of time. Here, I'll help you finish pulling the weeds."
            "We finished pulling the weeds together while we talked."
                
    $ loved += 2
    $ relaxed += 3
    return

# Messages on the computer
label relax_together_j:
    call play_scene_music
    scene bg farm_interior with fade
    show her normal at right
    show him normal at left
    with dissolve
    "I was sitting at the table, reading on my computer pad, when I got a message from [his_name]."
    show her surprised
    play bg_sfx "sfx/message.mp3"
    "(Why is he sending me a message? He's right there...)"
    him_c "Right now I am sitting five feet away from the hottest chick in the universe."
    menu:
        "What should I write back?"
        "I'm jealous!":
            her_c "I'm so jealous, who is she?!"
            him_c "Her name's [her_name]; you've probably heard of her. She's famous for her quick wit and good looks."
            her_c "Tell me more about her."
            him_c "Well, she's not conceited at all, that's one thing I like about her, and she's funny and creative, and she's got these lips that just beg to be kissed."
            her_c "So kiss them already!"
            show her flirt
            show him flirting at midright with move
            "He sauntered over with a grin, leaned down, and kissed me like we had never kissed before."
            $ made_love += 1
            $ loved += 2
        "I'm next to a hot guy.":
            her_c "Oh yeah, well I'm sitting right next to the sexiest man alive, or dead!"
            him_c "Sexier than Clark Gable and Abraham Lincoln?!"
            her_c "Definitely. He's funny, and hard-working, and when he looks at me, he's got these intense eyes-- I just melt."
            him_c "What a lucky guy..."
            show him serious
            show her laughing
            "He looked over at me with what I'm sure he thought was a melting gaze, but instead it just made me laugh."
            show him laughing
            show her flirt at midright
            show him flirting at midleft
            with move
            
            "Soon he was laughing, too, and we were kissing, and everything seemed just about perfect."
            $ loved += 2
        "Nothing.":
            "I didn't write him back. He's just being silly, to send me a message when I'm right here. I don't have time for that."
            $ loved -= 2
    nvl clear
    $ relaxed += 3
    return


# Baby names
label relax_together_k:
    call play_scene_music
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    if (is_pregnant or want_kids):
        "We were talking about what it would be like when we did have a baby, and soon we started talking about baby names."
    else:
        "Somehow, we started talking about baby names."

    him surprised "You don't like the name Ringo?"
    her annoyed "No! It sounds like a circus master, or a cowboy, or..."
    him happy "Or a totally awesome musician?"
    her angry "No! It just sounds dumb!"
    him annoyed "Well, not as dumb as Benedict. 'Hello, my name is Benedict, I'm a tap-dancing pansy who can't even button his own waistcoat."
    her happy "It's refined and intelligent! And there's nothing wrong with tap dancing, is there?"
    him concerned "No, but do you really think a kid of ours is going to be a tap dancer?"
    her concerned "Probably not."
    show him serious with dissolve
    her normal "Anyway, we'll just keep looking, I bet we can find a name we both like."

    $ relaxed += 3
    $ loved += 2
    return

# Horror puzzle game
label relax_together_l:
    call play_scene_music
    play bg_sfx "sfx/rain-02.ogg" loop
    scene bg farm_interior with fade
    "We played a horror puzzle game together. We were both good at different kinds of puzzles, so we made a good team."
    "...plus I think he liked to see me jump at all the scary parts."
    show her surprised at midright
    show him normal at midleft
    her yelling "AHHHHHHH!"
    him surprised "You didn't know that was going to happen?"
    her annoyed "Well, I knew {b}something{/b} was going to happen, but no! Clowns don't usually have fangs!"
    him happy "Hehe, it's okay, we'll beat him. If we can figure out what to type on the typewriter..."
    her surprised "Oh, try the first letter of each word in the clue!"
    him happy "Yeah!"
    "The game was fun, but I don't think I would have played it on my own. The best part was being with [his_name]."
    stop bg_sfx
    $ relaxed += 3
    $ loved += 2
    return
