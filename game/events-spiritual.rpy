# Afternoon Events
# Spiritual

# the default
label spiritual_def:
    call play_scene_music from _call_play_scene_music_142
    scene bg path with fade
    "I took a walk and spent some time just thinking."
    $ skill_spiritual += 10

    return

# Intro Event
label spiritual_0:
    call play_scene_music from _call_play_scene_music_143
    # attending church and praying
    scene bg church with fade
    "Coming to a new planet and leaving behind my old job, friends, and family felt pretty lonely sometimes."
    "I mean, of course I had [his_name], and I was making some friends here, but I yearned to feel more included, a part of something bigger than myself, bigger than just our colony."
    "I decided to check out the worship services that Sister Naomi led."
    show naomi at center with dissolve    
    naomi "...we are all invited to come and partake of goodness and peace. Do you think it matters what planet we are on?  Of course it doesn't. We all have the same access to divine inspiration and guidance, no matter where we are."
    naomi "Now let us pray."
    "I thought she was going to pray for us, but instead we had a few minutes of silence where everyone could pray on their own."
    menu:
        "I..."
        "Didn't know what to say.":
            "I didn't know what to say, so I just kind of sat there. I guess it was peaceful."
        "Poured out my heart to God.":
            "I poured out my heart to God. I talked about everything that was bothering me, everything that made me happy, and asked for help."
            "I prayed that we would be protected, that we would make good decisions, that we would know what to do."
            "Praying about all that helped me feel at peace."
        "Prayed for peace and understanding.":
            "I wished for an increase in love, peace, and understanding in the people of Talaam -- and of Earth. I also prayed for peace in my own heart, and that I might understand people better instead of judging them."
            "Praying about all that helped me feel at peace."

    "Every week she had different things to say, but she always ended with about ten minutes of just quiet, where people could pray or meditate or just think. I didn't always make time for quiet moments in my everyday life, so I enjoyed this bit of peace."
    $ relaxed += 5
    $ community_level += 1

    "Afterwards, I went up to her to talk. I'd been thinking a lot about what makes us human, and eternity, and divinity."
    scene bg church with fade
    show naomi at midright with dissolve
    show her serious at midleft with moveinleft
    "Naomi Grayson" "Welcome, [her_name]. How can I help you?"
    her surprised "Hi...uh, What should I call you, anyway? Pastor? Reverend?"
    naomi "Why don't you call me \"Sister Naomi\"? While I'm not a nun of any religion, I like to emphasize that we are all like children when it comes to matters of the spirit, and all part of the same human family."
    her normal "Okay, Sister Naomi...what exactly do you do here?"
    naomi "When people have questions about what they should do, or what to believe, sometimes it is helpful for them to have a guide. Since there are people of many different faiths here on Talaam, I try and guide them in a way that is helpful for their religious background."
    her serious "But what do you believe?"
    naomi "Is that really the question you should be asking?"
    her surprised "Huh?"
    naomi "What do {b}you{/b} believe?"

    menu:
        "What do {b}I{/b} believe?"
        "I don't know.":
            her concerned "I don't really know what I believe. My parents didn't talk about spiritual things much."
            her normal "That's why I'm coming to you; I want to learn more."
        "I have strong beliefs.":
            her happy "I've thought a lot about religion and spirituality, and I have my own reasons for my beliefs, but I still want to learn from others and their experiences."
        "I don't think it matters.":
            her annoyed "What does it matter what I believe? I'm only interested in what's true."

    naomi "It is good to want to learn. May I suggest learning about several of the main religions people believe in here on Talaam, and let your experiences there guide you further?"
    her normal "I would like to learn more, yes."
    naomi "I have several books you can borrow, if you would like. But as you study, listen with your heart as well as your mind. Read as if the writer is speaking to you, about your own life, and perhaps you will find some truth that you need."
    $ skill_spiritual += 10
    return

# Reading a little each day
label spiritual_1:
    call play_scene_music from _call_play_scene_music_144
    scene bg farm_interior with fade
    show her serious at center with dissolve
    "I downloaded some of the books Naomi sent me and took a look at them."
    "There were books from all over the world, from all different religions."
    "This was going to be a lot of reading."
    "Maybe I'd start on that next time..."
    "I mean, I should probably decide if it was even worth studying."
    "I thought about different religious texts and how and why they were written. A lot of them had been copied by hand over hundreds or thousands of years... clearly, the people writing them had thought they were incredibly important."
    "Even though each writer was partly a product of his or her own culture, they also each felt like they had something new to add, something so important that people passed it on for generations..."
    her surprised "If this is what humanity's ancestors have thought were the most important things to know about being a human, shouldn't I at least take a look?"
    show her normal
    "I decided to read a little bit each day."
    $ skill_spiritual += 10
    return

