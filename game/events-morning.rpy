# Event content for all the events that can happen in the morning,
# either at work or skipping work.

# Default work event if there's no special event
label act_work:
    call set_work_bg
    call play_scene_music
    
    if (relaxed <= -8):
        "I worked hard at work. I was starting to feel burned out, though."
    elif (relaxed >= 8):
        "I breezed through work. Everything seemed easy."
    else:
        "I worked hard at work as usual."
    $ relaxed -= 5
    $ community_level += 1
    $ times_worked += 1
    return

label act_skip_work:
    call set_work_bg
    call play_scene_music("music/You.ogg")
    
    # it doesn't count if you take time off right after giving birth
    if (is_pregnant and (month == 25)):
        "Brennan was taking care of everything he could at work so I could rest after giving birth to [baby_name]."
        $ relaxed += 5
        return
         
    if (slacked_off == 3):
        "The mayor called me in to meet with him after work."
        show pavel at midright,behind her
        show her normal at midleft
        pavel sad "[her_name], I'm worried about you. You haven't been putting in your usual effort at work lately."
        menu:
            "What should I say?"
            "I'm sorry.":
                her concerned "I'm sorry. I should pay better attention to my work."
            "Things are busy at home.":
                her concerned "Sorry - things have been so busy at home, trying to get the farm started and everything."
            "It won't happen again.":
                her serious "I'm sorry - I won't let it happen again."
            "Whatever.":
                her annoyed "Whatever."
                pavel "Excuse me?"
                her "As long as I get my job done, what's the big deal?"
                pavel "Well, just see that you do get it done."
                $ slacked_off = 1
                $ relaxed -= 2
                return
            "I'm pregnant." if ((is_pregnant) or (is_pregnant_later)):
                her serious "Sorry, I didn't think being pregnant would make me so tired."

        pavel normal "I understand, but this can't happen all the time. We need you here."
        her serious "All right, thanks for understanding."
        $ slacked_off = 0
    else:
        "I took a little time off work and didn't push myself this month."
        $ relaxed += 5

    $ slacked_off += 1
    return

# Special Morning Events
label work_0:
    $ times_worked += 1

    scene bg community_center
    call play_scene_music("music/Sojourn.ogg")
    play bg_sfx "sfx/people.mp3" fadein 1.0
    "My boss was also the leader of our little community. I guess you could call him the mayor?"
    "Right after we landed, he called a meeting for everyone where he gave a speech."
    show pavel at center 
    pavel "We made it this far! Now, as you know, we've arrived right at the beginning of this planet's spring, so it's time to get seeds in the ground! We would like for our colony to become self-sufficient as far as necessities are concerned."
    stop bg_sfx fadeout 1.0
    pavel "In two years, another colony ship will come with supplies and more colonists. So, until then, we're on our own."
    pavel "Let me introduce some of our experts, here."
    show pavel at quarterleft, behind naomi with move
    show naomi at center with moveinright
    pavel "First of all, here's my wife Naomi, who is our colony's counselor and chaplain. She will be holding nondenominational religious services once a week for any who are interested, and is also available for individual counseling."
    naomi "I look forward to learning alongside all of you."
    hide naomi with moveoutright
    show lily at midright with moveinright
    pavel "Next is the person who has lived here the longest, astronaut and xenobiologist Dr. Lily. Any scientific inquiries should be directed her way."
    lily happy "Thank you, Mayor."
    hide lily with moveoutright
    show ilian at midright
    show sara at quarterright
    with moveinright
    pavel "Ilian Andrevski is in charge of the storehouse here on the colony. That's where we keep all our extra supplies and food. His wife, Sara will be helping all of us stay organized."
    ilian "I will distribute our resources frugally and fairly."
    sara "If you want an appointment with the mayor, it's best to ask me, since I'm handling his schedule."
    hide ilian
    hide sara
    with moveoutright
    show pete at midright
    show helen at quarterright
    show baby boy at quarterrightbaby
    with moveinright    
    pavel "Pete is in charge of the library, so if you need to research something or print something out, head over there. He and his wife Helen are also experts on raising cattle, and will be starting a ranch up to the north."
    pavel "And, their baby, who was born on the shuttle, was the first human being to be born in space!"
    pete happy "Hey, y'all. Don't be strangers! I'll mostly be up at the ranch, but send me a message and I'll come down to the library if y'all need help."
    helen "Hi..."
    hide pete
    hide helen
    hide baby
    with moveoutright
    pavel "Next I want to introduce our farmers."
    show julia at midright
    show thuc at quarterright 
    with moveinright
    pavel "The Nguyens raise goats along with alfalfa and rice and some other crops. I'm sure their kids have names, but, honestly, I'm having trouble telling them all apart!"
    thuc "C'mon, there's only ten of them!"
    julia "We look forward to getting to know you all better."
    hide julia
    hide thuc
    with moveoutright
    show natalia at midright
    show martin at quarterright
    with moveinright
    pavel "The Peróns will be growing beans and corn, and are raising chickens and turkeys."
    martin "And also five children."
    natalia "Tomás is the oldest, and then there's Isabella, Raúl, Josephina, and Mateo."
    martin happy "Don't feel like you have to keep track of them all; that's my job!"
    hide natalia
    hide martin
    with moveoutright
    show her serious at midright with moveinright
    show him normal at quarterright with moveinright
    
    if (profession == "doctor"):
        pavel "[her_name] is our doctor. Don't wait until you're sick to stop by the clinic; go over and say hi sometime this week."
        her normal "Thanks, Mayor. I'll try and keep you all healthy!"
    elif (profession == "carpenter"):
        pavel "[her_name] is our carpenter. If you need something built, she's the one to ask."
        her normal "I work mainly with wood and fabric, and can print things with plastic, too."
    elif (profession == "mechanic"):
        pavel "[her_name] is our mechanic. When things break, she'll help get them working again!"
        her normal "But it's much easier if they don't break in the first place, so please treat your machines nicely!"
    elif (profession == "teacher"):
        pavel "Now, you kids ought to pay attention - I want to introduce the colony's teacher, [her_name]."
        her normal "Classes start next week, and I'm looking forward to meeting all you kids!"

    show her at quarterright with move
    show him at midright with move
    pavel "[his_name] knows a lot about growing vegetables and caring for horses and other animals, so be sure to ask him if you have questions in that area."
    him happy "I can't wait to get started!"
    
    hide her
    hide him
    with moveoutright
    pavel "Are there any questions?"
    menu pavel_meeting:
        "Do I have any questions?"
        "How much food do we have?":
            her surprised "How much food do we have in storage now?"
            pavel "We brought enough in our storehouse for everyone for two years. It will last much longer than that unopened, so I'd like to keep it for emergencies and use the food we grow as much as possible."
            jump pavel_meeting
        "What about medicine?":
            her surprised "What about medicine?"
            pavel "We have a good supply of the most common medicines, and Dr. Lily has the tools to synthesize new medicines if needed. But our supply is not unlimited, so try and use them sparingly."
            jump pavel_meeting
        "Do we have spare parts?":
            her surprised "Do we have spare parts for when things break?"
            pavel "We have the 3D printers at the library for spare parts, but we have a limited supply of plastic and metal, so let's make sure we recycle and use native materials where possible."
            jump pavel_meeting
        "Any weapons?":
            her surprised "Do we have any weapons?"
            pavel "We do have a few rifles and shotguns that you can check out from the storehouse if you would like to try your hand at hunting, though I'd check with Dr. Lily first and make sure that the animal is edible!"
            jump pavel_meeting
        "When is the colony ship coming?":
            her surprised "You said another ship is coming? Is that in two Earth years or Talaam years?"
            pavel "Good question; that's two Earth years, which makes about..."
            show lily at midright with moveinright
            lily "About 25 Talaam months. Since there are seven months a year here, that makes a little over three Talaam years."
            pavel "Right...hopefully that answers your question!"
            hide lily with moveoutright
            jump pavel_meeting
        "No questions.":
            "After the meeting, the mayor met with me to show me around where I'd work."

    call set_work_bg
    show pavel at quarterleft with moveinleft
    show her normal at midright with moveinleft
    play music "music/Isaiah.ogg" fadeout 1.0
    
    #Different event for each profession
    # DOCTOR
    if (profession == "doctor"):
        pavel "All right! This is the clinic where people will come in if they get sick. I don't just want us to react to injuries and illness, though - we need to be proactive, and help promote good health."
        her serious "I helped some people out on the ship on the way here, so this should be similar. I will need some more supplies, though."
        pavel "That's fine, just write up a list and give it to me to approve. Then you can go on over to the storehouse and take what you need."

    # CARPENTER
    elif (profession == "carpenter"):
        pavel "All right! This is the shop where people will come in if they need something made they can't make themselves."
        pavel "We don't have a lot of materials yet, but you can requisition some from the storehouse for important projects, and there are some materials, like wood, right here on the planet."
        her happy "I can see that this job is going to take a lot of ingenuity!"
        pavel "Yes, it will! Perhaps you can start by helping me out - one of the roof pieces from the Nguyen's house broke when we were unpacking it, so they are going to need a replacement."
        her normal "Sure, I'll take a look at the standard roofs and see if I can make something out of the wood around here."

    # MECHANIC
    elif (profession == "mechanic"):
        pavel "All right! This is the shop where people will bring machines that need to be fixed."
        pavel "You'll be responsible for any kind of machine people have, from datapads to tractors. We don't have many replacement parts, so do what you can to fix things up when they break."
        her concerned "I can see that this will take a lot of ingenuity."
        pavel "Yes, it will! Perhaps you can start by helping me with my datapad? It always freezes up when I try to access my calendar..."
        her normal "Sure, let me take a look at it..."

    # TEACHER
    elif (profession == "teacher"):
        pavel "All right! This is the schoolhouse. There's not a lot of kids in the community yet, so we just have them all in one room with you as their teacher."
        pavel "Please consider what they'll need to learn about Talaam in addition to the standard curriculum, and try to be flexible if kids are needed to help out back at home."
        her surprised "I guess the kids are going to have to work hard, too..."
        pavel "Yes, but they need to learn a lot, too! It will take a lot of effort to see that they don't forget about Earth, and all the things humanity has managed to learn there."
        her serious "Even though it seems far away, it's still our home, isn't it?"

    "I worked hard getting things set up, and even though the job seemed pretty big, I thought I would probably do okay."
    $ relaxed -= 5

    # Meet friend Sara
    scene bg community_center with fade
    "Afterwards, I stopped by the community center to see if [his_name] was done meeting with the other farmers. He wasn't, so I started talking with one of the people I had met on the ship."

    show her normal at midright
    show sara at midleft
    with dissolve
    sara "I guess you're not a farmer, either, huh?"
    her "Not really. I'm a [profession]."
    sara "Really? That's pretty cool."
    "We talked about my job for a while, and then she admitted,"
    sara sad "I'm not sure why I'm here...I'm not really good at anything."
    menu:
        "What should I say?"
        "That's not true!":
            her concerned "That's not true! I mean, I don't know you very well yet, but I can tell you're a good listener."
            sara "Thanks..."
        "Why are you here?":
            her surprised "Why {b}are{/b} you here?"
            sara "Well..."
        "(Change the subject.)":
            her surprised "(I don't know what to say!)"
            her normal "Well, uh, what do you like to do?"
            sara "I like to read...I read a lot. I'm a pretty good photographer, too."
            her normal "That sounds fun. Who's in your family??"
    show her normal
    show sara normal
    sara "My husband is Ilian Andrevski - he's not a farmer, either. He's a food scientist."
    her surprised "Really? There are food scientists?"
    sara "Yes, they study things like nutrition and shelf-life and ways to preserve foods while maintaining lots of nutrients - things like that. I think he'll also do a lot of the inventory and distribution of food."
    her normal "What about you? What's your job?"
    sara "Breeding stock."
    her surprised "What?!"
    sara "Ha ha ha, I'm just kidding! Though it does seem like we'll be expected to have lots of kids quickly to increase the population...but I'll be helping Ilian in the storehouse, and also helping the mayor stay organized."
    her normal "Good! I bet we'll see each other a lot, then."
    sara "Probably so. It's nice to have met you, [her_name]."
    "Sara and I talked almost every day after that. We had a lot in common as newlywed colonists, and she had an easy laugh and an understanding smile that made her fun to be around."
    return

