# The Way Home — All Choices and Endings


## Ending overview

| Ending | Name | Trigger | Outcome |
|---|---|---|---|
| A | THE WAY HOME | David co-signs; correct override answer; survive the final action | Stop the experiment, save your wife, return home with your memories. |
| B | A STRANGER'S KITCHEN | David permits access but does not co-sign; correct override answer; survive | Stop the experiment and return to your wife, but lose the old timeline's memories. |
| C | FIVE METERS | Open VENT 2 after waiting for the technician; survive the action | Stop the experiment, but destroy the return channel and remain in the past. |
| D | TWO GRAVES | Confirm rushing the console; survive the FADE check | The struggle kills David and the player: sacrificial ending. |
| E | FADE | Step back at the will gate, approach your younger self, or reach 100 FADE | Dissolution/failure. |

An action that brings FADE to 100 produces E **before** its intended A/B/C/D
outcome. Ending routes assume enough FADE remains.

## Main branch map

```text
Prologue: learn David's wish for a way home
  |
Lobby: scan casing -> solve levers -> power restored
  |
Ruins: recover badge -> scan diary -> enter 2322
  |
Will gate
  +-- Step back -------------------------------------------- E
  |
  +-- Proceed -> Living base
                   |
                   +-- David
                   |    +-- Photo -> permission, no co-sign
                   |    |             -> override + "home" -- B
                   |    +-- Diary -> permission + co-sign
                   |                  -> override + "home" -- A
                   |
                   +-- Coolant room -> code 1473 -> wait
                   |                                  -> VENT 2 -- C
                   |
                   +-- Experiment hall -> rush -> confirm -- D
                   |
                   +-- Canteen -> approach younger self ---- E
                   |
                   +-- Any paid action reaching 100 FADE --- E
```

David's choice does not force an immediate ending. You can still choose sabotage
or assault afterwards. Completing his conversation locks in the photo/diary
decision for that run: revisiting him does not offer the choice again.

## 1. Prologue

No branching choices: read the archive, interview, accident report and rules.

Important clue: David says, “I'm building a way home.”
This supports the final override answer: **home**, **go home**, or **to go home**.

## 2. Lobby: restore power

### Lobby menu

| Choice | Result |
|---|---|
| 1 — Scan the shielded panel casing | Enables lever use. Saves the panel note and Zhou's warning: never open VENT 2 before ignition, because it disables the core and destroys the return channel. |
| 2 — Use the control panel, before scanning | Refused; return to lobby. |
| 2 — Use the control panel, after scanning | Opens the lever puzzle. |
| 3 — Read notebook | Read saved clues; return to lobby. |

Scanning again is allowed. All lobby actions are free of FADE.

### Lever choices

Indicators start in this order: MAIN, AUX, COOL, ANCHOR.
Initial state: **TRIPPED, LOCKED, TRIPPED, LOCKED**.
The goal is to make all four LOCKED.

| Choice | Lever | Indicators toggled |
|---|---|---|
| 1 | Alpha | MAIN, AUX, COOL |
| 2 | Beta | AUX, COOL, ANCHOR |
| 3 | Gamma | MAIN, COOL, ANCHOR |
| 4 | Delta | MAIN, AUX, ANCHOR |
| 5 | Step back | Return to lobby; lever states and move count remain. |

Toggling reverses an indicator: LOCKED becomes TRIPPED and vice versa.
A successful pull immediately restores power and ends the puzzle.

**Shortest solution from the initial state: Beta (2), then Delta (4).**
Delta then Beta also works. These are separate menu entries, not the text “24”.

Hints:
- After the fourth unsuccessful pull: notice that each lever flips several indicators.
- From the eighth unsuccessful pull onward: show the full lever mapping.
- Pulling the same lever twice cancels its effect, unless the first pull already
  completed the puzzle.

## 3. Ruined base: badge, diary and calibration

### Corridor menu

| Choice | Result |
|---|---|
| 1 — Examine collapsed panel | If the badge is missing, choose how to retrieve it. If already collected, show “Empty gap”. |
| 2 — Enter control room | Locked without the badge; otherwise opens the control-room menu. |
| 3 — Calibrate the core | Refused without the diary; otherwise opens the calibration puzzle. |
| 4 — Read notebook | Read clues and return. |

### Badge choices

| Choice | Result |
|---|---|
| 1 — Pry the panel | Obtain Dr. Lin's badge; shoulder-discomfort text only, no penalty. |
| 2 — Look for a gap | Obtain the same badge; different description, same game state. |

### Control-room choices

| Choice | Result |
|---|---|
| 1 — Scan David's diary | Save revised time 04:16, his private words and the mathematical-operation clue. Enables calibration and later diary dialogue. |
| 2 — Return to corridor | Leave without collecting anything new. |

The diary is mandatory for calibration, so its dialogue option is available in
every normal playthrough that reaches David.

### Calibration

