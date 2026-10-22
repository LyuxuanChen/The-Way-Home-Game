"""The Way Home - beginner version.

Run: python3 main.py
All game code is in this file. No packages or imports are needed.
Read CODE_GUIDE.md for a guided explanation.

This version uses ordinary scrolling print/input.
It does not enforce the assignment's strict 80x24 display requirement.
"""


# 1. BASIC INPUT AND OUTPUT
def read_answer(prompt):
    answer = input(prompt).strip()
    if answer.lower() == "q":
        print("Thanks for playing.")
        raise SystemExit  # Python's built-in way to stop the program.
    return answer


def show_message(title, text):
    print()
    print("--- " + title + " ---")
    print(text)
    read_answer("Press Enter to continue (Q to quit): ")


def choose(title, text, options):
    # options is a list of pairs: choice number and its description.
    print()
    print("--- " + title + " ---")
    print(text)

    allowed = []
    for number, description in options:
        print(number + ". " + description)
        allowed.append(number)

    while True:
        answer = read_answer("Your choice (Q to quit): ").lower()
        if answer in allowed:
            return answer
        print("Please enter one of the choices shown.")


def ask_text(title, text):
    print()
    print("--- " + title + " ---")
    print(text)
    return read_answer("Your answer (Q to quit): ")


def normalise(text):
    # Keep letters/numbers only: " To go home! " becomes "togohome".
    result = ""
    for character in text.lower():
        if character.isalnum():
            result += character
    return result


# 2. PROGRESS: A DICTIONARY STORES WHAT THE PLAYER HAS DONE
ENDING_NAMES = {
    "A": "THE WAY HOME", "B": "A STRANGER'S KITCHEN",
    "C": "FIVE METERS", "D": "TWO GRAVES", "E": "FADE",
}


def new_state():
    return {
        "power": False, "badge": False, "diary": False,
        "calibrated": False, "past": False, "fade": 0,
        "location": "Lobby", "notes": {},
        "david_ready": False, "cosign": False, "ending": None,
    }


def update_status(state):
    if state["past"]:
        era = "PAST"
    else:
        era = "RUINS"
    print()
    print(era, "|", state["location"], "| FADE:", state["fade"], "/ 100")
    print("Goal: Stop the experiment. Go home.")



def spend_turn(state, cost=4):
    """Only past-world actions spend FADE. Return False if the player fades."""
    if state["past"]:
        state["fade"] += cost
        if state["fade"] > 100:
            state["fade"] = 100
    update_status(state)
    return state["fade"] < 100


def notebook(state):
    text = ""
    for name in state["notes"]:
        text += name + ": " + state["notes"][name] + "\n\n"
    if text == "":
        text = "You have not recorded any clues yet."
    show_message("Notebook (no FADE cost)", text)



# 3. INTRODUCTION
def prologue():
    show_message(
        "THE WAY HOME - Archive: forty years ago",
        "NEWSREADER: Another city has begun evacuating its residents. "
        "Without reliable electricity, water pumps have stopped, hospitals "
        "are closing, and winter heating is failing.\n\n"
        "Families are leaving homes they may never see again. "
        "Even fusion power has failed to become affordable on a large scale.\n\n"
        "Tonight, a research team prepares to test a different answer "
        "to the energy crisis: a machine called the Rewinder."
    )

    show_message(
        "Archive interview - before the experiment",
        "REPORTER: How could reaching into the past help us now?\n\n"
        "DAVID: The Rewinder retrieves matter from an earlier time. "
        "If we can recover usable fuel with less energy than it provides, "
        "we could power the cities again. Our small tests are promising, "
        "but we still have much to prove.\n\n"
        "REPORTER: And what would success mean to you personally?\n\n"
        "DAVID: Families returning to their streets. Lights in their windows. "
        "A reason to unpack the bags they left beside the door.\n\n"
        "DAVID: I'm building a way home."
    )

    show_message(
        "Archive report - the accident",
        "The interview ends. A later report describes what happened next.\n\n"
        "After successful tests with non-living matter, David volunteered "
        "for the first human trial. The team hoped to prove that the "
        "Rewinder could safely navigate a living person's timeline.\n\n"
        "Instead, it pulled a younger David out of his own history. "
        "The present David vanished. Reality tore around the machine, "
        "and the base burned.\n\n"
        "You helped build the Rewinder. You survived the accident. "
        "Your wife, Dr. Lin, did not.\n\n"
        "The world lost its promised way home. You lost yours."
    )
    show_message("Forty years later",
            "You are seventy now. You helped David build the Rewinder. "
            "Tonight you return to its sealed base with a new theory: "
            "countless possible pasts exist, and one still holds her.\n\n"
            "A restored machine could carry you into the morning of the test. "
            "If you stop it there, you may build a future where she lives.\n\n"
            "You cannot force the ruined doors. You must use what you know.")
    show_message("How to play",
            "Choose numbered options and press Enter. Q quits at any prompt. "
            "The notebook keeps clues. Wrong menu entries cost nothing.\n\n"
            "The ruins have no time limit. In the past, moves and major actions "
            "usually add 4 FADE. At 100 you disappear. Reading, hints and "
            "notebook pages cost nothing; this is not a real-time countdown.\n\n"
            "Goal: stop the experiment and return home. The full win also "
            "preserves your memories. Every ending offers R to restart.")