# Emergency where she can't help everyone in time, leading to 
# the mayor offering to find her some help.
label work_1:
    $ times_worked += 1
    if (relaxed > 5):
        $ relaxed = 0
    else:
        $ relaxed -= 5
    $ community_level += 2

    call set_work_bg
    call play_scene_music("music/NoSilencePlease.ogg")

    # DOCTOR
    if (profession == "doctor"):
        show her normal at quarterright with dissolve
        "Usually things were pretty quiet at the clinic. I made an appointment with each colonist to learn about each person's medical conditions, and sometimes made suggestions for how to deal with chronic problems. We had a few minor injuries while setting up, but nothing serious."
        "But one day in particular was extremely busy."
        her surprised "Oh! What happened?"
        show him serious at left
        show pete at midleft
        with moveinleft
        "[his_name] carried Pete in and set him on the exam table. I could tell his leg was broken but he was not in immediate danger. I took his vitals while [his_name] filled me in."
        show her serious
        him serious "We were putting together a mill for grain. But one of the heavy cast iron rollers fell on Pete here. We tried not to move his leg while we carried him over."
        her serious "Good, thank you. You'll be all right, Pete."
        pete "Thanks, doc. Hurts like hell, though."
        him normal "I'll see you later, [her_name]."
        her normal "Hey, thanks for bringing him in."
        hide him with moveoutleft
        "The x-rays showed where his femur was crushed into several pieces."
        her serious "It's a comminuted fracture; it will take quite a while to heal."
        "I was just about to put him under so I could put in some pins when the radio crackled and I heard Sara."
        play bg_sfx "sfx/radio.mp3"
        "Sara on the radio" "Doctor! You've gotta come right away; one of the kids stopped breathing - I think he's choking!"
        "I started out the door while I talked to her on the radio. I hated to leave Pete alone, but this was urgent."
        hide her with moveoutleft
        scene bg path with fade
        show her serious at left with moveinleft
        her "I'm on my way. How old is he?"
        "Sara on the radio" "It's Van Nguyen, he's three!"
        show her serious at center with move
        her "Do you know how to do the Heimlich?"
        "Sara on the radio" "Yes! I mean, I've never done it before, but..."
        her yelling "Do it! Put your fist right above his belly button, support it with your other hand, and push in and up forcefully."
        show her serious at right with move
        "Sara on the radio" "She's doing what you said; it's not working!!"
        her serious "Hit him on the back between the shoulder blades! Don't give up!"
        hide her with moveoutright
        "Sara on the radio" "Hurry, [her_name], he's starting to turn blue!"

        scene bg farm_interior with fade
        show julia mad at midright with dissolve
        show sara sad at right with dissolve
        show van wince at center with dissolve
        show her serious at midleft with moveinleft
        if (skill_physical < 20):
            "By the time I got there, the little boy was unconscious."
            "I moved quickly. I could see something in the back of his mouth and was able to sweep it out with my finger. Mrs. Nguyen watched me grimly."
        else:
            "When I got there, he was blue but still conscious."
            "I moved quickly. I could see something in the back of his mouth and was able to sweep it out with my finger. Mrs. Nguyen watched me hopefully."
            
        play bg_sfx "sfx/cough.mp3"
        "Finally, he coughed and started to breathe."
        show sara normal
        show her normal
        show van normal
        with dissolve
        julia normal "Van! Oh, my boy!"
        "I didn't have time to stick around for adulation, though - Pete was still waiting for me to help his leg in the clinic."
        hide her with moveoutleft
        scene bg clinic with fade
        show pete at midleft with dissolve
        show her normal at midright with moveinleft
        her "Sorry to leave you waiting so long; I know you're hurting- oh!"
        show her surprised
        "I had bandaged up his leg, but the wound had reopened and he was bleeding a lot."
        pete "Doc, I tried to, to, stop the bleeding..."
        her serious "It's okay, I'm here now. You're going to be just fine..."
        "I took care of his leg, and several hours later, Pete woke up."
        pete "Hey, is Van okay?"
        her surprised "Van? Oh, yes, I got there just in time."
        pete "They really ought to have someone in here helping you out. I mean, what if you were in the middle of surgery or something?"
        show her normal
        menu:
            "Do I need help?"
            "I need help.":
                her "You are right...I can't do this by myself. I'll ask the mayor if there's someone that could assist me."
            "I can do it myself.":
                her "It's not a problem most of the time. I can handle it."

        scene black with fade
        "Word got around about my two close calls in one day."
        scene bg clinic with fade
        show her normal at midright with dissolve
        show pavel at quarterleft, behind her with moveinleft
        pavel sad "Doctor, I'm so sorry about what happened today."
        her serious "It's not your fault, Mayor Grayson."
        pavel normal "Well, it partly is my fault. It's obvious you need an assistant. Perhaps not full-time, but someone who can come quickly and help out during busy times."
        her normal "That would be helpful, actually."
        pavel "Well, I'll see who has some medical experience and get back to you about that."
        her "Thank you."

    # CARPENTER
    elif (profession == "carpenter"):
        show her normal at midright with dissolve
        "They kept me pretty busy making things for all the colonists. I made a lot of farm tools and fences, and started working on some woodworking tools. We didn't have a lot of metal, so I was trying to make tools out of local materials, but it wasn't going very well."
        "Today, however, I didn't have time for any of that. I was working on a roof for a chicken coop."
        show pavel at midleft, behind her with moveinleft
        pavel "[her_name], have you finished the barrels for the storehouse yet?"
        her serious "No, I thought you said you wouldn't need those for another week."
        pavel "Well, the Nguyen's carrots grew faster than they anticipated, and they need a place to put them."
        her "Well, I can start on them now, but the Perón's really wanted this roof for their chicken coop - they've already lost two chickens to some nighttime predator."
        pavel "I think the chicken coop takes priority here. But you're starting to have a lot of work to do, aren't you?"
        menu:
            "What should I say?"
            "Way too much.":
                her "I'm a little overwhelmed, honestly."
            "Sometimes.":
                her "Sometimes. It seems like when one person needs something right away, everyone else suddenly needs something, too."
            "No problem.":
                her "Nothing I can't handle."
        pavel "Well, I'll see if I can get someone that you can call on when you get a lot of work."
        her normal "That would be great, thanks."
        "Eventually, I got everything done, but I was looking forward to having some help sometimes."

    # MECHANIC
    elif (profession == "mechanic"):
        show her normal at midright with dissolve
        "Back on Earth, I only worked on cars. But here on Talaam, people brought me all kinds of machines to try and fix. If it had moving parts or electricity and it broke, it came to my shop."
        "Usually I could fix things pretty quickly, but after several months of hard farming, a lot of things were breaking down. It wouldn't have been so bad except that we had only a small reserve of spare parts, so I tried to only use them when there was no other way to fix things."
        show him normal at midleft with moveinleft
        him "Hey, [her_nickname], is the tractor fixed yet?"
        her concerned "No, sorry, I've been working on the clinic's radio all afternoon."
        him concerned "Oh..."
        her annoyed "..."
        her serious "I'll let you know when it's done."
        him serious "It just seems like tractors should be a pretty high priority, since that's how we're growing all the food we're going to live on."
        her "Yeah, but the clinic needs the radio in case someone on one of the farms is hurt. We don't have phones, and the computer pads are unreliable."
        him annoyed "Well, how long is it going to take?"
        menu:
            "A day or two.":
                her serious "Probably another day or two. Sorry, [his_nickname]."
                him serious "All right, well, maybe I'll just hitch Lettie up to the plow and see what she can do."
                her happy "Lettie can do anything!"
            "As long as it takes.":
                her annoyed "It'll take as long as it takes, okay? It depends on whether I can make it work without putting in a new belt."
                him serious "All right, I guess I'll just have to trust you."
                her normal "I'll get it done."
            "It'll go faster if you leave me alone.":
                her angry "It'll go faster if you leave me alone!"
                him angry "Okay! I'm leaving!"
                her "Good!"
                $ loved -= 2
        
        hide him
        show her annoyed with dissolve
        show pavel at midleft, behind her with moveinleft
        pavel "Everything all right in here?"
        her concerned "Yes, it's just a busy day."
        pavel "Are those all the things that need to be repaired?"
        her "Yes, I've got quite a backlog right now."
        pavel "Seems to me like you could use a little help sometimes."
        her normal "That'd be great, actually."
        hide pavel
        "It turned out that the radio just had a loose connection, so I soldered it back together, and then turned my attention to the tractor. I was able to get it fixed just before sundown. [his_name] would be happy, but it sure was a busy day for me. Hopefully the mayor would be able to find someone soon."
        
    # TEACHER
    elif (profession == "teacher"):
        show her normal at center with dissolve
        show raul at midleft
        show kid at midright
        play bg_sfx "sfx/kids.mp3"
        "Normally twenty-three students would be a nice size for a classroom. But my students are all different ages and skill levels. We have some good technology to help us out, but sometimes it's not enough..."
        her serious "On your computer pad you will see that I have sent each of you some reading about ancient Rome, appropriate for your skill level. Please read the selection, and then answer the questions at the end."
        "It took some of the kids five minutes, and others needed at least two hours. I decided to start a science experiment with the younger kids."
        her normal "We're going to make some different shapes out of paper, and see which ones will fly the best."
        "They all liked that idea, but the kids that were still reading didn't want to miss out on paper airplanes, so they ended up building those instead of doing their history work."

        scene bg path with fade
        show her serious at center
        show kid frown at quarterright        
        show van wince at midright
        with dissolve
        "At recess, one of the kids fell and got a bloody nose. While I was helping him, two of the teenage boys started arguing on the other side of the field."
        "One of them punched the other. Soon they were wrestling and rolling on the ground yelling. I ran to try to stop them."
        her yelling "Stop! Stop it, now!"
        "They kept fighting. The kid with the bloody nose was crying, some of the kids were screaming and some were chanting and jeering, and I was trying to pull them apart."
        play bg_sfx "sfx/punch.mp3"
        "One of the punches missed the kid and hit me in the head. I must have blacked out for a minute, because when I woke up the fight was over and all the kids were looking down at me worriedly."
        scene black with fade
        stop bg_sfx fadeout 1.0
        "I separated the two fighters, and somehow I managed to make it through the rest of that day. Just as the children were all leaving, the mayor came by."
        call set_work_bg
        show her concerned at midright with dissolve
        show pavel at midleft, behind her with moveinleft
        pavel sad "[her_name], are you all right?"
        her serious "Yes...though I may have a black eye tomorrow."
        pavel "That's terrible! You shouldn't be all by yourself here, not every day."
        her serious "Well, part of it is that Tomás really doesn't need to be here every day. He's old enough to do most of his work from home, and then he could help out his parents more, too."
        pavel normal "That may be a good idea, but I want to find someone to help you out on the days when you have all the kids here."
        menu:
            "Do I need help?"
            "I need help.":
                her concerned "You are right...I can't do this by myself."
                pavel "I'll see what I can do to find someone to help you out some of the time."
            "I can do it myself.":
                her serious "It's not a problem most of the time. I can handle it."
                pavel "I appreciate your confidence, but let me see if I can find someone, at least for part of the time."
        her normal "Thanks, Mayor Grayson."
        "That wasn't the only rough day, but it was the worst one for quite some time."
    return