# Reading the Dhammapada
label spiritual_2:
    call play_scene_music from _call_play_scene_music_145
    scene bg farm_interior with fade
    show her serious at center with dissolve
    "One of the books Naomi loaned me was the Dhammapada, a collection of sayings of the Buddha. There were a lot of good teachings, but I was struck by one part in particular..."
    her serious "\"For hatred does not cease by hatred at any time: hatred ceases by love, this is an eternal rule.\""
    her concerned "..."
    her serious "I don't really {b}hate{/b} anyone, but I certainly don't always love everyone either."
    her surprised "Can you even love someone when you're mad?"
    her concerned "You don't stop arguing by arguing; you stop arguing with love and seeing the other person's point of view. If you still disagree after that, at least you'll understand each other and maybe won't need to argue as much?"
    her surprised "Now can I actually {b}do{/b} that?"

    $ skill_spiritual += 10

    return

# See if he wants to come to church
label spiritual_3:
    call play_scene_music from _call_play_scene_music_146
    scene bg farm_interior with fade
    show him normal at midleft
    show her normal at midright
    with dissolve
    
    $ he_goes_to_church = False
    her "Hey, [his_nickname], I was going to go to church services today... do you want to come?"
    him surprised "Why are you going?"
    menu:
        "What should I say?"
        "It helps me be a better person.":
            her normal "I learn ways to become a better person. Sister Naomi always makes us think and helps us see our weaknesses and find ways to overcome them."
            him surprised "Hmmm, really?"
            if (loved >= 0):
                him normal "Maybe I'll come with you today, then."
                $ he_goes_to_church = True
            else:
                him concerned "Let me know how it is; I've got too much stuff going on here."
        "It helps me feel more at peace.":
            her concerned "Sometimes I feel so stressed out... church is one of the few places where I really feel at peace."
            him surprised "Hmmm, really?"
            if (loved >= 0):
                him normal "Maybe I'll come with you today, then."
                $ he_goes_to_church = True
            else:
                him concerned "Let me know how it is; I've got too much stuff going on here."
        "I like socializing with everyone.":
            her normal "I like to have an excuse to see everyone and chat with them."
            him annoyed "That's why you go?"
            her serious "Well, one of the reasons..."
            him serious "Well, I don't really want to do that, so I'm staying here."
        "I feel like I'm supposed to.":
            her concerned "I guess I feel like I'm supposed to. Maybe I go because I feel guilty if I don't?"
            him surprised "Really? You'd feel guilty if you didn't go to church?"
            her concerned "Yeah, isn't it something you're supposed to do?"
            him serious "Only if it helps you."
            her concerned "Does that mean you don't want to come?"
            him concerned "Not really, I've got too much stuff going on here."
    
    her serious "Okay..."

    "I didn't dress up or anything - nobody here owned nice clothes."
    if (he_goes_to_church):
        "We held hands as we walked to town and entered the small chapel."
    else:
        "I walked to town and entered the small chapel."
    scene bg church with fade
    "Probably about half the people of the colony were there. Some people were coming in from smaller rooms on the side; some denominations held their own meetings before Sister Naomi's sermon."
    "We sang a hymn of thankfulness for blessings, and Mrs. Perón gave a prayer."
    show naomi at center with moveinright
    naomi "Today I want to share a parable with you."
    naomi "Once there was a merchant travelling to a far-off land. He carried fruits and other foods. While he was travelling, one of the fruits fell out of his pack and rolled down the hill to a gardener's house."
    naomi sad "No fruit trees grew in this area; everyone thought it was too dry and rocky."
    naomi normal "But this fruit landed in some soft earth that had been cleared by a man who lived nearby. Wild animals came and ate away the fruit, but the seeds nestled into the soft dirt."
    naomi sad "When they sprouted, the man who lived there didn't know what they were. He thought about pulling them up so they wouldn't bother his garden. But he decided to wait and see what would grow."
    naomi normal "He waited for years and years, until a great tree grew there, and every summer it gave bushels and bushels of delicious fruit to the man, who shared it with his friends and neighbors with a heart of thanksgiving, and humility."
    "Sister Naomi was quiet for a minute, letting us think about what she said. I wondered if we were supposed to be the merchant, or the gardener, or maybe the seeds?"
    "She told a few more stories, but I kept thinking about those seeds."
    "She ended with a few moments of silence for us to ponder or pray."
    
    if (he_goes_to_church):
        "Then there was a potluck lunch, where everyone brought some food to share, and we talked and mingled with the other colonists."
        
    scene bg path with fade
    show her normal at midright
    
    if (he_goes_to_church):
        show him normal at midleft
        "Then we walked home."
        her surprised "What did you think about it, [his_name]?"
        him serious "Oh, it was alright. Sister Naomi seems really nice."
        her serious "Yeah... I keep thinking about that story about the seeds."
        him "Yeah, me too... Like, what kind of seeds are we planting for those who will come after us?"
        her concerned "It made me think about how I came here, even though I had no idea what it would be like. I'm still waiting to see what sort of tree this colony will grow into..."
        show her serious
        "We walked in thoughtful silence together all the way home."
    else:
        "I walked home slowly by myself, thinking about everything she had said."
        "Was I doing everything to have the life I wanted? Was my attitude one of humility and thanksgiving, or ingratitude and selfishness?"
        "What would help me to improve my relationships and my situation?"
        "What seeds could I plant now, what things could I do to later have the life I wanted?"
    $ skill_spiritual += 10
    return

