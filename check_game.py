"""Optional checks. This file is NOT needed to play the game.

Run: python3 check_game.py
It sends scripted keyboard answers to main.py, like a player testing the game.
The game itself has no imports; these testing tools are standard-library tools.
"""

import subprocess
import sys
from pathlib import Path


folder = Path(__file__).resolve().parent


def start_answers():
    return [
        "", "", "",                  # Read the three introduction pages.
        "1", "",                      # Scan lobby and read the clues.
        "2", "3", "2", "1", "4", "", # Set breakers; read success message.
        "1", "2", "",                 # Recover badge through the gap.
        "2", "1", "",                 # Enter control room and scan diary.
        "3", "04:17", "",             # Calibrate and read success message.
        "", "1", "",                  # Read rules, cross, read arrival.
    ]


def finish_answers(ending):
    if ending == "A":
        return ["1", "1", "", "1", "", "2", "", "3", "1", "home", "q"]
    if ending == "B":
        return ["1", "1", "", "1", "", "1", "", "3", "1", "home", "q"]
    if ending == "C":
        return ["2", "2", "2", "", "q"]
    if ending == "D":
        return ["3", "2", "1", "q"]
    return ["4", "2", "q"]


def check(name, answers, expected):
    result = subprocess.run(
        [sys.executable, str(folder / "main.py")],
        input="\n".join(answers) + "\n",
        capture_output=True,
        text=True,
        timeout=10,
        cwd=folder,
    )
    assert result.returncode == 0, result.stderr
    assert "Traceback" not in result.stderr
    for phrase in expected:
        assert phrase in result.stdout, name + ": missing " + phrase
    print("PASS:", name)
    return result.stdout


if __name__ == "__main__":
    for ending in "ABCDE":
        check("Ending " + ending, start_answers() + finish_answers(ending),
              ["ENDING " + ending])

    # Restart C -> A, including a fresh scan, badge, diary and calibration.
    first_run = start_answers() + finish_answers("C")[:-1] + ["r"]
    output = check("Restart C to A", first_run + start_answers() + finish_answers("A"),
                   ["ENDING C", "ENDING A"])
    assert output.count("Badge recovered") == 2
    assert output.count("RUINS | Lobby | FADE: 0 / 100") == 2

    check("Unknown menu input",
          ["", "", "", "99", "hello"] + start_answers()[3:] + finish_answers("A"),
          ["Please enter one of the choices shown.", "ENDING A"])

    # Invalid breaker order four times, then the correct order.
    answers = ["", "", "", "1", ""]
    answers += ["2", "5", "5", "5", "5", ""] * 4
    answers += start_answers()[5:] + finish_answers("A")
    check("Breaker retries and hints", answers,
          ["Wrong breaker order", "3, 2, 1, 4.", "ENDING A"])

    # Try the control room and calibration before obtaining the required items.
    answers = start_answers()[:11] + ["2", "", "3", ""]
    answers += start_answers()[11:] + finish_answers("A")
    check("Badge and diary dependencies", answers,
          ["Control room locked", "Calibration needs evidence", "ENDING A"])

    # Wrong time three times causes a numbered fallback.
    answers = start_answers()[:17]
    answers += ["3", "21:00", "", "3", "wrong", "", "3", "", "", "3", "2", ""]
    answers += start_answers()[20:] + finish_answers("A")
    check("Time fallback", answers, ["Calibration fallback", "ENDING A"])

    for time_text in ["0417", "4:17", " 04:17 "]:
        answers = start_answers()
        answers[18] = time_text
        check("Time format " + repr(time_text), answers + finish_answers("A"), ["ENDING A"])

    for passphrase in ["GO HOME", " To go home! "]:
        answers = finish_answers("A")
        answers[-2] = passphrase
        check("Passphrase " + repr(passphrase), start_answers() + answers, ["ENDING A"])

    answers = start_answers() + finish_answers("A")[:-2]
    answers += ["bad", "", "bad", "", "bad", "", "1", "", "2", "q"]
    check("Passphrase fallback", answers, ["Override fallback", "ENDING A"])

    check("Will gate failure", start_answers()[:-2] + ["2", "q"], ["ENDING E"])

    check("FADE exhaustion through travel", start_answers() + ["4", "1"] * 12 + ["4", "q"],
          ["FADE: 100 / 100", "ENDING E"])

    answers = start_answers() + ["2", "1", "", "2", "2", "1", "", "4", "", "2", "", "q"]
    check("Alarm and wrong vent recovery", answers,
          ["Caught", "Nothing changes", "ENDING C", "FADE: 39 / 100"])

    answers = start_answers() + ["3", "1", "", "1", "2", "", "1", "", "1", "", "2", "", "3", "1", "home", "q"]
    check("Locked override and failed lie recovery", answers,
          ["Override locked", "The lie fails", "ENDING A"])

    check("Quit at introduction", ["q"], ["Thanks for playing."])
    check("Clean end-of-input", [], ["Game closed."])
    print("All 22 checks passed.")