# Introduce co-worker Brennan Callahan
label work_2:
    $ times_worked += 1
    $ relaxed -= 5
    call set_work_bg
    call play_scene_music
    show her normal at midright with dissolve
    "I was ready for another busy day at work when the mayor walked in with someone new. I remembered seeing him on the shuttle; he had an infectious smile and just the hint of an accent."
    show brennan at quarterleft with moveinleft
    show pavel at midleft behind her with moveinleft
    pavel "[her_name], I'd like you to meet Mr. Callahan. He's sort of a jack-of-all-trades here, helping out wherever we need it. He can help you out some of the time."
    show pavel at left, behind brennan
    show brennan at midleft
    with move
    # TODO: add bit o' slang in here.  CV? Or maybe we don't need it...
    brennan "Call me Brennan. And I know we've met already; I'd never forget a pretty face like yours."
    menu:
        "What should I say?"
        "Nice to meet you.":
            her happy "Nice to meet you, Brennan. It will be good to have some help sometimes."
            brennan happy "You're quite welcome."
        "I remember you, too.":
            her happy "Yes, I remember you too, Brennan. Thanks for agreeing to help out."
            brennan happy "You're quite welcome."
        "I'm more than just a pretty face.":
            her flirt "I'm more than just a pretty face, I hope."
            brennan happy "Of course! I just meant that I remembered you. But I could understand how you might not remember me."
        "Are you going to be helpful?":
            her annoyed "Do you have any talents besides flattery?"
            brennan happy "A few, to be sure! But don't worry; I'll try not to distract you too much."
    show her surprised
    "He winked at me playfully. Was he...flirting with me? I didn't have time to think about it; there was too much work to do."
    show her normal
    show brennan normal
    hide pavel with moveoutleft
    "It was nice to have him around, especially when things got busy later in the day. He didn't wait for me to ask him to do things, but he didn't get in my way, either."
    show brennan at center with move
    show her serious at quarterright with move
    brennan "It was a pleasure working with you today, [her_name]."
    "He looked into my eyes intently as he shook my hand. His gaze was direct, friendly, and...amused? I looked away."
    her normal "Thanks for your help today."
    brennan "Anytime."
    scene bg farm_interior with fade
    "I walked home, trying not to think about Brennan. When I got there, [his_name] greeted me with a kiss."    
    show him normal at midright with dissolve
    show her normal at midleft with moveinleft
    show him at center with move
    show him at midright with move
    him "How was work today?"
    menu:
        "What should I say?"
        "I got some help...":
            her happy "Great! I got some help - the mayor sent Brennan Callahan to help me out once in a while."
            him annoyed "Oh, well, that's good, I guess."
            her surprised "What, you don't think that's a good idea?"
            him serious "Well, I'm just a bit suspicious of Brennan. He comes on the shuttle at the last second with no special skills, no family, and nobody else seems to think that's unusual."
            her concerned "I guess they did ask mostly for couples and families to come..."
            him annoyed "He seems nice enough, but I'm just wondering what the real purpose is for him to be here."
            her surprised "You think he's a spy or something?"
            him serious "I'm not saying that. I'm just saying that there's unanswered questions here."
            her flirt "Interesting. Well, I'll keep an eye out, and if I see him sending coded messages to the aliens, I will let you know."
            scene black with fade
            "The next time Brennan helped out at work, he was as friendly as ever, but I didn't feel as uncomfortable as before. I treated him politely, but cooly, and we got a lot of work done."
        "Nothing special.":
            her serious "Just the usual. How about you?"
            him serious "Had to dig out some big boulders in the new field I'm working on."
            her normal "Oh, that sounds hard. Hungry for dinner?"
            him flirting "Oh yeah, I'm always hungry."
            her flirt "Ohh, that I believe!"

            $ loved -= 2
            $ relaxed -= 2
        "I have to work with someone obnoxious.":
            her annoyed "Ugh, the mayor wants me to work with Brennan Callahan."
            him surprised "Really? What's wrong with him?"
            her serious "I don't know, he's helpful enough, he's just kind of...creepy."
            him normal "Like in a 'secretly-a-vampire' kind of way, or a 'socially-inept' kind of way?"
            her concerned "Like in a flirting-with-a-married-woman kind of way."
            him serious "... He was flirting with you?"
            her serious "I don't know! Maybe? Or maybe he just acts that way with everyone."
            him annoyed "I don't know; I always thought it was a little strange how he came on the shuttle at the last minute, with no special skills and no family."
            her "I guess that is unusual."
            him surprised "Want me to talk to him?"
            menu:
                "Do I want him to talk to Brennan?"
                "No, I'll handle this.":
                    her serious "No thanks, I can handle him."
                    him annoyed "That's what I'm afraid of."
                    her annoyed "You know that's not what I meant! You're the only man I want to handle, silly."
                    him serious "I know, it's okay, I don't really want to have that conversation with him, anyway. But let me know if you do want me to help you out later, okay?"
                    her normal "Thanks, [his_nickname]."
                    call set_work_bg
                    show her normal at midright with dissolve
                    show brennan at midleft with dissolve
                    "The next time I saw Brennan, I thanked him for his help and mentioned that I expected everyone working there to maintain a professional attitude."
                    brennan "I'm sorry; I didn't mean to make you uncomfortable. Quite the opposite, actually."
                    her serious "Right. Now we've got work to do."
                    "Things went more smoothly after that, and we got a lot of work done."
                "Just \"talk\" to him.":
                    her concerned "By \"talk\" you mean \"speak words with\" not \"punch in the face\", right?"
                    him annoyed "Of course, what kind of barbarian do you think I am?"
                    her annoyed "I don't know, I was just making sure!"
                    "I didn't hear anything else about it, but the next time Brennan came to help, he acted much more professionally. That sure made things easier at work."
                "No, I'm probably imagining things.":
                    her normal "No, it's not the big of a deal. He's probably just a friendly kind of guy."
                    him annoyed "Friendly to women, you mean."
                    her flirt "Maybe, but, whatever. I'm not interested. I've got you!"
                    "The next time Brennan helped me out, he was friendly as ever, but I didn't feel as uncomfortable as before. I treated him politely but cooly, and work went well."

    return

# MONTH 9
# working hard
label work_3:
    $ times_worked += 1
    $ relaxed -= 2
    call set_work_bg
    call play_scene_music
    show her serious at midright with dissolve

    # DOCTOR 
    if (profession == "doctor"):
        "I worked hard all month. A new baby was born, a kid got his finger chopped off, and it looked like Mr. Perón might have cancer. In addition, we were monitoring the colonists' radiation and nutrient levels to try to keep them healthy."
        "The best thing about being a doctor here on the colony was not having to deal with insurance or payment or referrals. We logged everything carefully, but there was no bureaucracy and no money to keep track of."
        "Since there were only about 200 colonists, I was usually able to devote much more time to each patient than I had at the general practice where I worked before."
        "Although, sometimes it was awkward to do physical exams on people I saw all the time outside of work..."
        
        show brennan at quarterleft with dissolve
        "Brennan worked hard, too - he didn't have any formal medical training, but he learned to take vitals and log patients and fetch equipment for me."
        "It would have been impossible to do it all by myself."

    # CARPENTER
    elif (profession == "carpenter"):
        "I worked hard all month. Now that everyone was settling in, people had a lot of things they wanted. We made towels and spoons and a cradle and pots and other things."
        "The best part was having the freedom to make things the way we wanted. I didn't have to follow a pattern or follow the latest trends."
         
        show brennan at quarterleft with dissolve
        "Brennan worked hard, too - he had some woodworking skills, so he did a lot of that work so I could concentrate on other things."
        "Together we accomplished way more than I could have on my own. Even so, our task list never seemed to get any shorter."

    # MECHANIC
    elif (profession == "mechanic"):
        "I worked hard all month. People's datapads would get corrupted if they were left out during solar flares, the farm equipment needed maintenance, and sometimes homes' solar panels or stoves would break down."
        "Some critter kept chewing through the wires at the Jennings' farm, and so we were always going out there to replace those."
        "The best part was the lack of meetings and paperwork. I met with the mayor every so often, and logged all the work we did, but that's it."
        "If there was nothing going on, I'd just head home. If I was in the middle of something at dinnertime, I might take it home with me and work on it some more at night."
        "It was so freeing to be doing work for the sake of getting good things done, and not for the sake of a paycheck."
         
        show brennan at quarterleft with dissolve
        "Brennan worked hard, too - he didn't know much about electronics, but he could run wires and haul materials and use ordinary tools to care of the easier things."
        "We accomplished a lot more together than I could have on my own."

    # TEACHER
    elif (profession == "teacher"):
        show kid frown at center
        show raul at midleft
        show van at right
        with dissolve
        
        "I worked hard all month. We had to be a lot more flexible than at a regular school, as sometimes kids were absent if they were needed at home on the farm. I wrote up an entirely new curriculum customized for teaching all ages at once, so that all the kids could be studying the same topic but at their own level."
        "Some of my lessons were not as interesting to the kids as I hoped they'd be, but usually they went over pretty well. I felt like the kids were learning a lot."
        "The best part was really being able to concentrate on the students. I didn't have to administer any standardized tests or fill out long forms or go to staff meetings."
        "And I could teach what they really needed to learn and wanted to learn, not just what some committee thought they should learn."
         
        show brennan at quarterleft with moveinleft
        "Brennan worked hard, too - he didn't have any experience with teaching, but he was good with kids and helped keep them on task."
        "There were times when just having another adult around was so important."
        hide kid
        hide raul
        hide van
        with moveoutleft
    show her normal with dissolve
    her normal "Good work today, Brennan."
    brennan "Thanks, [her_name]. It's a pleasure working with you."
    menu:
        "What should I say?"
        "I enjoy working with you, too.":
            her "I like working with you too; you've been very helpful."
            brennan "I'm glad there's something useful I can do."
            her surprised "You weren't doing anything useful before?"
        "Tell me about yourself.":
            her surprised "Hey, I've been wondering, what brings you to the colony, anyway?"
        "Gotta go, bye.":
            her concerned "Thanks. Um, I gotta go."
            brennan "I'll see you tomorrow, [her_name]..."
            return

    $ brennan_relationship += 1
    brennan "It's true my skills aren't exactly in high demand here..."
    her surprised "What skills are those? What did you do back on Earth?"
    brennan "I was a salesman. Not a bad one, either."
    her normal "So why are you here?"
    brennan "I was too good at my job. It became my life; trying to sell more than last month, trying to beat the other fellows. Finally I had to ask myself what was the point of it all?"
    brennan "On a whim I applied to be a colonist, and I suppose there was something about me they liked, because I was accepted."
    her serious "That's strange..."
    brennan "What, you think it's strange they found something about me they liked?"
    her concerned "No, it's just - well, no offense, but we don't really need any salesmen here, especially ones with no family, and.... I'm sorry, that was rude of me--"
    brennan "And absolutely true. It feels lonely here, sometimes. There's no pubs or parks or any place to meet people - there's no one to meet! I don't even have my own pad or anything; they put me up in the Mayor's house."
    her serious "That sounds awkward."
    brennan "I have my own room, and he and his wife are nice enough, but they're not family."
    menu:
        "What should I say?"
        "Want to come over for dinner?":
            her normal "Not family, no, but you have friends here! Why don't you come have dinner with [his_name] and me tonight? I'm sure he'd like to meet you."
            brennan "Not very likely! You haven't seen the dirty looks he's been giving me?"
            her surprised "Really?"
            brennan "Oh, sure! He's always looking at me like I'm a ravenous wolf."
            her normal "Well, maybe we could go for lunch together sometime."
            brennan "I'd like that, [her_name]. Thank you, for being a friend."
        "(Give him a hug.)":
            show her serious at center with move
            her concerned "I'm sorry you're so alone..."
            "He didn't seem at all surprised when I reached out my arms to give him a hug. I didn't want him to feel left out...hopefully he could sense that."
            her concerned "(This is probably the first hug he's had in months... poor guy.)"
            brennan "Thank you, [her_name]. It helps having a friend like you."
        "We're all family.":
            her normal "We're all family here, right?"
            brennan "I suppose so, though you're the only one I feel close enough to to call family."
            her flirt "Sure, I'll be your big sister."
            brennan "Sister! Ha, that's...nice. Thank you, [her_name]."
    
    return

