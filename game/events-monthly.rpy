# Event content for all the important monthly events

# You shouldn't ever see this. This is just a fall through in case something happens
# and there's no event for this month.
label monthly_event_0:
    "Nothing happened this month."
    return

label monthly_event_1:
    "Our first month living on our own together, we had to work a lot of things out."
    menu:
        "It's breakfast time."
        "Make some for [his_name]":
            her "Here, [his_name], I made you some breakfast."
            him "Oh, thank you. I could just make it myself, you know."
        "Ask if he wants some":
            her "So, I'm making breakfast...do you want some?"
            him "Oh, that'd be great, thanks."
            her "Still just meal rations, until the crops start coming in."
            him "Yeah, it will be a while still."
        "Don't make him any":
            him "Oh, you made breakfast?"
            her "Sorry, I just made some for me."
            him "Okay, I can get my own."
    
    "That set the pattern for our mornings. Some things weren't as easy to work out, though."
    her "Thanks for making dinner, but you left the dirty dishes on the stove."
    him "I was going to do them later."
    her "You can't save them for later; they'll attract pests!"
    him "Well, I thought since I made dinner, maybe you would do the dishes."
    her "In my house, whoever made the mess cleaned up the mess."
    him "Well, this is {b}our{/b} house, now."
    menu:
        "We'll do it your way":
            her "Fine, we'll do it your way. Whoever cooks, the other person cleans up afterwards."
            him "Great, that will work."
            "But it didn't work..."
            her "When were you going to do those dishes?"
            him "Those? I'm getting around to it."
            her "They're not going to clean themselves! Since I cooked, it's your turn to wash them!"
            him "Okay, but I'm not doing it right now, I'm in the middle of something."
            "When we went to bed they were still there."
            her "Honey? You haven't done the dishes yet."
            him "Oh, I'm too tired, I'll do it in the morning."
            "But the next morning, I found..."
                
        "We'll do it my way":
            her "Let's do it my way. Whoever cooks, cleans up afterwards."
            him "I guess that will work."
            "But it didn't work..."
            her "Are you going to make dinner tonight?"
            him "What? I wasn't planning on it..."
            her "But I made dinner last night."
            him "I'm not that hungry."
            "{b}I{/b} was hungry, so I just made dinner for myself. It felt a little lonely, though, eating by myself while he was poring over his charts for the farm. Still, I cleaned up and settled down to relax."
            her "(If he gets hungry he can make his own dinner.)"
            "I fell asleep early, and awoke the next morning to find..."
                
        "I'll be in charge of dishes" if (skill_domestic >= 10):
            her "Promptly cleaned dishes are really important to me, so why don't I be in charge of that? We can either take turns cooking, or cook together."
            him "Thanks, I really can't stand doing dishes. I'd rather do almost anything else."
            her "Like getting the water for our morning coffee?"
            him "Yeah, I'll do that."
            her "Thank you; I hate going outside first thing in the morning."
            "So that worked out pretty well."
            $loved += 5
            return

        "Let's take turns fairly" if (skill_knowledge >= 10):
            her "Did you know that men who do more housework are generally happier in their marriages?"
            him "According to who?"
            her "There's also a study correlating amount of housework done with frequency of sex."
            him "What exactly are you trying to say?"
            her "Just thought you might find those studies interesting. In a totally abstract way."
            him "It sounds like splitting household chores is really important to you."
            her "It is. We both work hard all morning in different ways. We don't have to each do half of everything, but I think there will be less chance for arguments if we work out ahead of time what each person will do."
            him "All right, let's make a list, then."
            "We listed all the household chores we could think of, and then marked each one as \"hate\", \"enjoy\" or \"meh\". It turned out that he really hated doing dishes, so I agreed to do them all the time, and since I was not a morning person, he would make breakfast every morning. We worked out the other chores, too."
            "So that worked out pretty well."
            $loved += 5
            return

    #if nobody did the dishes, pest problems!
    her "AAAAAAAAAAAAAAAHHHHHH!!!!"
    him "What is it?! What's wrong?"
    "I just pointed to the dirty dishes. Coiled around his mess kit, happily nibbling on bits of leftover food, was a long, flat, segmented creature with innumerable legs and dangerous-looking claws. It was at least as long as my arm."
    him "Whoa!"

    menu:
        "I..."
        "Yelled":
            her "THAT is why you don't leave dirty dishes out overnight!!!"
            him "Okay! How was I supposed to know this planet had giant leftover-eating millipedes?"
            her "It's pretty obvious! Every planet has its scavengers!"
            him "Calm down, I'll take care of it."
            $relaxed -= 5
        "Cried":
            "I started sobbing."
            her "This would have never happened if you hadn't left out those dirty dishes!"
            him "Hey, hey, it's okay, here, I'll take care of it."
            $relaxed -= 5
        "Laughed":
            her "Who invited the millipede to breakfast?"
            him "Sorry about that. He seemed like such a nice fellow last night..."
            her "I'm afraid he's worn out his welcome. Perhaps you could gently escort him off the premises?"
            him "It would be my pleasure."
            
        "Analyzed":
            her "Interesting. It's legs are jointed like an arthropod, but those claws look more crustacean ... of course, arthropods and crustaceans are not that far apart from each other... how did it get inside, anyway?"
            him "I think it crawled under the front door. There's quite a gap there."
            her "Huh. Looks like it's an omnivore; it ate the protein and the vegetables..."
            him "Well, whatever it is, we should put it back outside."                 
    "He put on his work gloves and picked up the mess kit by the handle. I opened the door so he could take it outside."             
    him "C'mon, George, time to take a hike."
    her "George?! You're giving this thing a name?"
    him "Doesn't he look like a George to you? Besides, I accidentally invited him in with my mess, so I guess he's my pet."
    her "As long as he's an outside pet."
    "The dishes were never left undone after that."
    return

