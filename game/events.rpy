# This file contains the definitions for events that will be part of the 
# game.  We define when each event can happen and what label it should
# jump to.  The events themselves are split up into events-morning,
# events-afternoon, and events-evening.  So if you want to add an event, 
# first define when it happens in this file, then add the label and the 
# appropriate content in event-whatever
  

# TODO: How should these affect stats and/or emotional state?

# "init python" tells renpy this whole next thing is python code. 
# That means we don't need the '$' that we usually use for python code.
init python:
    # MORNING EVENTS
    # Default events if nothing else is going on at work
    event("act_work", "act == 'act_work'", event.solo(), priority=200)
    event("act_skip_work", "act == 'act_skip_work'", event.solo(), priority=200)

    # This is an introduction event, that runs once when we first go
    # to work. 
    event("work_intro", "act == 'act_work'", event.once(), event.only())



    # AFTERNOON EVENTS
    # For each type of skill, we have 10 special events that happen when your skill
    # reaches a certain level.  There is also an intro event and a master event.
    for skill_type in ["domestic", "creative", "technical", "spiritual", "social", "knowledge", "physical"]:
        # Set up default events for each type of skill
        event (skill_type + "_0", "act == 'act_" + skill_type + "'", event.solo(), priority=200)
        
        # Add special events that only happen once when you first get to a certain
        # skill level in that skill type.
        for i in range(1,10):
            event("domestic_" + `i`,
                  "act == 'act_domestic' and skill_domestic >= " + `i*10`,
                  event.once(),
                  event.depends("domestic_" + `i-1`))

        # This event happens every time we work on a skill when it is already maxed
        event(skill_type + "_master",
              "act == 'act_" + skill_type + "' and skill_" + skill_type + " >= 100",
              event.solo(),
              event.depends(skill_type + "_10"))



    # EVENING EVENTS
    # Evening Events
    event("act_relax_together", "act == 'act_relax_together'", event.solo(), priority=200)
    event("act_relax_alone", "act == 'act_relax_alone'", event.solo(), priority=200)