# MONTH 12
# Something bad happens - Brennan helps out.
label work_4:
    $ times_worked += 1
    if (relaxed > 10):
        $ relaxed = 5
    else:
        $ relaxed -= 5
    $ community_level += 2
    call play_scene_music("music/NoSilencePlease.ogg")
    call set_work_bg

    # Doctor - problems with new local bacteria (no viruses, though)
    if (profession == "doctor"):
        "There were not a lot of illnesses so far - they took great pains to make sure none of the colonists were carrying infectious diseases, and the viruses here probably hadn't had time to adapt to us yet."
        "But there were plenty of injuries, as people tried to adjust to new equipment, the different climate and atmosphere, and a new way of life."
        "Then, we met our first big challenge - the Streaks."
        "The first incidence was with one of the kids. Josephina fell down, got a scrape on her hand, and kept playing. The next day, the scrape was swollen and had red streaks all around it - like a child's drawing of the Sun."
        "Brennan and I cleaned out the wound and put a fresh bandage on it. We weren't too worried - it was a small scrape, and the kid was mostly acting fine."
        "But the next day, she came back. She had a fever and the wound wasn't healing well."
        show her normal at midleft with dissolve
        show brennan at midright with dissolve
        her serious "Take a culture sample; looks like a bacterial infection."
        brennan "Alright."
        "I borrowed a microscope from the science lab and examined the culture. It was like no bacteria I had ever seen, or any I could find in the database."
        her "Brennan, we need to quarantine the clinic. I'll send out a message to everyone urging them to stay away, wash wounds promptly, and watch out for these symptoms."
        "Would this bacteria respond to traditional antibiotics? They seemed to have cell walls, just like bacteria on Earth, so we decided to give it a try."
        scene bg clinic with fade
        show her normal at midleft
        show brennan mad at midright
        with dissolve
        "We stayed up all night with the girl, but the next day she was shaking, and her hand was starting to turn white around the cut. And now her brother was in the clinic with similar symptoms on his knee."
        show natalia at quarterright with moveinright
        "Their mother, Natalia Perón, ignored the quarantine and came to be with them in the clinic."
        natalia "You think a quarantine's going to stop me from being with Josephina and Raúl? Not this mama!"
        "Though the kids appreciated her presence, it also made everything take longer because she wanted me to explain everything we were doing."
        show her serious with dissolve
        "We continued treatment all that day, but the wounds still didn't seem to be improving. Instead, the infection appeared to be spreading."
        "We tried several antibiotic medications, but none had any effect on this strange organism. The girl complained of tingling in her hands and feet, which made me think the bacteria were attacking her spinal cord."
        show her serious at midright
        show brennan mad at midleft
        with dissolve
        
        menu:
            "What should we do?"
            "Ask Dr. Lily.":
                her "There's got to be something these bacteria are weak against. Maybe Dr. Lily can help."
                brennan "But what about the quarantine? You said you didn't want to risk the bacteria infecting anyone else in the colony."
                her concerned "We'll figure something out"
                
                her_c "Dr. Lily, do you have anything that might be helpful with fighting against local bacteria?"
                lily_c "Perhaps some of the fungi or algae here have evolved ways to fight against it?"
                her_c "Yes! Can you collect some samples and bring them to the clinic?  The Perón kids are here sick, and I don't want you to catch it."
                lily_c "I will bring anything that might help."
                nvl clear
                
                scene bg clinic with fade
                show her serious at midleft with dissolve
                show lily at midright with moveinright
                her surprised "What! No, don't come in! Now we'll have to quarantine you, too..."
                lily "You require my assistance. I am not concerned about being quarantined."
                her normal "Okay, well, thank you. Let's get started."
                "We tried a little bit of all the medicines and substances we had that we thought could possibly work. We tried different chemicals, local mold, algae - anything we could think of."
                "The hardest part was waiting around for the results, while the kids were suffering. Natalia and Brennan did their best to keep them comfortable and distracted."

                lily "Look at the algae culture; there's hardly any bacteria left."
                her concerned "Hopefully the algae itself wouldn't be harmful to people..."
                lily upset "I can't say for sure."
                call set_work_bg
                show her serious at midright
                show brennan at midleft
                with dissolve
                "We decided to try it. The kids just kept getting worse, and I was worried that if the bacteria spread further, it could do irreversible damage."
                "I monitored the kids' condition, but there was really nothing to do but wait... somehow, I must have fallen asleep."
            "Cut out bacteria.":
                her serious "We can't risk the bacteria spreading to vital systems. The antibiotics aren't working, and these kids' condition just keeps worsening. "
                brennan normal "What are you going to do?"
                her "I'm going to try to cut away the infected flesh to make it easier for the antibiotics to do their job."
                natalia "What?! Don't we have anything better?!"
                her "Honestly, I think this is the simplest option with the fewest side effects."
                natalia "... I supposed I'll have to trust you, then."
                brennan mad "Isn't that going to be painful?"
                her "That's why your job is to keep the kid immobilized and happy while I'm doing it."
                brennan normal "You have an awfully high opinion of my ability to keep people happy."
                her annoyed "I have local anaesthetics I can use; just help her not to be scared or wiggle around too much."
                "We told her what we were going to do, and then Brennan and Natalia held her so she wouldn't move. Brennan started telling her a story about faeries and flying mushrooms while I gave her the local anaesthetic."
                "I didn't want to take out healthy skin, but I wanted to leave as little bacteria as possible, so it was pretty tricky."
                "We treated the boy the same way, and then I was so exhausted I fell asleep at my desk."
            "Program nanobots.":
                her serious "We'll see if we can program our nanobots to hunt and destroy this type of bacteria."
                brennan "I hope you know how to do that."
                her concerned "I've worked with them a few times before. Basically, we will set them in leukocyte mode and give it a sample of the bacteria we want it to fight. It will then seek out and destroy those wherever it finds them."
                brennan mad "That sounds easy enough; why didn't we just try that in the first place?"
                her serious "Because we don't have built-in algorithms for this kind of bacteria. We have to train the nanobots, which takes time, and if they are not trained properly they can damage the body's own cells instead of just the bacteria."
                brennan normal "I'll leave you to it, then."
                natalia "Good luck, Doctor [her_name]."
                hide brennan with moveoutleft
                hide natalia with moveoutright
                "It took all day. The standard leukocyte programs ignored things they didn't recognize, like this alien bacteria, so I had to change their algorithms."
                "Brennan and Natalia did their best to keep the kids comfortable and distracted while I worked."
                "After several training passes, the highest accuracy I could get was 85\%. Hopefully their bodies could fight the rest of them on their own..."
                "I injected the nanobots into the two kids around 3am. I stayed up, monitoring their condition, making sure their bodies didn't reject the nanobots, and then I must have fallen asleep somehow."

        scene black with fade
        scene bg clinic with fade
        show her concerned at center
        "I awoke the next day in a hospital bed, disoriented. I was still in my clothes..."
        her surprised "The kids!"        
        "I rushed over to check on them. For the first time, the kids seemed a little better. I don't know if it was our crazy idea, or if the antibiotics were finally working, or both, but I was so relieved that we could help them."
        "Brennan had fallen asleep on another bed, snoring softly."
        show her normal
        "On my desk, my computer pad was full of messages from everyone asking about the kids and the quarantine. I looked for messages from [his_name]."
        him_c "Hey, [her_nickname], I haven't heard from you since the quarantine announcement...are you okay? I missed you today, but if anyone can help those kids, you can."
        if (loved >= 5):
            him_c "Starting to get a little worried here - any news?"
        if (loved >= 10):
            him_c "[her_name], I am seriously considering breaking my own leg so that they'll let me in there with you! You better still be alive in there!"
        nvl clear

        her happy "(He was so worried about me...)"
        $ loved += 2

        "There were other outbreaks of the Streaks, but now that we knew how to treat it, we didn't worry quite so much."

    # CARPENTER - running out of plastic & wood
    elif (profession == "carpenter"):
        show her normal at midright with dissolve
        "We made a lot of furniture and parts for the colonists - sometimes they made things on their own, but not everyone knew how. It was easier with the schematics we brought with us - the computer could easily cut complex shapes out of wood or metal, or print them out of plastic."
        "But..."
        show brennan at midleft with moveinleft
        brennan "Where's the two by fours? I wanted to start on those shelves for the school."
        her serious "That pile there is all we've got. The mayor said we're going to save the rest for emergencies."
        brennan mad "Well how do you like that! How are we supposed to build without materials?"
        her concerned "Well, there are plenty of trees by the river..."
        brennan "We're not lumberjacks!"
        her normal "No, but I have an idea."
        "We didn't have a sawmill yet (I think that was one of the things that was supposed to come on the next ship), so we needed to make do with what we had."
        her "Brennan, I need you to gather or saw off or whatever a bunch of small branches, as uniform in diameter as possible."
        brennan normal "You're the boss..."
        hide brennan with moveoutleft
        "While he was gone, I started drawing up some designs that used simpler materials. Instead of using big boards for the shelves, we could lash a bunch of medium-sized branches together."
        her serious "We'll still need some thick, long branches for the posts... and then how should we attach the shelves to the posts?"
        "I did some research and drew up some ideas when Brennan came back. He had a trailer full of branches, and he looked sweaty and miserable."
        show brennan at midleft with moveinleft
        brennan mad "I hope this is enough for you."
        her normal "That'll do... for today."
        brennan normal "Today! You're a slave driver, you are."
        if (brennan_relationship >= 1):
            her flirt "I have to be to get any work out of you, Your Laziness."
        her serious "Anyway, come see these plans. We'll need to strip the branches of twigs and leaves, and cut them to uniform sizes..."
        show brennan at center, behind her with move        
        "He stripped the branches while I attached them together. It took a few tries to attach everything so it was sturdy, and it wouldn't hold as much weight as a normal shelf, but in the end, we finished it."
        
        her concerned "I might have to have the mayor emphasize to people how much work it is to build this stuff, and maybe they won't ask for so many things."
        brennan "Or you could have them bring you the wood anytime they want you to make something."

        "I was going to have to do more research on ways to build with the wood we had here on Talaam."
        
    # MECHANIC
    elif (profession == "mechanic"):
        show her normal at midright with dissolve
        show brennan at midleft with dissolve
        her annoyed "This is the third one of these radios that has broken so far! I can't believe they sent such cheapo equipment on a space mission."
        brennan mad "I know; you'd think it might have occurred to them that we can't order new parts on a whim."
        her concerned "And they didn't send us with many variable resistors, either."
        brennan normal "There's plenty of these fixed resistors, though."
        her serious "Well, that doesn't do us much good, unless..."
        brennan "What?"
        her normal "Well, we could just use a fixed resistor instead and turn it into an on/off switch instead of a volume control."
        brennan mad "But then you couldn't control the volume."
        her "No, but it's better than running out of variable resistors that we might need for a more vital system somewhere."
        brennan normal "That's true..."
        her serious "Although, we do have some resistive tape; we could probably make our own...but it would be more bulky than the original."
        "We worked on making a small potentiometer out of resistive tape and metal rings, but we couldn't get it small enough to fit on the handheld radio. So we had to just remove the volume control. Our solutions weren't always ideal, but we did the best we could with the materials we had."

    # TEACHER a kid claims teacher hit them
    elif (profession == "teacher"):
        show her normal at midleft
        show brennan at midright
        with dissolve
        "It was the end of another school day. Even though the kids went home in the afternoon, I usually stayed around for another hour or two working on lesson plans and grading papers. Sometimes Brennan stayed and worked, too."
        "One day after school the Mayor came by to talk with me."
        show pavel at quarterleft, behind her with moveinleft
        show her at center
        show brennan at quarterright
        with move
        pavel "So, how are things going at the school?"
        her normal "Pretty good! I feel bad that the older kids have to spend so much time helping the younger kids, but it's really the only way to teach so many of different ages."
        pavel "That's good, that's good... Well, what I came to talk to you about, is that one of the parents came to me with a concern."
        her surprised "Oh?"
        pavel sad "They said that their child came up with red marks on their hands, and the child said you hit their hands with a ruler."
        her yelling "They said WHAT?!"
        brennan mad "[her_name]'ll be stern when the kids need it, but she's never hit anyone."
        pavel "This is news to you, then."
        her surprised "Of course it is! I would never do that. Which kid is it?"
        pavel "Gardenia Nguyen."
        her concerned "Gardenia... Well, a few days ago we were talking about how discipline in schools has changed, and how they used to hit kids that misbehaved with rulers or make fun of them, and how we don't do that anymore."
        brennan normal "I remember that. Then at recess, she was playing school with Josephina, and they were whacking each other's hands with sticks. They thought it was great fun."
        pavel "So, you think it was one of the other kids pretending to be a teacher?"
        her serious "That's the only thing I can think of."
        pavel normal "It sounds like this was just a misunderstanding. I'll talk to Gardenia's parents and let them know what happened."
        her normal "Thanks, Mayor Grayson. I wish they would have come to me about it, though."
        pavel "I'll tell them that, too. Good-bye, then."
        her "Good-bye."
        hide pavel with moveoutleft
        show her serious at midleft
        show brennan normal at midright
        with move
        her serious "Thanks for sticking up for me."
        brennan "Of course. I couldn't let cute little Gardenia get away with another one of her fibs."
        her annoyed "She certainly has a good imagination..."
        "Gardenia didn't give us any more trouble that month."

    return