label monthly_event_2:
    # TODO: Should I put the cellar event in here instead, as it is somewhat time dependent?
    "Place in Community"
    return

label monthly_event_3:
    "Even though we were on a new planet, we still kept track of what day it was on the Earth calendar. The seasons didn't match up or anything, but it helped us feel like we were still a part of things back home."
    her "It's his birthday this month!"
    menu:
        "Maybe I should do something for him..."
        "Have a party" if (skill_social >= 20):
            "I invited some friends over and we ate dinner together and played games together until late. We sang Happy Birthday to [his_name]."
            him "Thanks, [her_name] - what a great birthday."
        "Make delicious food" if (skill_domestic >= 20):
            "I couldn't really copy his bread-cake that he made on the shuttle for my birthday, but I was determined to make him something tasty."
            "I found some berries that I had tried before, and combined them with some biscuits from our rations to make a sort of berry shortcake. We had some candles in our emergency case, so I lit one of those for him, too."
            her "Happy birthday, [his_name]"
            him "Wow! Thank you! This looks great!"
            "It didn't taste anything like strawberry shortcake, but it was still good, and [his_name] seemed to like it."
            
        "Make him a present" if (skill_creative >= 20):
            "I thought and thought about what I could make him that he would like."
            "I finally decided I would make him a hat."
            "I could only work on it when he wasn't paying attention, so it went pretty slowly. But finally I was able to finish it."
            her "Happy birthday, [his_name]. This is for you."
            him "A birthday present?! Wow, thanks!"
            "I hoped he would actually like it, and not just pretend like he liked it."
            him "This hat is perfect! It will keep the sun off my neck and will be warm in the cold wind, too!"
            her "I'm so glad you like it."
        "Make him a card":
            "I made him a nice card and gave it to him on his birthday."
            him "What's this for?"
            her "Today's your birthday! On the Earth calendar."
            him "Oh! I hadn't thought about the Earth calendar for a while! I forgot; thank you!"
            her "Sorry I couldn't really get you anything."
            him "It's okay; I have everything I need right here."
            
        "Just tell him happy birthday":
            "I figured it'd be a waste of resources to make him anything special. We had what we needed. But I did tell him happy birthday, and he seemed to like that."
            him "Thanks for remembering my birthday."

    "I was happy I could show him I cared by remembering his birthday."
    $loved += 5
    return

label monthly_event_4:
    "Are Hobbies Waste of Time"    
    return

label monthly_event_5:
    "Differing Value of Items"
    return

label monthly_event_6:
    "Alien Pests"
    return

label monthly_event_7:
    "How Honest Should You Be?"
    return

label monthly_event_8:
    "Conflict of Interest: Community vs. Spouse"
    return

label monthly_event_9:
    "Different Date Ideas"
    return

label monthly_event_10:
    "Something Bothering Him - What To Do?"
    return

label monthly_event_11:
    "Jealous of New Friend"
    return

label monthly_event_12:
    "Frustration with Work"
    return

label monthly_event_13:
    "Monthly 13"
    return

label monthly_event_14:
    "Pregnancy/ Tired And Emotional"
    return

label monthly_event_15:
    return

label monthly_event_16:
    return

label monthly_event_17:
    return

label monthly_event_18:
    return

label monthly_event_19:
    return

label monthly_event_20:
    return

label monthly_event_21:
    return

label monthly_event_22:
    return

label monthly_event_23:
    return