# Reading the Upanishads
label spiritual_4:
    call play_scene_music from _call_play_scene_music_147
    scene bg farm_interior with fade
    show her normal at center

    "Another book Naomi loaned me was the Hindu Upanishads."
    her serious "\"That one, who is able to visualize the presence of Atma (the Soul) in all other moving things and even creatures and is able to visualize the presence of all such things within the Atma, never gets angry and he never hates anything in life.\""
    her surprised "So...I should try to visualize the souls of all the living things?"
    her annoyed "Ugh, even those nasty bugs that sneak in the cracks of our house to drink out of our wash basin?! I can try..."
    "I thought about it for a few minutes."
    her surprised "I guess even they have a soul of sorts...they are just thirsty, aren't they? They're not {b}trying{/b} to scare the crap out of me in the morning. Poor things..."
    her concerned "...and I guess I should try to visualize the souls of other people, too."
    menu:
        "Whom should I think about?"
        "[his_name].":
            her serious "[his_name]'s soul... Sometimes he acts kind of rude, but I think that is usually when he is worried about something. He probably feels like the whole farm is his responsibility, and if anything goes wrong he has to fix it on his own."
            her normal "So instead of getting mad at him for being rude, maybe I could try and see what he's worried about."
        "My boss.":
            her annoyed "I hate it when Mayor Grayson tells me how to do my job... but how does he see the situation?"
            her concerned "..."
            her sad "I guess he probably is worried about the colony, and wants to make sure everything goes well so that we can all survive together."
            her serious "What a huge responsibility that would be! And he actually does a good job, most of the time.  He could use my support, not my annoyance."
        "Sara.":
            her annoyed "Sara comes to me about every little problem...sometimes it gets kind of annoying."
            her serious "But I know she doesn't really have any other friends, and her husband isn't much of a talker, either."
            her normal "She always seems to feel better after we talk...maybe if I can keep in mind how important it is to her I can be a better listener and friend to her."

    "Thinking about another person's perspective did help me to understand them better, so maybe I wouldn't get mad at them as easily in the future."
    
    scene bg church with fade
    show naomi at midright with dissolve
    show her normal at midleft with moveinleft
    naomi "How is your reading going, [her_name]?"
    her serious "Pretty good. Some of the books are more confusing than others, but there's always something that helps me think about things differently."
    naomi "I'm glad to hear it. How is [his_name] doing?"
    her normal "Good, he's been working hard every day growing food."
    naomi sad "Yes, I don't see him very often, so I guessed that he was very busy."
    her surprised "How are you and Pavel?"
    naomi normal "Well, we miss our family sometimes, but we really feel that what we are doing here is important."
    her surprised "You left family back on Earth?"
    naomi "Yes, we have four children and seven grandchildren."
    her concerned "That must be hard not to see them... Didn't any of them want to come with you to Talaam?"
    naomi "No, they are all very much involved in their own areas. We miss them, but they are getting along just fine without us."
    her happy "Well, we're lucky they were able to part with you, because you and Pavel really bind this community together."
    naomi "Thank you, [her_name], we are all working towards that, I hope."
    
    $ skill_spiritual += 10
    return