# Month 15 - Solar flare while at work
label work_5:
    $ times_worked += 1
    $ relaxed -= 5
    call set_work_bg
    call play_scene_music

    if (skill_technical >= 30):
        "There were some days when we just had to stay inside because of strong solar flares. The prediction system I improved usually let us know a day or two ahead of time, so we could be prepared."
    else:
        "There were some days when we just had to stay inside because of strong solar flares. They had a prediction system that usually let us know an hour or two ahead of time, so we could be prepared."
    "But one day it didn't work..."

    show her normal at midright with dissolve
    show brennan normal at right with dissolve
    "It started as a normal day at work, when Dr. Lily's voice came over the radio."
    play bg_sfx "sfx/radio.mp3"
    show her surprised
    show brennan mad
    lily "Attention all colonists! This is Dr. Lily. A strong solar flare has just started. Get inside now. I repeat, there is a solar flare in progress, please get indoors."
    "The radio emitted a strong burst of static, and I could barely make out anything else she said."
    lily "...close the...stay...further notice..."
    show her serious
    "Our computer pads also popped up a notification from her."
    her surprised "That's strange; usually we have more warning than this."
    brennan "Hopefully everyone can get inside in time."
    show her serious
    show brennan normal
    "We closed the windows and turned off unecessary electronics."

    show martin at midleft with dissolve
    if (profession == "doctor"):
        "We only had one patient at the time; Mr. Perón was being treated for basal-cell carcinoma."
        "We had just cut a large tumor out of his face, and I was bandaging it up."
    elif (profession == "carpenter"):
        "There were just the three of us in the shop at the time - Brennan, me, and Mr. Perón, who had been explaining a farm tool he wanted us to try and make."
    elif (profession == "mechanic"):
        "Brennan and I had been watching Mr. Perón show us his method for twisting wire together to use the least amount of metal possible."
    elif (profession == "teacher"):
        "Other than that, I tried to teach class as usual. We had a guest speaker today, Mr. Perón, who was teaching the kids about chickens and how to breed and feed them, and what sort of plants they liked, and what they might eat that would make them sick."
        "He had just finished speaking and got ready to go when I stopped him."

    her serious "I'm afraid you're stuck here for awhile - Dr. Lily says there is a solar flare going on."
    martin "What? I haven't heard anything about that."
    her serious "They just announced it on the radio; I don't know why we didn't have an earlier warning this time."
    martin sad "I can't stay here! I have to make sure Natalia is safe!"
    her concerned "Please calm down. I'm sure your wife knows what to do."
    martin "Natalia always forgets to turn the radio on! She might not even know there is a flare! And Mateo is at home with her..."
    "I tried contacting his family on the radio, but either the radiation from the flare was interfering with our transmissions, or her radio was off. I couldn't connect my computer pad to the wireless network, either."
    play music "music/NoOneWillKnow.ogg" fadeout 1.0
    "Mr. Perón was getting more and more distraught. I was worried he was going to try and leave, and I wasn't sure I could stop him."
    show brennan at midright
    show her serious at right
    with move
    brennan mad "Calm down, please! Everything will be just fine."
    martin "You don't understand; you can't understand! If you had any family, you'd know that I have to be there!"
    "Brennan just looked at Mr. Perón, a curious expression on his face. Finally, he nodded."
    brennan normal "I'll go make sure everything's all right with your family."
    her surprised "You can't do that! The radiation is too strong!"
    brennan mad "But he's right. I don't have a family; I don't have special skills. I'm replaceable."
    if (is_pregnant):
        brennan "And you've got to protect your baby, so you can't go."
       
    $ grays_absorbed = 3
    menu:
        "What should I do?"
        "Try and stop him.":
            her yelling "It's not worth sacrificing yourself over!"
            brennan normal "I'll be fine. And if I'm not, well, at least I'll have done some good here."
        "Let him go.":
            her serious "If you really want to go, I won't stop you."
            brennan normal "Not that you could, anyway. But I'm glad you understand."
        "{i}Wear this blanket{/i}" if (profession == "doctor"):
            her serious "Here, at least put this over your head to shield you from some of the flare's rays. It won't completely protect you, but it's better than nothing."
            brennan happy "Thank you, [her_name]."
            $ grays_absorbed = 2

    hide brennan with moveoutleft
    show her serious at midright with move
    "I watched him leave. The weather was deceptively placid - bright sun, a cool breeze, tree branches waving... the deadly radiation was completely invisible."
    "Neither Mr. Perón or I talked; we couldn't do anything else, either; we were too nervous."
    show her concerned
    play bg_sfx "sfx/radio.mp3"
    "The radio crackled every ten minutes - we could just barely make out that it was Dr. Lily repeating her warning."
    "The second time she repeated her warning, the radio came on again just minutes later."
    play bg_sfx "sfx/radio.mp3"
    brennan "[her_name]...Perón house...got everyone inside...There was...but we...anyway. Repeat, we're...okay."
    show her normal
    show martin normal
    with dissolve
    "I let out a breath I hadn't realized I had been holding. Mr. Perón smiled and asked me to hand him the radio."
    martin "Thank you, Brennan. Earlier, what I said...well, I was wrong. You do have a family here."

    martin happy "You're part of ours."
    "There was silence, and static."
    brennan "...thank you."
    hide martin with moveoutleft

    if (profession == "doctor"):
        show brennan at midleft with moveinleft
        "The flare was over after a few more hours, and Mr. Perón brought Natalia and little Mateo to be treated for radiation sickness.  Afterwards, I insisted on Brennan being treated, too."
        her serious "You've absorbed at least [grays_absorbed] grays of radiation..."
        brennan happy "Grays of radiation? That makes it sound like I've got aliens living inside me."
        her annoyed "Stop joking and lie down. We need to see how bad it is."
        brennan mad "Hold on, I think I might--"
        "He vomited. At least most of it went on the floor..."
        her yelling "That's exactly what I'm talking about. Now lie down!"
        "The amount he was exposed to was more than is usually used in chemotherapy, but if he didn't get more exposure his body would probably heal it just fine."
        show her serious
        "I treated his burns and gave him some medicine, and warned him to be especially careful to avoid any radiation for the next few weeks while his body healed."
    else:
        "The flare was over after a few more hours, and Mr. Perón went home, but I insisted on Brennan going to the clinic."
        scene bg path with fade
        show her serious at midright
        show brennan mad at midleft
        with moveinleft
        "He threw up on the way there, and I could see some burns on his face and neck."
        hide her
        hide brennan
        with moveoutright

        scene bg clinic with fade
        show her serious at midright
        show brennan normal at midleft
        with moveinleft
        "The doctor treated his burns and gave him some medicine and said he would probably be fine, as long as he was extra careful to avoid any radiation exposure in the next few weeks."

    scene black with fade
    "I was impressed that he had risked himself for a family he wasn't particularly close to - but maybe it was that desire for closeness that led him to do such a thing in the first place."
    "It hadn't even occurred to me to go out in the solar flare to help Mr. Perón. Was that because I was more selfish, or just not as stupid? What if it was my family out there - would I have sacrificed my health to help them?"
    "It wasn't something I had ever had to think about before."

    return