# 4. FIRST PUZZLE: THE BREAKERS
def lobby(state):
    scanned = False
    failures = 0
    while not state["power"]:
        choice = choose("Lobby - dead board, living card",
                           "The breaker board is dead. Your scanner has just enough "
                           "battery for one saved view of this lobby's past.\n\n"
                           "I MAIN | II AUX | III ...OL | IV ANCHOR | V LIGHTS",
                           [("1", "Scan the lobby's past"), ("2", "Set breaker order"),
                            ("3", "Read notebook")])
        if choice == "1":
            scanned = True
            state["notes"]["Duty card"] = "COOL - AUX - MAIN - ANCHOR. Names, not numbers."
            state["notes"]["Review notice"] = "Original test time: 21:00. Subject to revision."
            state["notes"]["Zhou's maintenance note"] = "Bleed VENT 2 before ignition."
            show_message("Battery snapshot",
                    "An intact duty card reads: RESTORE ORDER: COOL - AUX - MAIN - ANCHOR.\n\n"
                    "Below it: 'Original test time: 21:00. Subject to revision.'\n\n"
                    "Zhou's note: 'Bleed VENT 2 before ignition.' "
                    "All three clues are copied into your notebook.")
        elif choice == "3":
            notebook(state)
        elif not scanned:
            show_message("Missing instructions", "Guessing could damage the board. Scan the old duty card first.")
        else:
            order = ""
            for position in range(1, 5):
                order += choose("Breaker " + str(position) + " of 4",
                                   "Chosen so far: " + (order or "none") +
                                   "\nDuty order: COOL - AUX - MAIN - ANCHOR\n"
                                   "I MAIN | II AUX | III ...OL | IV ANCHOR | V LIGHTS",
                                   [("1", "I"), ("2", "II"), ("3", "III"),
                                    ("4", "IV"), ("5", "V")])
            if order == "3214":
                state["power"] = True
                show_message("Power restored",
                        "The relay holds. III, II, I, IV. COOL, AUX, MAIN, ANCHOR.\n\n"
                        "Emergency lights wake. Your scanner charges from the board: "
                        "full SCAN is now available. The corridor door releases.")
            else:
                failures += 1
                hint = "The relay snaps back. You can retry without penalty."
                if failures >= 2:
                    hint += "\nThe card lists names. Match them to the board's Roman numerals."
                if failures >= 4:
                    hint += "\nCOOL is III, AUX is II, MAIN is I, ANCHOR is IV: 3, 2, 1, 4."
                show_message("Wrong breaker order", hint)