# Pondering, praying, meditating
label spiritual_5:
    call play_scene_music from _call_play_scene_music_148
    scene bg path with fade
    "I decided to take a break from reading for a while...I wanted to experience some of the things I read about for myself."
    menu:
        "I decided to:"
        "Meditate.":
            "I found a quiet place and sat down, emptying my thoughts. I tried to be like the ocean, letting thoughts drift away like bits of kelp. Without my thoughts, what was I?"
            "Without any distractions, without any worldly cares, I could just...{b}be{/b}. The boundary between myself and other living things seemed smaller, somehow, and I floated in a sea of stars and souls."
            "The physical world I could see was such a small portion of the universe..."
        "Pray.":
            "I prayed to God to help me find the truth I had been looking for. I prayed that our little colony would make it. I prayed that [his_name] and I would make it. I prayed for forgiveness and comfort and peace and something to fill the emptiness that I felt sometimes even when I was happy."
            "And...I felt something. It was like the feeling you get when you know someone far away is thinking about you, or the feeling you get when someone looks in your eyes and sees your soul, or the feeling of belonging and being loved and knowing everything will be okay."
            "It wasn't lightning or thunder; I didn't faint or scream or shout; but it was {b}something{/b}, and it was something that I wanted to draw closer to."
        "Ponder.":
            "As I walked I pondered. I thought about the stars; how many trillions of stars were there, and how small our one little planet was. I marvelled at how many living things there were, just on our own little farm, not to mention in the universe."
            "I was just one of those little lives. Could I make a difference? What was the point of my life, unless I made things better for at least some other little lives near mine?"
            "I felt inspired to do better, and be better."
  
    $ relaxed += 5
    $ skill_spiritual += 10
    return