Use shift 2: add, subtract, multiply and divide the respective digits.
Then swap the first and third digits, and the second and fourth digits.

```text
Example: 1234 -> 3062 -> 6230
Diary:   0416 -> 2223 -> 2322
```

To discover shift 2, undo the example's swaps: 6230 -> 3062.
Then compare 1+2=3, 2-2=0, 3*2=6, and 4/2=2.

| Input/condition | Result |
|---|---|
| 2322 | Calibration succeeds; advance to the crossing. |
| Wrong answer | Increment failure count, display hint, return to corridor. Choose corridor option 3 to retry. |
| First failure | Hint about four equations sharing one shift. |
| Second and subsequent failures | Reveal shift 2 and remind the player about swaps. |
| After three failures | On the next calibration attempt, replace text entry with the fallback menu. |

Fallback menu:
- **1 — 2100:** wrong; return to corridor.
- **2 — 0416:** wrong; this is the unencoded time.
- **3 — 2322:** correct; advance.

Calibration failure count persists while revisiting rooms in this stage.
There is no FADE cost. Text answers are normalised by removing non-alphanumeric
characters and converting letters to lowercase.

## 4. Will gate

| Choice | Result |
|---|---|
| 1 — Proceed into the past | Enter the living base with FADE 0. |
| 2 — Step back | Immediate ending E, even though FADE is still 0. |

## 5. Living-base navigation and FADE

| Choice | Destination | Effect |
|---|---|---|
| 1 | Preparation room | Talk to David. |
| 2 | Coolant room | Door puzzle, technician and vents. |
| 3 | Experiment hall | Override or assault. |
| 4 | Canteen window | See your wife and younger self. |
| 5 | Notebook | Free; remain in corridor. |

Visiting destinations 1–4 costs **4 FADE outward**.
Returning without an ending costs **another 4 FADE**.
An ending ends the visit immediately, so there is no return-trip cost.
If outward travel reaches 100, the destination interaction never begins.

## 6. David conversation

### Identity

| Choice | Result | Extra FADE |
|---|---|---|
| 1 — Tell the truth about building the machine | David recognises you; advance to his creed question. | 4 |
| 2 — Claim to be an inspector | Lie fails; repeat identity menu. | 4 per attempt |
| 3 — Leave | Return to corridor without his permission. | No conversation cost; return travel still costs 4 |

### His creed

| Choice | Result | Extra FADE |
|---|---|---|
| 1 — Remind him of his promise of a way home | Advance to the evidence choice. | 4 |
| 2 — Leave the conversation | Return without completing his authorisation. | No cost for this choice; return travel still costs 4 |

If you leave early, the incomplete conversation is not saved; a later visit
starts again with the identity question.

### Why you came: evidence

| Choice | David's response | State/outcome | Extra FADE |
|---|---|---|---|
| 1 — Wife's photograph | He sympathises and steps aside, but will not co-sign on this evidence alone. | david_ready=True, cosign=False. Correct override leads to B. | 4 |
| 2 — Quote his diary | He recognises private words he just wrote and agrees to help. | david_ready=True, cosign=True. Correct override leads to A. | 4 |

The current code includes the photograph response (“He steps aside”).
Both choices return to the corridor after the response.
Once david_ready is True, revisiting David only shows “David is waiting”.
It does not let you change your evidence choice. Restart to test the other branch.

## 7. Coolant-room route

### Maintenance door

The badge does not open this door. It requires a separate code.

| Choice | Result |
|---|---|
| 1 — View coordinate diagrams | Show four dot grids and coordinate lists; return to keypad menu. |
| 2 — Enter code | Ask for the four-digit answer. |
| 3 — Return to corridor | Leave; normal return travel costs 4 FADE. |

Diagram data, in order:
1. (3,6), (3,0) — intended digit **1**.
2. (4,6), (1,3), (4,3), (4,0) — intended digit **4**.
3. (1,6), (5,6), (2,0) — intended digit **7**.
4. (1,6), (3,6), (5,5), (3,3), (2,3), (5,1), (3,0), (1,0) — intended digit **3**.

The code is **1473**. The program checks the typed code, not a drawing.
It does not give explicit stroke-connection instructions.

| Input/condition | Result |
|---|---|
| 1473 | Unlock door permanently for this run; save code in notebook; advance to technician. |
| Other input | Retry for free. Unlike calibration, internal punctuation is not removed. |
| Two or three wrong attempts | Hint that the shapes are handwritten digits. |
| Four or more wrong attempts | Reveal 1473. |

Leaving before unlocking resets the door-puzzle failure counter on the next
visit. Once unlocked, future visits skip the keypad entirely.

### Technician

| Choice | Result |
|---|---|
| 1 — Act while watched | Add 19 FADE (4 action + 15 alarm). If alive, get escorted out and pay 4 return travel. If FADE reaches 100, E. |
| 2 — Wait in the shadows | No extra FADE; advance to vent choices. |
| 3 — Leave | Return to corridor; pay 4 return travel. |

