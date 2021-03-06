# File containing the tutorial, played at month 1

label tutorial_ask:
    scene screenshot
    menu:
        "Would you like to see the tutorial again?"
        "Show Tutorial":
            jump tutorial
        "Return":
            call screen computer_pad(["Work", "Skills", "Free Time"])

label tutorial(from_computer_screen=True):
    scene screenshot
    tutorial "This screen shows [her_name]'s computer pad."
    
    scene screenshot_left with dissolve
    tutorial "On the left is her Personal Status."
    tutorial "[her_name]'s expression shows you how relaxed or stressed out she is."
    tutorial "[his_name]'s expression shows you how he is feeling this month."
    tutorial "The heart in the middle shows the strength of their relationship."

    scene screenshot_center with dissolve
    tutorial "In the middle is the Colony Status."
    tutorial "You can see what the weather is, and what messages are on the colony message board. There's new messages to read every month!"
    
    scene screenshot_right with dissolve
    tutorial "On the right, you choose [her_name]'s focus for this month."
    tutorial "Taking it easy at work is more relaxing, but is not as useful to the colony. And, some months are so busy that taking it easy is not an option."
    tutorial "All the skills are useful and help [her_name] and the colony in different ways, so choose whichever skill you like. Mastery of a certain skill can unlock new scenes and help the colony in special ways."
    tutorial "But remember, life's too short to master every skill (at least, until New Game+)!"
    tutorial "During Free Time, choosing to spend time together will increase their relationship, but is not as relaxing as spending time alone."

    scene screenshot with dissolve
    tutorial "You have 25 months to maintain their relationship and help the colony survive."
    tutorial "Good luck!"
    
    if (from_computer_screen):
        call screen computer_pad(["Work", "Skills", "Free Time"])
        
    return