# Reading the Koran; helping Helen Jennings
label spiritual_6:
    call play_scene_music from _call_play_scene_music_149
    scene bg farm_interior with fade
    show her normal at center
    "In the Koran I read:"
    her serious "\"You will not attain piety until you expend of what you love; and whatever thing you expend, God knows of it.\""
    her surprised "What is \"piety\", anyway? Maybe I'll ask Sister Naomi..."
    scene bg church with fade
    show naomi at midright with dissolve
    show her serious at midleft with moveinleft
    naomi "What is piety? Come with me, and I will show you."
    scene bg path with fade
    show naomi at midright with moveinleft
    show her serious at midleft with moveinleft    
    "I followed her across town, and she still kept walking. I started to feel impatient."
    her annoyed "Where are we going?"
    naomi sad "We are needed."
    scene bg talam with fade
    "We walked past one farm, and then another. We had been walking for about a half an hour. Finally, we reached the farthest farm from town. It belonged to the Jennings - Helen and Pete were newlyweds like [his_name] and me."
    "They were the farthest farm for a reason; they seemed to like to be by themselves. I hardly ever saw them, or their baby who was born on the shuttle."
    "When we got there, Sister Naomi knocked on the door and Helen let us in."
    scene bg farm_interior flip
    show helen at quarterright
    show baby boy at quarterrightbaby
    with dissolve
    show naomi sad at center behind baby
    show her normal at midleft
    with  moveinleft
    "We entered their small cabin, not that much different from our own. Helen was sitting on the bed with the baby on her lap doing some knitting. She invited us to sit next to her."
    her surprised "What are you making?"
    helen "It's supposed to be a baby hat, but it isn't turning out very well. I don't think any baby's head is shaped like this."
    show her laughing with dissolve
    "She held up her misshapen knitting. It looked more like a hat for a dragon than a baby. I laughed without thinking, but Helen didn't laugh with me."
    show her sad with dissolve
    "Naomi didn't say anything - she just patted Helen's shoulder and looked at me. I felt so awkward; what was I supposed to say?!"
    menu:
        "What should I say?"
        "I think the hat looks fine.":
            her normal "I think the hat looks fine. It's not like the baby's going to care if it's a little crooked; he'll just be happy to have a mom who loves him enough to make him a hat at all."
            "I expected her to laugh, but she didn't."
            helen "Yeah... hopefully it will at least stay on."
        "{i}The problem is with this row of stitches here.{/i}" if (skill_creative >= 60) :
            her serious "The problem is with this row of stitches here. See?"
            helen "Oh, you're right! I'll have to redo these last six rows..."
            her normal "The rest of it looks great. Ummm....how's your baby doing, anyway?"
            "She looked down at him, and he grinned toothlessly."
            helen "He's doing okay, I think. He's growing bigger, anyway."
        "How's your baby doing?":
            her concerned "How's your baby doing, anyway?"
            "She looked down at him, and he grinned toothlessly."
            helen "He's doing okay, I think. He's growing bigger, anyway."
        "{i}I'm going to have a baby, too{/i}" if is_pregnant:
            her normal "We're going to have a baby soon..."
            helen "Oh? Congratulations."
            her serious "Thanks...It's a weird feeling, isn't it?"
            helen "Being pregnant?"
            her concerned "Knowing that someone else, a little stranger, is depending on you so much."
            helen "That's true..."
        "{i}I wish I was expecting, too{/i}" if want_kids and (not is_pregnant):
            her serious "Yeah, we really want to have kids, but who knows how long it might take?"
            helen "We weren't really anticipating becoming parents so soon..."
            her normal "Well, I think you're doing great. It's cool that you're making something for the baby."

    show naomi sad at quarterleft behind baby
    show baby boy at quarterleft, Position(ypos=400)
    with move
    show her serious at center with move
    
    "We sat in silence for a few minutes. Naomi picked up the baby and played with him on the other side of the room, leaving Helen and I sitting together."
    "I didn't know what to say. I hoped Naomi would say something wise and comforting, but she didn't. Finally, Helen set down her hat."
    helen "The truth is, I hate knitting."
    her surprised "You do?"
    helen "Yes! But the one thing I hate more than knitting is feeling useless! I wish I could be helping Pete with the cows, or working at the library, or {b}something{/b} other than sitting around waiting for this baby to grow up!" 
    her surprised "Well, aren't there some other things you could do, even while watching a baby? It's not like he has to stay home all day."
    helen "I don't know... this planet is so strange, I don't really feel safe taking him outside. And I don't feel safe leaving him here by himself, either."
    her serious "When will it be safe enough?"
    helen "What?"
    her annoyed "Will it be safer when he's two? Six? Ten?"
    helen "Probably not..."
    her concerned "There's risks everywhere; that's why he has you. To help him learn how to handle the dangers, not to shield him from any possibility of danger."
    helen "It's just... every time I think about taking him anywhere, all I can think about is all the things that could go wrong. A solar flare giving him skin cancer, or alien bugs landing on him and biting him, or someone hurting him..."
    
    menu:
        "What should I say?"
        "You need to stop worrying.":
            her serious "Helen... you need to stop worrying so much."
            helen "Don't you think I've tried?! I don't want to think about everything that could go wrong, but that's just what pops into my head!"
            her surprised "Is there anyone that can help you?"
        "That must be hard.":
            her serious "Helen... you sound really anxious."
    helen "Yeah... Sister Naomi has been helping me with some therapy, but I still don't feel ready to leave the house yet."
    if (profession == "doctor"):
        her concerned "If you'd like to make an appointment to meet with me sometime, as your doctor, we could consider some other options. Sister Naomi is a great therapist, but if therapy is not working for you, medication is an option."
    else:
        her concerned "Would it help if I came with you?  We could just go on a short trip together, maybe to visit Pete or something, and I can help you with anything you need."
    
    helen happy "Thanks, [her_name]. I'll... I'll think about that."
    show helen normal with dissolve
    "We talked some more about other things, and Naomi left a book that she had brought, and then it was time for us to go. It was getting late, and it would take me a while to walk all the way home from Helen's house, but I felt that it was worth it."
    scene bg path with fade
    show naomi sad at midleft
    show her normal at midright
    with moveinleft
    show night
    her surprised "But...what did any of that have to do with piety?"
    naomi "You read \"You will not attain piety until you expend of what you love\"."
    her serious "Well...Helen is definitely giving up a lot for her baby, even if I'm not sure all her sacrifices are necessary."
    naomi normal "I was talking about your sacrifices, [her_name]. You gave of your time, and of yourself."
    show her normal
    
    $ skill_spiritual += 10
    $ community_level += 2
    return