# MONTH 18 - lunch with Brennan
label work_6:
    $ times_worked += 1
    $ relaxed -= 5
    call set_work_bg
    call play_scene_music

    if (profession == "doctor"):
        "The clinic wasn't very busy this month, so I'd been working on writing a paper about how the nutrition of crops planted here differed from the nutrition of crops grown in Earth soil, based on comparing my own blood samples."
        "The colonists would need supplements of some minerals that were not as abundant here."
        "But soon it was lunch time."
    elif (profession == "carpenter"):
        "We had the kids collect supple branches from the local trees, and we made wicker crates, baskets, and chairs out of them."
        "Brennan and I went to the school and taught some of the kids the weaving techniques we had learned."
        "Soon it was lunchtime, and the kids went home to eat."
    elif (profession == "mechanic"):
        "Inspired by the idea of replacing complicated parts with more simple ones, I set about looking at our inventory and cataloguing how parts we had a lot of could be used to substitute for parts we were running out of."
        "Soon it was lunch time."
    elif (profession == "teacher"):
        show her normal at midright
        show brennan at left        
        show kid frown at center
        show raul at midleft
        show van at right
        with dissolve
        her serious "Class, after you read your assigned section on nomads of the Great Steppe, please write about ways our colony is similar to and different from the nomad culture."
        her normal "Once you've done that, you can come over here and we will learn some wood carving techniques that they used to make and decorate their furnishings."
        "I tried to include a hands-on component to all our learning, even if sometimes it wasn't completely related."
        "Of course, most of the kids just dashed off a few sentences before coming to watch Brennan teach woodcarving, so I had to make some of them go back and work on it some more."
        "Soon it was lunchtime, and the kids went home to eat."
        hide kid
        hide raul
        hide van
        with moveoutleft

    show her normal at midright
    show brennan at midleft
    with move
    her concerned "Oh no, I forgot my lunch."
    brennan "I was just going to go home for lunch; do you want to join me?"
    her serious "No, it's okay, I can just walk home and get something."
    brennan mad "That's two klicks each way; you won't have any time to cook and eat anything."
    brennan normal "Come on, I'll fix you something. It's the least I can do for you, after all you've done for me."
    her concerned "Well..."
    menu:
        "What should I say?"
        "Yes.":
            her normal "Thank you, I'd appreciate that."
            scene bg farm_interior flip with fade
            show brennan normal at midright
            show her normal at midleft
            with moveinleft
            "We headed over to the mayor's house, which was as large as the Nguyens', with three bedrooms and a kitchen.  I guess that's why they had Brennan staying there, too."
            "Mr. and Mrs. Grayson weren't there today, though."
            "Brennan pulled out a frying pan and put some oil in it, and prepared some potatoes, cabbage, eggs and spices."
            her surprised "Do you like to cook?"
            brennan "Once in a while. Usually Mrs. Grayson cooks for all of us, but I'll take a turn sometimes, too."
            her normal "What are you making?"
            brennan "Just a little hash. Ordinarily, I'd add some sausage or bacon, but they're both in short supply these days."
            her happy "That sounds delicious! It's kind of a treat to have someone else cook for me..."
            brennan happy "[his_name] doesn't cook for you?"
            her normal "Oh, he does, sometimes, but we often end up just cooking together."
            brennan normal "You're lucky to have someone who loves you so much."
            menu:
                "What should I say?"
                "{i}I sure am.{/i}" if (loved >= 0):
                    $ relaxed += 2
                    $ loved += 2
                    her normal "I sure am...I don't know what I'd do without him."
                    brennan mad "..."
                    her flirt "But what about you! Aren't there any single women on the colony you could date? Or are you not interested in women?"
                    brennan happy "There's nothing I'm interested in more than women! But, well, let's see, single women...There's Dr. Lily, but she's at least 45 years old."
                    her surprised "Okay, she's really smart, and nice too, actually, but that is a lot older than you."
                    brennan normal "And then there's the Nguyen's oldest daughters, who are seventeen and sixteen."
                    her normal "I've seen them taking care of their little siblings, but I don't know them very well."
                    brennan "Well, the oldest, Joanna, is all over that Tomás fellow who's about her age. I'm surprised they're not married yet."
                    her surprised "They're only seventeen!"
                    brennan happy "Well, it's old enough to get into trouble, and old enough to help propagate the species..."
                    her flirt "What about the younger sister, Miranda?"
                    brennan mad "You're not seriously suggesting I try and date a child, are you?"
                    menu:
                        "What should I say?"
                        "Yeah, things are different here.":
                            her concerned "Normally, I wouldn't, but..."
                            brennan normal "But what?"
                            her serious "I want you to have a future here. I can tell you're lonely, and Miranda is old enough to make her own decisions."
                            her normal "I'm not saying you should sleep with her or anything, but in two years, she'll be an adult. Why not see if you can be friends, and then see what happens in the future?"
                            brennan "She is only eight years younger than me...But there's no way Mr. Nguyen would allow her to date such a creepy older man as myself."
                            her annoyed "Don't think of it as dating! And don't, like seduce her or anything. Just... see if you could be friends."
                            brennan normal "I'm not very good at being 'just friends' with women, [her_name]."
                            her normal "Well, you and I are just friends, right?"
                            brennan mad "... Of course."
                            her happy "Just like that, then."
                            brennan normal "Sure. Just like that."
                        "No, you should date Dr. Lily.":
                            her normal "No, I was just kidding. Actually, I think you should reconsider Dr. Lily."
                            brennan "Really? You don't think twenty years' age difference is too much?"
                            her serious "No way! I mean, she's attractive, right?"
                            brennan "Yeah, I suppose she does have a sort of sexy scientist sort of beauty..."
                            her flirt "And, you're not the type to be intimidated by a smart woman, right?"
                            brennan happy "You know I'm not."
                            her surprised "Well, then what do you have to lose?"
                            brennan mad "I just - she's old enough to be my mother, you know!"
                            her serious "She doesn't act like your mother!"
                            brennan normal "No, you're right... I should talk to her. There's no harm in trying, right?"
                            her concerned "The worst thing that could happen is she says she's not interested, and then it's awkward every time you see her for a while, and then you both forget about it."
                        "No, there's no hope for you.":
                            her normal "Of course not. But I didn't want to tell you to just give up."
                            brennan happy "You never know, perhaps we'll find some beautiful blue alien women out here somewhere. I could be Earth's ambassador, to teach them all about the strange and wonderful ways of the human species..."
                            her flirt "Keep dreaming, Brennan!"
                "I'm not so sure.":
                    her concerned "I used to think so, but I'm not so sure."
                    brennan "Why not?"
                    her sad "Things just aren't as exciting as they were when we were dating. I mean, we say 'I love you', but I don't feel it anymore. I don't think he does, either."
                    brennan mad "Bollocks. That's completely normal in a long-term relationship."
                    her surprised "Is it?"
                    brennan normal "Of course! But that doesn't mean you can't have any sparks of excitement. You just have to work a little harder."
                    her annoyed "Got any ideas?"
                    brennan happy "Hundreds! Like, when you're at dinner, play a little footsie under the table, or give him a little spank when he walks by, or go to bed naked, or grab his--"
                    her surprised "Whoa! That's enough!"
                    brennan normal "I've got plenty more..."
                    her concerned "It's kind of weird to have you telling me to get naked for my husband..."
                    brennan mad "Well, no one else is telling you, and you need to hear it!"
                    her serious "Brennan, you really don't have to-"
                    brennan normal "Also, you should wake him up once in a while with steamy hot kisses, never mind how bad your breath may smell in the morning."
                    brennan "And you should work together! When you've got a job to do, ask him to help you, or help him out. Find something he likes and surprise him with it. Make his favorite food!"
                    brennan mad "I mean, for crying out loud, [her_name], don't you realize how lucky you are just to have someone?!"
                    her concerned "..."
                        
                "{i}He doesn't love me.{/i}" if (loved <= -5):
                    $ loved -= 2
                    her sad "I don't think he loves me at all."
                    brennan mad "What?! Why do you say that?"
                    menu:
                        "What should I say?"
                        "He doesn't tell me.":
                            her sad "He never says 'I love you'"
                            brennan normal "Well, he should. How could he look at you every single day and not say 'I love you'? I'm sure I would."
                            her surprised "Would what?"
                            brennan happy "I, ah, well-- He's an arse, that's all I'm saying."
                        "We never make love.":
                            her sad "It seems like we never make love anymore..."
                            brennan normal "Is he gay? Impotent?"
                            her surprised "What?! No!"
                            brennan mad "Well, then, what's his problem?! Who could be married to you, and not want to show you some love every day?"
                            her concerned "I don't know; it just seems like we're always too tired or too busy by the time we go to bed."
                            brennan normal "Well, how about first thing in the morning? Or right before dinner? Or when you come home for a quick lunch break?"
                            her normal "Ha ha, that's not a bad idea. We'd probably feel like it more, then."
                            brennan mad "I mean, don't you two realize how lucky you are to have each other?!"
                            her concerned "..."
                        "I'm not good enough.":
                            her sad "I'm no good at living here; I'm not tough or hard-working enough."
                            brennan normal "What?! That's not true at all; we'd be totally lost without you as our [profession]."
                            her concerned "But I'm no farmer. I hate farm food; I don't want to work hard all day; I don't want to have to do without. I just want to go to a store and buy food and soap and have hot water!"
                            brennan "It sounds like [his_name] isn't the problem."
                            her concerned "Maybe not. But he loves it here. I just... don't."
                            brennan mad "Do you love him enough to stay here with him?"
                            her sad "I don't know..."
                            brennan normal "If you want out, we could leave the planet on the next colony ship. It'll be a few months, but you don't have to stay here if you're miserable."
                            her surprised "Brennan..."
                        "Things aren't exciting.":
                            her concerned "I don't know; it's just not the same as it was when we first got married."
                            brennan normal "Of course not. Nothing exciting can last forever, or it wouldn't be exciting any more, would it?"
                            her sad "But if I don't feel the love, then..."
                            brennan "That's not the only way to feel love, right? You care about each other, want the other person to be happy?"
                            her concerned "I used to..."
                            brennan mad "Do you love him enough to try and make things better?"
                            her serious "I don't know..."
                            brennan normal "Because if you want out, we could leave the planet on the next colony ship. It'll be a few months, but you don't have to stay here if you're miserable."
                            her surprised "Brennan..."

            show her surprised
            "Suddenly I noticed an acrid smell..."
            brennan mad "The hash!"
            show her normal
            show brennan normal
            "Luckily, it wasn't burned too badly, and we ate it together as the conversation turned to other topics."
            brennan "You know that I'm always here for you, right?"
            her normal "Yeah, thanks for listening."
            if (brennan_relationship >= 1):
                brennan "You helped me when I was feeling worthless; I'd do the same for you."
                her concerned "I--"
                brennan mad "I don't want you to ever feel trapped, like no one loves you or you have nowhere to go, because it's not true."
                her normal "Thanks, Brennan..."
            $ brennan_relationship += 1

        "No.":
            her normal "No, thank you. But if you would cover for me in case I get back late, I'd appreciate that."
            brennan "Of course."
            scene bg farm_interior with fade
            show him normal at midright with dissolve
            show her normal at midleft with moveinleft
            "I had to rush at home, and only had time to eat some raw vegetables before it was time to walk back."
            "But I didn't mind too much, as I got to see [his_name] while I was at home."
            him normal "I'll walk halfway with you; I don't usually get to see you during the day."
            her "Sure!"
            scene bg path with fade
            show him normal at midright
            show her normal at midleft
            "We talked and laughed together. [his_name] was going way out of his way, using up the energy he needed for farming...just to be with me."
            "I held his hand tight, and he squeezed back. We didn't need to say anything; he knew I appreciated him, and I knew he appreciated me, too."
            $ loved += 5
            return
        "{i}Let's join Sara.{/i}" if (skill_social >= 30):
            her surprised "Hey, do you mind if I invite Sara, too? Sometimes we like to have lunch together."
            brennan "No, that's - that would be fine. I'll cook up something for the three of us."
            scene bg farm_interior flip with fade
            show sara at right
            show her normal at midright
            show brennan at midleft
            with moveinleft
            "We all went over to the Grayson's house where Brennan lived. He fried up some potatoes and cabbage and eggs for us, and we talked and laughed all together."
            her surprised "Oh! It's been almost an hour; we should get back to work!"
            show her happy with dissolve            
            sara "Thanks for lunch, Brennan. We should do this again sometime."
            brennan happy "It was my pleasure to entertain you."
            $ brennan_relationship += 1
    return