# 5. BADGE, DIARY AND CALIBRATION
def ruins(state):
    failures = 0
    while not state["calibrated"]:
        state["location"] = "Ruins corridor"
        update_status(state)
        choice = choose("The ruined base",
                           "A collapsed panel lies across the corridor. Behind a glass "
                           "door sits the control room. The core console is awake.\n\n"
                           "You need clearance, then the revised test time.",
                           [("1", "Examine collapsed panel"), ("2", "Enter control room"),
                            ("3", "Calibrate the core"), ("4", "Read notebook")])
        if choice == "1":
            if state["badge"]:
                show_message("Empty gap", "You already recovered Dr. Lin's badge.")
            else:
                action = choose("A familiar photograph",
                                   "Her staff badge is trapped under the panel. "
                                   "You recognise the photograph before you read the name.",
                                   [("1", "Pry the panel"), ("2", "Look for a gap")])
                state["badge"] = True
                state["notes"]["Dr. Lin's badge"] = "Recovered. Legacy control-room clearance."
                if action == "1":
                    line = "Your shoulder files a complaint."
                else:
                    line = "The badge slides through a gap."
                show_message("Badge recovered", line + " You brush forty years of dust from her face.")
        elif choice == "2":
            if not state["badge"]:
                show_message("Control room locked", "A staff badge is required. Something shines beneath the panel.")
            else:
                action = choose("Control room",
                                   "LEGACY CLEARANCE ACCEPTED - WELCOME BACK, DR. LIN.\n\n"
                                   "The system still remembers her. David's desk holds "
                                   "a ruined diary. SCAN can recover its earlier writing.",
                                   [("1", "Scan David's diary"), ("2", "Return to corridor")])
                if action == "1":
                    state["diary"] = True
                    state["notes"]["David's diary"] = "Revised: 04:17. After tonight, everything is different. - D."
                    show_message("Diary recovered", state["notes"]["David's diary"] +
                            "\n\nYou copy both the time and his exact words into your notebook.")
        elif choice == "4":
            notebook(state)
        else:
            if not state["diary"]:
                show_message("Calibration needs evidence",
                        "The console warns: TARGET TIME WAS REVISED. The lobby's 21:00 "
                        "notice is outdated. Find David's revision in the control room.")
                continue
            if failures >= 3:
                answer = choose("Calibration fallback", "Choose the REVISED test time.",
                                   [("1", "21:00"), ("2", "04:17"), ("3", "12:00")])
                correct = answer == "2"
            else:
                answer = ask_text("Core calibration", "TARGET TIME (it was revised once).\n"
                                 "Enter the revised time (for example 21:00 input 2100), or Q to quit.")
                correct = normalise(answer) in ("0417", "417")
            if correct:
                state["calibrated"] = True
                show_message("Coordinates locked",
                        "The hands settle at 04:17. Every past view settles with them, "
                        "like dust. The Rewinder is ready.")
            else:
                failures += 1
                text = "Coordinate not on the mainline. No penalty; try again."
                if failures >= 2:
                    text += "\nDavid revised the time to 04:17. Check your notebook."
                show_message("Calibration rejected", text)


# 6. ENTER THE PAST
def crossing(state):
    show_message("Rules of the crossing",
            "You will enter a separate possible past. Your younger self is already "
            "there. The weave cannot hold both patterns for long: your FADE will rise. "
            "Direct contact with him means immediate dissolution.\n\n"
            "When history changes, the old line needs a wick as it burns away. "
            "Your memories will pay that cost unless the designer co-signs a "
            "controlled abort, letting his memories and the logs carry the old line.")
    choice = choose("The will gate",
                       "Once committed, stepping back collapses the unresolved crossing. "
                       "You would dissolve. Proceeding risks everything too.\n\n"
                       "Do you have the resolve?",
                       [("1", "Proceed into the past"), ("2", "Step back (ending: dissolve)")])
    if choice == "2":
        return "E"
    state["past"] = True
    state["location"] = "Past lobby"
    update_status(state)
    show_message("The same rooms, alive",
            "White noise. The corridor is clean. Someone laughs behind a door. "
            "The machine has carried you to 04:17, before the test.\n\n"
            "David is in the preparation room. A technician guards the coolant "
            "room. The experiment hall holds the override console.\n\n"
            "The ignition countdown is paused for preparation; only your actions "
            "advance FADE. You have time to read, but not to wander forever.")
    return None