# Reading the Tao Te Ching
label spiritual_7:
    call play_scene_music from _call_play_scene_music_150
    scene bg farm_interior with fade
    show her normal at center with dissolve
    "Naomi sure sent me a lot of books to read...but I think I'm getting something out of them."
    "Today I was reading part of the Tao Te Ching."
    her serious "\"I treat those who are good with goodness,\nAnd I also treat those who are not good with goodness.\nThus goodness is attained.\""
    her "\"I am honest with those who are honest,\nAnd I am also honest with those who are dishonest.\nThus honesty is attained.\""
    her surprised "I guess the only person whose goodness or honesty I have any control over is myself. If people were only nice when other people were nice, soon no one would feel like they had to be nice."
    her serious "That's kind of like turning the other cheek, isn't it?"
    "There were a lot of teachings that seemed to be in common across different religions, even if their theology and cultures were widely different."
    her concerned "Some of these scriptures are so old... people sacrificed a lot to make sure they were passed down to future generations... What wisdom will I pass on to future generations?"
    "I thought about that for a long time. I decided to keep a journal, where I could write down the things I had learned."

    $ skill_spiritual += 10
    return

# Reading the Tattvartha Sutra
label spiritual_8:
    call play_scene_music from _call_play_scene_music_151
    scene bg farm_interior with fade
    show her normal at center with dissolve

    "I read some of the Tattvartha Sutra, central to Jainism."
    her serious "\"Rendering help to another is the function of all human beings.\""
    her surprised "Our...function? \nThat makes us sound like robots!"
    her normal "Well, that's a good question - if I was a robot programmed to help other humans, what would I do differently?"

    her concerned "Maybe I would think about other people more?"
    her happy "What if I had sensors that could detect when people needed my help? That would sure be handy."
    her serious "I suppose that getting in the habit of thinking about other people would help with that."
    her concerned "I do that sometimes, but how can I remember to think about others more? Just wanting to isn't going to make it happen..."
    her serious "I suppose that's why mindfulness and prayer are such an important part of most religions. Without daily reminders, we forget about the little changes we want to make."

    "I decided to set aside a time each day to think about how I can help all the people in my life. I would even add items to my schedule or to-do list on my computer pad if there were specific things I wanted to do that day."
    "At first it felt a little awkward - slightly as if I were programming a robot."
    "But I was able to think about others more and help them in specific ways."
    her serious "Sara is often lonely; I should invite her to lunch this week.  Hmmm, Natalia was mentioning that she loves potatoes, and I don't think they are growing any on their farm - I could give them some of ours."
    her concerned "[his_name] has been really stressed out lately - he'd probably like it if I spent some time with him."
    her normal "It's been really nice of Sister Naomi to lend me these books and take the time to talk to me so much lately - I should tell her thank you for that."
    
    "They were just little things, but I could tell they meant a lot to the people I helped."

    $ community_level += 3
    $ skill_spiritual += 10
    return