# MONTH 21
# Brennan is government spy looking for lucrative resources. 
# People find out about past crimes; chance for redemption or execution?
# has quantum entanglement communicator for instantaneous communication with Earth
label work_7:
    $ times_worked += 1
    $ relaxed -= 5

    call set_work_bg
    call play_scene_music

    $ has_batteries = False
    $ questioned_brennan = False
    $ searched_room = False
    show her normal at midright with dissolve
    show brennan at midleft with moveinleft

    "One day while we were cleaning up after work, Brennan came up to me."
    brennan normal "[her_name], can I ask a favor of you?"
    her flirt "You can ask..."
    brennan mad "I need batteries."
    her surprised "Can't you just get them from the storehouse?"
    brennan normal "Normally I would, but... I've used my quota already. It's been so cloudy lately, you know, the solar panels just haven't been keeping up."
    her concerned "What do you need them for?"
    brennan happy "Just some electronics in my room."
    menu:
        "What should I say?"
        "Sure.":
            her normal "Sure, Brennan, I'll get some for you."
            brennan normal "Thanks so much. And, ah, I'd appreciate it if you didn't mention to Ilian that they're for me."
            menu investigate_brennan:
                "What should I do?"
                "Question Brennan further." if (not questioned_brennan):
                    if (has_batteries):
                        call set_work_bg
                        show her normal at midright
                        show brennan normal at midleft
                        with dissolve
                    $ questioned_brennan = True
                    her surprised "So, what kind of electronics do you have that are using so much power?"
                    brennan "You know, razor, computer pad, blow dryer, that sort of thing."
                    if ((skill_technical >= 60) or (profession == "mechanic")):
                        her annoyed "Blow dryers don't even work here, they draw too much current."
                    elif ((skill_spiritual >= 60) or (skill_social >= 60)):
                        her sad "You aren't being completely honest with me."
                    else:
                        her surprised "Really? That's strange..."

                    if (brennan_relationship >= 2):
                        brennan happy "Oh, [her_name], I should have known I couldn't hide anything from you."
                        brennan normal "It's easier if I just show you. Come with me."
                        scene bg farm_interior flip with fade
                        show her normal at midleft
                        show brennan normal at midright
                        with moveinleft
                        "We walked over to his room at the Graysons'. He pointed to an electronics box under the table."
                        jump brennan_confess
                    else:
                        brennan "You're right, of course, but I can't tell you what they're really for. Can you just trust me?"
                        jump investigate_brennan
                "Go to the store house." if (not has_batteries):
                    scene bg storehouse with fade
                    show ilian happy at midright with dissolve
                    show her normal at midleft with moveinleft
                    "I headed over to the store house and asked Ilian for the batteries. I hadn't gone over quota, so there was no problem."
                    $ has_batteries = True
                    menu:
                        "What should I do?"
                        "Question Ilian.":
                            her surprised "Hey, Ilian, do you know what Brennan needs all these batteries for?"
                            ilian normal "Wait, these are for Brennan?!"
                            her serious "Yeah, he asked me to get them for him."
                            ilian "He's already five sets over his quota! He needs to learn to do without!"
                            her surprised "Do you know what they are for?"
                            ilian "What does everyone use batteries for? Lights, computers, things around the house. They're not supposed to wear out so fast when they're charged properly."
                            her serious "Hmmm, okay, thanks."
                            ilian "What about the batteries?!"
                            her normal "I might need them."
                            ilian "Gahhh..."
                        "Leave.":
                            "I left with the batteries."
                    call set_work_bg
                    show her normal at midright with dissolve
                    show brennan at midleft with moveinleft
                    jump investigate_brennan
                "Search Brennan's room" if (not searched_room):
                    $ searched_room = True
                    "Something wasn't right here. I sensed Brennan was hiding something important from me, and I was determined to find out what it was."
                    "Since he said he needed the batteries for his room, I thought I would check there."
                    scene bg farm_interior flip with fade
                    show her normal at quarterright with moveinleft
                    "No one was home at the Grayson's house, but there were also no locks on the doors, so I just walked in."
                    her "(Brennan will be at work for a little bit longer, if he's waiting for me to bring him the batteries...)"
                    hide her with moveoutright
                    scene bg bedroom
                    show her normal at quarterright with moveinleft
                    "His room had the same few pieces of shuttle furniture we had, with a sleeping bag on the floor and a seat and table in the corner. The walls were bare; there were no photos or posters or decorations at all."
                    "The table had a mess kit and a cable for charging a computer pad. There was another cable, too, though, and when I followed it, it went underneath the table where there was a strange device."
                    "It looked a little bit like a computer, with a metal case and some LEDs lighting up every now and then. But there was no writing or labels on the case at all. It made a low humming noise."
                    her surprised "What is that?"
                    show brennan mad at left with moveinleft
                    "Suddenly, I heard footsteps and I jumped. Brennan was in the doorway, watching me."
                    her concerned "I was just, ah, well..."
                    "He entered the room, closing the door behind him."
                    show brennan mad at midleft with move
                    jump brennan_confess
                    
                "Give him the batteries." if has_batteries:
                    call set_work_bg
                    show her normal at midright
                    show brennan at midleft
                    with dissolve

                    "I brought the batteries back to Brennan."
                    brennan happy "Thank you so much, [her_name]. I'm completely in your debt."
                    her concerned "You're welcome..."
                    return

        "No, sorry.":
            her serious "I'm sorry; I can't do that for you, Brennan."
            brennan normal "Please, [her_name]. I wouldn't ask you unless it was really important."
            menu:
                "What should I say?"
                "I'll see what I can do.":
                    jump investigate_brennan
                "No.":
                    her "Sorry, Brennan, I won't do that."
                    brennan mad "Oh...well, I'll just make do without, then, I suppose."
                    her concerned "Yeah, that's something we've all had to do, isn't it?"
                    return
    return

label brennan_confess:
    $ discovered_qec = True
    brennan normal "It's a quantum entanglement communicator."
    her concerned "Okay, but what does it do and why do you have one?"
    brennan "I use it to send messages with Earth, instantly."
    her surprised "Instantly?! Faster than light speed - I thought that was impossible!"
    brennan "The technology's quite new and expensive - this is a prototype, actually. Part of my job here was to test it."
    her annoyed "And the other part?"
    "He looked away and paused for a second before answering."
    brennan mad "I'm to report on any resources this planet has that my...employer might find profitable."
    her "Who is your employer?"
    brennan mad "Rare Earth Tech. Well, I'm technically an independent contractor for Senator Martínez, who happens to be both on the board of R.E.T. and on the Senate Energy Committee."
    her serious "So you're a spy, basically."
    brennan normal "You could look at it that way."
    her annoyed "Since you've kept your employment a secret, I don't see any other way I can look at it."
    her angry "How could you hide this technology? People could have been using this to talk to their families back on Earth!"
    brennan "That's just it - there's not enough bandwidth for that. I can only send small bits of text at a time - like a telegraph. And besides, when I first came here we weren't even sure it would work."
    her surprised "So why did you need the extra batteries?"
    brennan mad "If it ever turns off, even for a second, the connection will be broken and I'll completely lose contact."
    if (brennan_relationship >= 1):
        her sad "What else are you hiding? Were you ever even a salesman, like you said?"
        brennan normal "I never lied to you, [her_name]. But I hope you'll understand why I never told you about this."

    her flirt "So, is this the part where you turn into an evil villain and kill me because I know too much?"
    brennan normal "Kill you?! Of course not. This is the part where I beg for mercy and ask you not to tell anyone else about my device here."
    menu:
        "What should I say?"
        "I won't tell.":
            her serious "I won't tell anyone. You're not hurting anyone, and..."
            brennan "And what?"
            if (brennan_relationship >= 2):
                her concerned "I'm afraid of what they'd do to you."
                brennan happy "That's much too sweet of you, [her_name]."
            else:
                her concerned "I'm not sure if everyone else would be as understanding as I am."
                brennan "That's true. Well, I trust you to keep it a secret. Thank you."
            her serious "But there is one more thing..."
            brennan "Oh? What's that?"
            jump wants_from_brennan
        "They have a right to know.":
            her angry "The colony has a right to know, and a right to be able to use the device."
            her serious "Like you said, we'll need some kind of priority system and limits on messages, etc, but it's not fair for only one person to be able to communicate with Earth like that."
            brennan mad "I suppose I can't stop you."
            her annoyed "..."
            brennan normal "...Do you think they'll forgive me?"
            her serious "We'll see."
            "Brennan and I worked out a proposed system where colonists could take turns giving him a short message to send. Then we told the colony about the device."
            scene bg community_center with fade
            show brennan mad at midleft
            show him angry at midright
            with dissolve
            him angry "I knew we couldn't trust him!"
            hide him
            show julia mad at right with dissolve
            julia mad "How could such a dishonest spy care about our colony?"
            hide julia
            show martin sad at midright with dissolve
            martin "I don't agree with his secret keeping, but Brennan does care about the colony - he saved Natalia and the kids from the solar flare."
            show natalia at right with dissolve
            natalia "Or he was just doing that so you wouldn't suspect him!"
            hide natalia
            hide martin
            show pete at left with dissolve
            pete "Yeah, there's no way we can trust him after this!"
            show him annoyed at quarterright
            him annoyed "Not that we trusted him much before..."
            show her serious at right
            her annoyed "I agree with you, but you're missing the most important piece of information here."
            show julia at center with dissolve
            julia "And what is that?"
            her serious "We can send messages to Earth instantaneously! No more waiting four years for your families to get your messages, and another four years for them to write back!"
            hide julia
            show sara at center with dissolve
            sara sad "My family is going through a lot right now... at least, they were four years ago. Being able to write back and forth to them will help me so much."
            show pete at left with dissolve
            pete "..."
            him concerned "..."
            her serious "I'm not asking you to trust Brennan. But can you forgive him enough to let him keep his place here?"
            brennan normal "I always hoped that the QEC would work well enough that eventually you could all use it... but they wanted to keep it a secret. Now that the secret's out, they have decided to let you all use it."
            pete "I don't think you got a choice, right?"
            brennan mad "Even if you stole the device from me, they could simply turn off their receiver, or refuse to pass on your messages. It might be better to retain their goodwill."
            hide sara 
            show julia normal at center with dissolve
            julia "How shall we do that?"
            brennan normal "By not treating me like a criminal."
            scene black with fade
            "In the end everyone agreed, but even though they were nice to him on the surface, I think Mr. Perón and I were the only ones that trusted him at all."
            
            $ exposed_brennan = True
        "I won't tell if...":
            her "I won't tell if you promise to-"
            menu wants_from_brennan:
                "What should I say?"
                "Get me off this planet.":
                    her sad "Promise to get me off this planet with the next colony ship. I know I promised to stay forever, but you have connections, you could help me."
                    brennan normal "Of course I'll help you. Just leave it to me."
                    $ wants_to_leave = True
                "Send a message for me.":
                    her concerned "Promise to send some messages to Earth for me."
                    brennan normal "Of course, I'll do what I can."
                    brennan "Thank you, [her_name]. I trust you to keep it a secret."
                "{i}Kiss me.{/i}" if ((brennan_relationship >= 2) and (loved <= 5)):
                    her serious "Kiss me. Now."
                    "What was I saying? What was I doing? I thought he was going to laugh, and I could pretend it was a joke, but then he stepped closer."
                    show brennan normal at center with move                    
                    "My heart raced and my mind shut down as there were no more words, just flesh melting into flesh with all the passion we had been holding back."
                    scene black with fade
                    play bg_sfx "sfx/cloth.mp3"
                    "I didn't think, didn't analyze, didn't worry about [his_name]; I just existed, in that eternal moment of pleasure and mutual acceptance."
                    "Afterwards, we didn't say anything. I just went home, and for a while we pretended nothing had happened..."
                    if (loved < 0):
                        $ loved -= 10
                    else:
                        $ loved = -10
                    $ cheated_on_him = True
                    $ relaxed -= 5
                "You owe me one.":
                    her flirt "Never mind, just... keep in mind that you owe me one."
                    brennan normal "I owe you much more than that. Thank you, [her_name]."
    return