A caught visit from the corridor costs **27 total FADE** if you survive:
4 outward + 19 caught + 4 return.

### Vents

| Choice | Result |
|---|---|
| 1 — Bleed VENT 1 | Add 4 FADE; no effect; repeat vent menu if alive. |
| 2 — Bleed VENT 2 | Add 4 FADE; if alive, ending C. Otherwise E. |
| 3 — Bleed VENT 3 | Add 4 FADE; no effect; repeat vent menu if alive. |
| 4 — Read notebook | Free; return to vent menu. |
| 5 — Leave | Return to corridor; pay 4 return travel. |

“Bleed” means open the vent to release fluid or gas.
Zhou's earlier warning identifies VENT 2 and explains why sabotage also destroys
your route home. David's permission is not required for this ending.

## 8. Experiment hall

| Choice | Result |
|---|---|
| 1 — Use designer override, without David's permission | Show “Override locked”; return to corridor. |
| 1 — Use designer override, with permission | Open passphrase puzzle. |
| 2 — Rush the console | Open confirmation menu. |
| 3 — Leave | Return to corridor. |

### Override answer

Accepted normalised answers: **home**, **gohome**, **togohome**.
Examples accepted: “HOME”, “go home”, “To go home!”.

| Input/condition | Result |
|---|---|
| Correct answer, cosign=True | Add 4 FADE; if alive, A. |
| Correct answer, cosign=False | Add 4 FADE; if alive, B. |
| Correct answer reaches 100 FADE | E instead of A/B. |
| Wrong answer | No FADE cost; remain at override, show hint and retry. |
| First failure | Hint that David once explained his purpose. |
| Second or later failure | Quote the interview about a way home. |
| After three failures | Next attempt uses fallback menu. |

Fallback choices:
1. Fame — wrong.
2. **To go home — correct.**
3. Endless energy — wrong.
4. Power — wrong.

Unlike calibration, incorrect override answers do **not** return to the corridor.

### Assault confirmation

| Choice | Result |
|---|---|
| 1 — Proceed | Add 4 FADE; if alive, D; if FADE reaches 100, E. |
| 2 — Step away | Cancel assault and return to corridor. |

You do not need to talk to David first to choose assault.

## 9. Canteen window

| Choice | Result |
|---|---|
| 1 — Keep walking | Return to corridor; total visit costs 8 FADE. |
| 2 — Approach them | Immediate E; no further FADE cost beyond the outward trip. |

## 10. Exact routes to test every ending

### Shared opening for the full game

1. Read the prologue.
2. Lobby **1**: scan; read the warning and scan results.
3. Lobby **2**: enter lever panel.
4. Lever **2** (Beta), then **4** (Delta): restore power.
5. Ruins **1**: examine panel; choose **2** (gap). Choice 1 also gets the badge.
6. Ruins **2**: enter control room; choose **1** to scan diary.
7. Ruins **3**: calibrate; enter **2322**.

If using the temporary test start, begin at step 5.

### A — Full win

After the shared opening:
1. Will gate **1**: proceed.
2. Living base **1**: David.
3. Identity **1**: truth.
4. Creed **1**: remind him of his promise.
5. Evidence **2**: diary.
6. Living base **3**: experiment hall.
7. Hall **1**: override.
8. Enter **home**.

Expected: **A**, final FADE **28**.

### B — Return without memories

Follow A's route, but at the evidence question choose **1 — photograph**.

Expected: **B**, final FADE **28**.

### C — Sabotage, stranded in the past

After the shared opening:
1. Will gate **1**.
2. Living base **2**: coolant room.
3. Keypad **2**: enter **1473**. Viewing diagrams is optional.
4. Technician **2**: wait.
5. Vents **2**: open VENT 2.

Expected: **C**, final FADE **8**.

### D — Sacrificial assault

After the shared opening:
1. Will gate **1**.
2. Living base **3**: experiment hall.
3. Hall **2**: rush.
4. Confirmation **1**: proceed.

Expected: **D**, final FADE **8**.

### E — Three distinct failure routes

- **Will gate:** after the shared opening, choose gate **2**.
  Expected E with FADE **0**.
- **Younger self:** gate **1**, living base **4**, approach **2**.
  Expected E with FADE **4**.
- **FADE exhaustion:** gate **1**; repeat living base **4**, then
  “Keep walking” **1**, twelve times (FADE 96). Choose living base **4**
  once more. Outward travel reaches 100 before the canteen menu.
  Expected E with FADE **100**.

## 11. Restart and quit

Every ending offers:
- **R:** restart with a new state: FADE 0, no badge, diary, notes, unlocked door,
  power, calibration or David permission. The full game repeats its prologue
  and lobby when those calls are enabled.
- **Q:** quit. The display restores the terminal.

There is no save/load system. Exiting does not preserve progress.