# 7. PERSUADE DAVID
def persuade(state):
    if state["david_ready"]:
        show_message("David is waiting", "The override is ready in the experiment hall. Finish what you started.")
        return None
    while True:
        choice = choose("David - identity",
                           "'Nobody walks the floor tonight. Who are you?'",
                           [("1", "Tell him: I built this machine with you, forty years from now."),
                            ("2", "Claim to be a facilities inspector"), ("3", "Leave")])
        if choice == "3":
            return None
        if not spend_turn(state):
            return "E"
        if choice == "1":
            show_message("Recognition", "David stares. '...I know those eyes.' "
                    "You describe the design fault that killed him. He listens.")
            break
        show_message("The lie fails", "He asks for an inspection badge. You have none. "
                "The wasted explanation costs FADE. You can still tell the truth.")
    choice = choose("David - the creed",
                       "'Even if I believe you, this machine could save the world.' "
                       "You remember the archive interview.",
                       [("1", "You promised a way home. Tonight this only burns homes down."),
                        ("2", "Leave the conversation")])
    if choice == "2":
        return None
    if not spend_turn(state):
        return "E"
    show_message("He wavers", "'Then use the designer override. The passphrase was never "
            "written on the console. You will have to understand why I built it.'")
    options = [("1", "Tell him about the woman in your photograph")]
    if state["diary"]:
        options.append(("2", "Quote his diary: After tonight, everything is different."))
    choice = choose("David - why did you come?",
                       "He can step aside, or join you in signing the abort. "
                       "A co-signed abort could preserve your memories.", options)
    if not spend_turn(state):
        return "E"
    state["cosign"] = (choice == "2")
    state["david_ready"] = True
    if state["cosign"]:
        show_message(
            "Two signatures",
            "YOU: 'After tonight, everything is different.' "
            "Those are your words, David.\n\n"
            "David goes still.\n\n"
            "DAVID: I just wrote that in my diary. "
            "I haven't shown it to anyone. How could you know?\n\n"
            "YOU: I read it in the ruins of this place, "
            "forty years from now.\n\n"
            "He studies your face, recognising his colleague "
            "beneath forty years of age.\n\n"
            "DAVID: Then we have to stop this. Together.\n\n"
            "He agrees to add his private key beside yours. "
            "Meet him at the experiment hall console."
        )
    else:
        show_message("He steps aside", "David studies her photograph and nods. "
                "He will let you use the override, but the machine must abort "
                "without his signature. Your memories will be the wick.")
    return None


# 8. SABOTAGE ROUTE
def sabotage(state):
    choice = choose("Coolant room - technician",
                       "The technician walks a fixed round. A sign warns that "
                       "venting before ignition will destroy the return channel. "
                       "It would stop the test, but strand you here.",
                       [("1", "Act now, while the technician is watching"),
                        ("2", "Wait in the shadow of the tanks (no FADE cost)"),
                        ("3", "Leave")])
    if choice == "3":
        return None
    if choice == "1":
        alive = spend_turn(state, 19)  # Action +4, alarm +15.
        show_message("Caught", "The technician raises the alarm and escorts you out. "
                "Action +4, alarm +15 FADE. You can return and wait for his round.")
        if alive:
            return None
        return "E"
    while True:
        choice = choose("Coolant room - vents",
                           "The technician turns the corner. Three vents are labelled. "
                           "Waiting and reading your notebook do not cost FADE.",
                           [("1", "Bleed VENT 1"), ("2", "Bleed VENT 2"),
                            ("3", "Bleed VENT 3"), ("4", "Read notebook"), ("5", "Leave")])
        if choice == "5":
            return None
        if choice == "4":
            notebook(state)
            continue
        if not spend_turn(state):
            return "E"
        if choice == "2":
            show_message("Ignition impossible", "COOLANT FAULT - SEQUENCE FROZEN. "
                    "The experiment cannot run. The core burns out the crossing "
                    "channel as it shuts down. You have saved them, but lost the way home.")
            return "C"
        show_message("Nothing changes", "The vent equalises silently. That was not Zhou's vent. "
                "The action cost 4 FADE. His maintenance note is in your notebook.")


# 9. FINAL PASSPHRASE
def override(state):
    failures = 0
    while True:
        if failures >= 3:
            answer = choose("Override fallback",
                               "The assistant repeats the interview: 'I'm building a way home.'\n"
                               "WHAT DOES THE CREATOR DESIRE?",
                               [("1", "Fame"), ("2", "To go home"),
                                ("3", "Endless energy"), ("4", "Power")])
            correct = answer == "2"
        else:
            answer = ask_text("Designer's override",
                             "IGNITION HELD - DESIGNER OVERRIDE REQUIRED\n\n"
                             "WHAT DOES THE CREATOR DESIRE?\n\n"
                             "Wrong answers do not increase FADE. Q quits.")
            correct = normalise(answer) in ("home", "gohome", "togohome")
        if correct:
            if not spend_turn(state):
                return "E"
            if state["cosign"]:
                return "A"
            return "B"
        failures += 1
        hint = "The console waits. No FADE cost."
        if failures == 1:
            hint += " The assistant says, 'He once explained why he built it.'"
        if failures >= 2:
            hint += " The assistant remembers his interview: 'I'm building a way home.'"
        show_message("Override rejected", hint)