# MONTH 24 Someone at work you can't help.
# Brennan says he's leaving, do you want to come
label work_8:
    $ times_worked += 1
    $ relaxed -= 2

    call set_work_bg
    show her normal at midright with dissolve
    call play_scene_music("music/You.ogg")

    "Most days I was able to help everyone with what they needed."
    "But not every day was a success."
    if (profession == "doctor"):
        # Someone has chronic pain (fibromyalgia?), don't know why
        show julia at midleft with moveinleft
        julia "The medicine you prescribed for me last time we met was completely ineffective."
        her surprised "Really?"
        julia "Yes, I'm still having pain all over, especially in my joints."
        her serious "Well, if the ibuprofen was not effective, it's probably not arthritis..."
        julia mad "Obviously."
        her annoyed "Well, let's try something else, then."
        julia "How shall we do that, if you don't know what is causing the pain? Shall I simply try every single drug available, and see what works?"
        her annoyed "Of course not. We started with the most probable cause, and we will work down from there."
        julia normal "How long is this list of \"probable causes\"?"
        her serious "Well, there's lots of things that can cause joint pain. Infections, cancer, fibromyalgia, depressive disorders--"
        julia mad "Enough. I won't subject my body to any more of your theories."
        her annoyed "Look, the tests were inconclusive. The only way we'll know is by trying some different treatments!"
        julia normal "My apologies for wasting your time. Goodbye, Dr. [her_name]."
        hide julia with moveoutleft
        her sad "..."
        show brennan at midleft with moveinleft
        brennan "Now there's a face that could turn wine to vinegar. What'd you say to her, [her_name]?"
        her concerned "She doesn't think I can help her... and she may not be wrong."
        brennan "Well, at least you're willing to give it a try!"
        her sad "She wants me to just do some magic and make it all better, but it doesn't work like that."
        brennan mad "Don't blame yourself. You can't help a crocodile with a toothache."
        her "But isn't that my job? Why am I here if I can't even help one person feel better?"
        brennan normal "Ah, sometimes I wonder the same thing."        

    elif (profession == "carpenter"):
        # Someone needs glasses; can't grind glass precisely enough
        show natalia at midleft with moveinleft
        natalia "I hope you can do something for Raúl..."
        her surprised "What is it?"
        natalia "He needs glasses. All this time we thought he was just a slow reader, but the doctor says it's his vision that's the problem."
        her normal "That would make it hard to read, wouldn't it?"
        her serious "But shouldn't the doctor have something that can help Raúl?"
        natalia "None of the glasses at the clinic worked. I brought over the closest ones, and the doctor wrote a prescription. Here it is."
        her serious "Hmmm, astigmatism, I see. Well, I'll see what I can make for him."
        natalia "Thank you, [her_name]. You always do such a nice job on everything you make, I'm sure you'll be able to help Raúl."
        hide natalia with moveoutleft
        show brennan normal at midleft with moveinleft
        brennan "We're making glasses, now?"
        her concerned "I don't see how we can... I don't have tools for grinding glass precisely. And we don't have any lenses in the shape he needs."
        brennan "I'm guessing contacts are out?"
        her serious "Yeah, even if we could trust a six-year-old with contacts, we don't have any way to make those in the right shape, either."
        brennan mad "So what are you going to do?"
        her concerned "I don't know."
        brennan normal "This was bound to happen eventually. We don't have every tool ever invented."
        her sad "They're counting on me... but I can't help them..."
        brennan mad "Don't blame yourself! They'll just have to make do with the lenses we have."
        her serious "I guess they will..."
        brennan normal "Honestly, we've done well to have built as much as we have."

    elif (profession == "mechanic"):
        # Can't fix someone's tractor/solar panels/hearing aid?
        show natalia at midleft with moveinleft
        natalia "[her_name], I don't know if there's anything you can do, but one of the kids' computer pads won't turn on."
        her surprised "What happened to it?"
        natalia "I think Raúl left it out during one of the solar flares..."
        her annoyed "(Again?! This is the fifth time she's brought Raúl's computer pad in for repairs!)"
        her serious "OK, I'll take a look at it."
        hide natalia with moveoutleft
        "I opened it up and got out my multimeter. Some of the circuits were completely fried."
        show brennan normal at midleft with moveinleft
        brennan "That doesn't look good."
        her concerned "No, it's totally fried."
        brennan normal "You can't fix it?"
        her annoyed "These are specialized electronics components; I can't just get a new piece off the shelf and solder it in."
        brennan "Perhaps this'll teach that naughty little tyke to take better care of things."
        her sad "Yeah..."
        brennan mad "Hey, don't blame yourself! It was bound to happen eventually."
        her concerned "I still feel like I'm letting them down."
        brennan normal "Honestly, we've done well to have fixed as much as we have."
        
    elif (profession == "teacher"):
        # Trouble with student
        show kid frown at midleft with dissolve
        "I had been having some trouble with one of the students, Gardenia. I asked her to stay after school so I could talk to her about her paper."
        "Gardenia" "Who cares if the letter's written the wrong way? You can tell what letter it is!"
        her normal "But it doesn't look right, and it will make it harder to learn cursive later."
        "Gardenia" "Why do I even need to learn cursive?! Everyone just types on the computer!"
        her serious "Sometimes you still need to write things by hand. And people will need to be able to read what you write-"
        "Gardenia" "People can read what I write!"
        her annoyed "Let me finish. People will need to be able to read what you write quickly, not after analyzing it for an hour."
        "Gardenia" "Well, I'm not doing it over."
        her angry "Yes you will! You'll sit here until you've written every letter correctly!"
        show brennan at right with moveinright
        "Gardenia" "No, I won't."
        hide kid with moveoutleft
        "She got up and walked out of the school. I started to follow her, but Brennan stopped me."
        brennan normal "I'll go talk with her."
        her sad "Go for it, I'm obviously useless here."
        hide brennan with moveoutleft
        "Brennan got along much better with Gardenia than I did. In a few minutes she was smiling and rewriting her paper."
        "She handed it to him, glared at me, and went home."
        show brennan at midleft with moveinleft
        her concerned "Thanks, Brennan."
        brennan normal "Hey, don't blame yourself. That one's a little spitfire."
        her sad "Yeah, but that doesn't excuse me yelling at her. I shouldn't have lost my temper."
        brennan "Honestly, I'm impressed you've done as well as you have. It's tough to teach so many different ages all at once."

    her surprised "We've been working here three years, now, haven't we?"
    brennan normal "Three years? Isn't it two?"
    her normal "Oh, I meant three Talaam years. That's probably about two Earth years."
    brennan mad "I can't get used to the different time measurements here - no matter how this planet rotates, I can't call seven months a year."
    if (wants_to_leave):
        her concerned "I know what you mean. This place still doesn't feel like home."
    else:
        her normal "Yeah, it is kind of weird. But I think I'm getting used to things here."

    brennan normal "At least I won't have to deal with it much longer."

    if (wants_to_leave or cheated_on_him):
        her serious "Because you're going back to Earth."
        brennan "Yes. You're coming too, right?"
        her concerned "I don't know..."
        brennan mad "What?! Why would you want to stay?!"
        menu:
            "What should I say?"
            "{i}They need me here.{/i}" if (community_level >= COMMUNITY_LEVEL_OK):
                her concerned "They need me here. There's no one else that is as good of a [profession] as I am."
                $ community_level += 5
            "{i}I love the people here.{/i}" if (skill_social >= 50):
                her normal "I love the people here. They feel like family."
                $ community_level += 5
            "{i}I love [his_name].{/i}" if (loved >= 0):
                her concerned "I love [his_name] too much to leave him behind."
                $ loved += 2
            "Actually, I don't want to stay.":
                $ wants_to_leave = True
                her annoyed "Actually, I don't want to stay here. This is my last chance to leave it all behind, so I'd better take it."
                brennan "I'm so glad. That long shuttle trip will be much more interesting with you on board with me."
                if (cheated_on_him):
                    her flirt "Oh, really? What were you thinking we'd do?"
                    brennan happy "You and me, in close quarters for a month with no other entertainment? What {b}won't{/b} we do?"
                    her flirt "I can't wait..."
                else:
                    her flirt "Ha! We'll see about that."
                    
                if (is_pregnant_later):
                    her surprised "The baby might even be born on Earth..."
                    brennan normal "There's no better place."
                    show her happy

                # She's giving up on the colony
                if (community_level >= COMMUNITY_LEVEL_OK):
                    $ community_level = COMMUNITY_LEVEL_OK - 15
                else:
                    $ community_level -= 15

                if (loved >= 0):
                    $ loved = -10
                else:
                    $ loved -= 10
                return
        brennan normal "You're lucky, [her_name]."
        her surprised "Why?"
        brennan "You have a place here. People who need you, depend on you, love you."
        brennan "Of course you wouldn't want to give that up."
        her serious "I'm glad you understand. I'll miss you, though - you've helped me a lot."

    else:
        her surprised "What? Where are you going?"
        brennan normal "Back to Earth."
        her flirt "How are you going to do that?"
        brennan "On the shuttle that's coming soon!"
        her surprised "They're returning to Earth?"
        brennan "Yeah, they're bringing back some samples of rocks and plants for the scientists on Earth to study. So I thought I'd tag along."
        her concerned "You've never liked it here, have you?"
        brennan mad "...No. If it wasn't for-"
        her surprised "If it wasn't for what?"
        if (discovered_qec):
            brennan normal "If it wasn't for my job, I never would have come here. I'm a civilized man; I like the comforts of Earth."
            her serious "So your new orders are to head back?"
            brennan "They want me to bring some metal samples, too; I've found some ore they might be interested in."
            her annoyed "They better not come ruin this planet with huge mines and factories."
            brennan mad "If the minerals are worth it, they might."
            her annoyed "..."
        else:
            brennan happy "Never mind."

        her serious "Well, that's too bad. You've helped me a lot."

    brennan normal "I'm sure I'm easily replaceable. There will be new colonists coming on the shuttle, after all."
    her normal "That's true. But I'm sure none of them will be as...unique as you."
    brennan happy "You mean none of them will be as handsome and dashing?"
    her flirt "I meant exactly what I said."
    
    return


label set_work_bg:
    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "carpenter"):
        scene bg workshop with fade
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade
    return