# Reading the Bible; helping Naomi
label spiritual_master:
    call play_scene_music from _call_play_scene_music_152
    scene bg farm_interior with fade
    show her normal at center

    "I had read so many religious texts from all over the world, but last I started reading the Bible."
    "I was touched by how many people Jesus helped, and his continual teaching that people stop seeing people who were different as \"others\" but instead treat them as neighbors."
    "A lot of the stories were familiar, but there were some things I had never read before."
    "I read in 1 Thessalonians, \"In every thing give thanks,\" and it made me stop and think."
    her surprised "Can I really give thanks for {b}everything{/b}?"
    "There were a lot of things I was definitely not grateful for - pests, bad weather, sickness, arguments..."
    her concerned "I can't give thanks for those things."
    "But then I read it again."
    her normal "It doesn't say to give thanks {b}for{/b} everything, but {b}in{/b} every thing... so I should give thanks no matter what situation I'm in?"
    her happy "I guess there is always something to be grateful for, even when things are going wrong."
    "I thought about when the bugs had destroyed most of our corn."
    her serious "Even though we lost a lot of our corn, we did learn more about the planet. And our other crops haven't had many pest problems... the weather is nice, and we still have plenty of food to eat."
    her normal "I like my job; I've been doing a lot of good there. I have good friends, like Sara and Sister Naomi."
    if (loved >= 0):
        "And I'll always have [his_name]..."
    her happy "I do have a lot to be thankful for..."
    "I felt my attitude changing even as I recognized how many good things I had in my life."
    scene black with fade

    if (profession == "doctor"):
        scene bg clinic with fade
        show naomi at midright
        show her normal at midleft
        with dissolve
        "That week, the Mayor brought in Sister Naomi, who was having a stroke."
        "Luckily, he brought her in soon enough that we were able to dissolve the blood clot and halt the damage."
        "When the danger was passed and she was awake, I went in to speak with her."
    else:
        "Later, I went to see Sister Naomi, but found out that she had just had a stroke and was in the clinic."
        "When she was well enough for visitors, I headed over to see her."        
        scene bg clinic with fade
        show naomi at midright with dissolve
        show her normal at midleft with moveinleft
    her concerned "Sister Naomi, how are you doing?"
    naomi sad "The headache is gone, and my eyesight is back to normal. But...moving is difficult on my left side..."
    if (profession == "doctor"):
        her serious "Yes, there is some damage there. With therapy, I believe we will be able to restore use of your limbs."
    else:
        her serious "That's awful! Is it permanent?"
        naomi normal "Probably not. The doctor said I'd need a lot of therapy, but my chances are good for a full recovery."
        her normal "That's good."
        
    naomi sad "But, I won't be able to lead the services tomorrow."
    her surprised "You don't have anyone who can fill in for you?"
    naomi "No, I'm the only one who works at the chapel."
    her concerned "That's no good. You should be able to take it easy for a while."
    her happy "Why don't you let me handle things for the next few weeks? It'd be better than cancelling, wouldn't it?"
    naomi normal "Yes, I think it would be good for everyone to hear from someone new. Thank you, [her_name]."

    scene black with fade
    "I was a little nervous about speaking about such important things in front of half the colony. I knew they all had different beliefs, too - I didn't want to offend anyone."
    "But I prayed for help, and decided to prepare a sermon on gratitude, using some stories and verses from all the scriptures I had read."

    scene bg church with fade
    show her serious at center
    "The congregation was a little surprised to see me up at the stand instead of Sister Naomi, but we sang and prayed together like normal, and then I delivered my sermon."
    "I talked about how gratitude makes us happier. True gratitude also helps us be motivated to help others."
    "I told about Moses parting the Red Sea, and how the Israelites praised God for protection and gave thanks."
    "I counseled everyone to not just appreciate things, but also people. I challenged them to think of three people they could say thank you to this week."
    show her concerned
    "It wasn't too bad, but it was way too short! The service wasn't supposed to end for another fifteen minutes!"
    "I started to panic, but then a wave of calm swept it away. I had an idea."
    her normal "Let's not wait until later to be grateful. Let's give thanks right now. If you would like, please take turns sharing with us one thing you are grateful for."
    "I sat down. Would anyone volunteer?"
    hide her
    "The silence continued. A few people shuffled in their seats."
    show ilian at center with dissolve
    ilian happy "I'm thankful for my wife, Sara. She never complains, and is always smiling cheerfully."
    hide ilian
    show lily at center with dissolve
    lily happy "I'm thankful for electricity."
    hide lily 
    show thuc at center with dissolve
    thuc "I'm grateful to Mayor Grayson. He's fair and cares about everyone."
    hide thuc
    show julia at center with dissolve
    julia "I'm thankful for the doctor's quick care, so Van didn't choke to death."
    hide julia
    "Even some of the kids chimed in."
    show raul at center with dissolve
    "Raúl Perón" "No school today!"
    hide raul
    show kid at center with dissolve
    "Gardenia Nguyen" "We haven't been eaten by wolfslugs!"
    hide kid
    show van at center with dissolve
    van "Mommy and daddy."
    hide van
    
    "They were all simple things, but thinking about them made us all feel so blessed and full of hope. And that hope gave us strength to work hard and help each other."
    scene bg clinic with fade
    show naomi at midright with dissolve
    show her normal at midleft with moveinleft
    naomi "So, how did it go?"
    her happy "It went well! I think it helped that everyone got to give their ideas at the end."
    naomi "That's true; that probably helped make it real for them."
    her normal "I love helping people feel positive and hopeful."
    naomi "We certainly need that here, don't we?"
    her concerned "Yes..."
    naomi sad "What is it?"
    her concerned "Can I ask you a question?"
    naomi normal "Of course."
    her surprised "What do you believe? And why?"
    naomi sad "[her_name], that is a question with a very long answer. An answer that is still changing and growing even as I am still learning."
    her serious "I know..."
    naomi "But I will share with you one thing, today. When I was a child, my parents both had very different religious beliefs. My mother was a Christian who also practiced many of the traditions of the Acoma Pueblo where she grew up."
    naomi "My father had grown up with Hindu beliefs, and while he wasn't particularly devout, his mother taught me many of the stories and teachings."
    naomi "My parents were always very respectful of each other, and so I grew up thinking there was nothing strange about believing in Jesus and Vishnu and harmony with nature."
    naomi sad "I believed in them with the simple faith of a child.  Until I was fourteen, and my twin sister died at the hands of a violent stranger."
    her surprised "Oh no!"
    naomi sad "It was no longer obvious to me that a loving and caring deity was in charge, or that all souls deserved an afterlife, or that humanity was any good at all. I questioned everything."
    naomi "People said that her death must have been part of God's plan, but I refused to accept that. My mother said I needed to be more humble, that God knew way more than I did and I should submit to His will."
    naomi normal "But I decided that if God was really all-powerful, He could help me to understand why He would allow such a thing to happen."
    naomi sad "And so I prayed. I studied. I read scriptures, philosophy, logic, history. I felt like Jacob wrestling with an angel, or like Hanuman chasing the Sun. How was it possible that the death of an innocent girl could be God's plan?"
    her concerned "What did you find?"
    naomi normal "For awhile, nothing but empty platitudes. But one night, I had a dream. My sister was in it, laughing. \"How can you laugh when you died so horribly?\" I asked her."
    naomi "\"That was ages ago!\" she said. \"Death is not the worst thing that can happen.\" And so I asked her, \"What is the worst thing that can happen?\""
    naomi "She just shook her head at me and disappeared."
    naomi sad "Since then, I have thought of many more worse things than death. And I had to ask why God would allow those, too. But, I have come to realize that the purpose of life is not to avoid bad things happening."
    her surprised "What is the purpose of life?"
    naomi normal "To me, the purpose of life is to become your best self. Your self that is the most benevolent, the most knowledgeable: the most divine."
    naomi "But that can only happen when people are allowed to have bad things happen. For it is in the reaction, in the choosing, in the consequences, that we change and become more than we have been."
    naomi "That is why God does not stop all bad things from happening."
    her concerned "But then, what is God?"
    naomi "All my experiences with studying and praying and searching for the divine feed into my concept of \"God.\" God is not something you can understand simply by applying a label like \"Jesus\" or \"Brahman\"."
    naomi normal "God is something you understand through study, prayer, and love. Then, I think, you will see the divine all around you."
    
    menu:
        "What should I say?"
        "I agree.":
            her happy "I know what you mean. I have seen it, a little, as I've studied and tried to help people."
            naomi "Good! But we must never stop searching, for \"It is impossible for a man to learn that which he already thinks he knows.\""
        "I will think about that.":
            her serious "Hmmm, I'll have to think about that some more."
            naomi "Please do. You'll never stop learning unless you stop thinking. After all, \"He who asks a question is a fool for five minutes; he who does not ask a question remains a fool forever.\""
        "That's not an answer!":
            her annoyed "That's not really an answer."
            naomi "No, it's not. The best questions don't have answers that you can explain with just a few words."
            naomi "Why do you think there are so many scriptures? They are trying to describe, with limited human words, that which is far greater than any words can convey."
            naomi "But I hope that showing you where I have found answers may have helped you, a little."
            
    her serious "Yes, that's true. I'll keep searching and learning."
    her concerned "But, what about you? How are you really feeling?"
    
    naomi "Well, I've been doing a lot of praying lately."
    her surprised "More than usual?"
    naomi sad "Oh yes. My whole life is built around helping others. But with my stroke, I could barely move, and I needed to be able to accept help instead of giving it."
    her concerned "Why was that so hard?"
    naomi "I had to face my fear of old age."
    her surprised "You're scared of getting old? No offense, but aren't you already... um, I mean--"
    naomi normal "Yes, I've been getting old for my whole life, really. But I've never been helpless, never had my body betray me quite like that."
    her serious "Are you scared of dying?"
    naomi sad "No, dying will be quite interesting. What bothers me is the slow process of decay of the body, and worst of all, the mind."
    her surprised "Has your stroke affected your mind, too?"
    naomi "Well, that's the problem - if my mental capacity is affected, I might have problems detecting it. And I wonder if those close to me would be honest and tell me if they notice anything?"
    her serious "I'll tell you the truth, Naomi; you seem just as sharp as ever. And your kind spirit hasn't changed at all."
    naomi normal "Thank you, [her_name]. I appreciate you letting me draw on your strength."

    $ skill_spiritual += 10
    $ community_level += 10
    return