# 10. CHOOSE WHERE TO GO IN THE PAST
def living_base(state):
    while True:
        state["location"] = "Past corridor"
        update_status(state)
        choice = choose("The living base",
                           "The corridors lead to David, the coolant room and the console. "
                           "You can also hear familiar laughter through the canteen window.\n\n"
                           "Each destination costs 4 FADE outward and 4 on return. "
                           "Reading your notebook is free.",
                           [("1", "Preparation room: speak to David"),
                            ("2", "Coolant room: consider sabotage"),
                            ("3", "Experiment hall: override or assault"),
                            ("4", "Canteen window: familiar laughter"),
                            ("5", "Read notebook")])
        if choice == "5":
            notebook(state)
            continue
        state["location"] = {"1": "Preparation room", "2": "Coolant room",
                             "3": "Experiment hall", "4": "Canteen window"}[choice]
        if not spend_turn(state):
            return "E"
        ending = None
        if choice == "1":
            ending = persuade(state)
        elif choice == "2":
            ending = sabotage(state)
        elif choice == "4":
            approach = choose("Two people over a tray",
                                 "She is alive. Your wife laughs at something said by "
                                 "the man beside her. He is you, forty years younger.\n\n"
                                 "Contact with your younger self will dissolve you.",
                                 [("1", "Keep walking"), ("2", "Approach them (ending: dissolve)")])
            if approach == "2":
                ending = "E"
        else:
            action = choose("Experiment hall",
                               "The override console needs David's cooperation. "
                               "You could instead rush the controls, but your body "
                               "could not survive a struggle.",
                               [("1", "Use designer override"), ("2", "Rush the console"),
                                ("3", "Leave")])
            if action == "1":
                if state["david_ready"]:
                    ending = override(state)
                else:
                    show_message("Override locked", "David must authorise access. Speak to him in preparation.")
            elif action == "2":
                confirm = choose("A final, violent choice",
                                    "David stands between you and the controls. "
                                    "A struggle may kill you both. Proceed?",
                                    [("1", "Proceed (fatal ending)"), ("2", "Step away")])
                if confirm == "1":
                    if spend_turn(state):
                        ending = "D"
                    else:
                        ending = "E"
        if ending:
            return ending
        if not spend_turn(state):
            return "E"


# 11. SHOW THE ENDING
def finish(state, ending):
    state["ending"] = ending
    update_status(state)
    stories = {
        "A": "Two signatures stop the experiment. David's memories and the logs "
             "carry the dying timeline, leaving yours intact.\n\n"
             "Rain on a kitchen window. A kettle whistling. Forty years of grief "
             "that no one in this world remembers but you. She turns from the "
             "stove and smiles like you never left. 'You're home.'\n\nFULL WIN: "
             "You saved her, returned home, and kept your memories.",
        "B": "The experiment stops. The old line burns away, using your memories "
             "as its wick.\n\nShe is alive in the kitchen. You know her, but not "
             "the forty years you spent trying to return. You win everything "
             "except the reason why.\n\nPARTIAL WIN: Next time, ask David to "
             "co-sign. Something in his diary could convince him.",
        "C": "The test can never run. The return channel is gone.\n\nYou live "
             "out this past as a seventy-year-old consultant. Your younger self "
             "and your wife share a life you can only watch from a distance. "
             "You must stay at least five metres from them.\n\nPARTIAL WIN: "
             "They live, but you cannot go home.",
        "D": "The scuffle kills David before ignition. Your heart stops on "
             "the console glass. The experiment never runs.\n\nReality "
             "re-weaves around a report: 'an unidentified intruder'. No one "
             "living knows who saved them.\n\nSACRIFICIAL ENDING: Two graves.",
        "E": "The weave rejects your presence. Your hands turn transparent; "
             "the corridor passes through them.\n\nThe world will never "
             "know you tried.\n\nFAILURE: Avoid your younger self, commit at "
             "the will gate, and finish before FADE reaches 100.",
    }
    return choose("ENDING " + ending + " - " + ENDING_NAMES[ending], stories[ending],
                     [("r", "Restart from the beginning"), ("q", "Quit")])


# 12. PUT THE SCENES IN ORDER AND HANDLE RESTART
def play():
    """Start a fresh game each time the player chooses R."""
    while True:
        state = new_state()
        update_status(state)
        prologue()
        lobby(state)
        ruins(state)
        ending = crossing(state)
        if ending is None:
            ending = living_base(state)
        if finish(state, ending) != "r":
            return state


# Start here when you run this file. Importing it for tests does not start a game.
if __name__ == "__main__":
    try:
        play()
    except (EOFError, KeyboardInterrupt):
        print("\nGame closed.")

