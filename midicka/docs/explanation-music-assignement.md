# Explanation of musiºc assigment

The explanation look for an innovative approach of integrating music theory
with the gameplay mechanics of Magicka.
It offers a unique perspective by assigning musical notes and MIDI values to game elements,
creating an auditory dimension where spells have their own harmonies or dissonances.

This guide explains how opposite elements produce tension through dissonant intervals,
while compatible combinations create consonance,
enhancing the gameplay experience through the principles of music theory.

## Mapping

Mapping piano notes through MIDI to actions in a game like Magicka
can create a unique and immersive gameplay experience.
By assigning MIDI values to specific in-game actions,
players can use a piano keyboard to control their characters, casting spells
and navigating the game world with musical keys instead of traditional game controls.

This setup could benefit from creating a playful, creative environment and may even help players develop their musical skills while gaming.

For example,
assigning the MIDI note C4 (with a MIDI value of 60) to cast the "Fire" spell (Key F in the game),
and E4 (MIDI value of 64) to cast "Water" (Key Q in the game),
would allow a player to play these notes on a piano to cast these spells in-game.

To map piano notes to elements in a way that reflects their opposition in Magicka,
you can use dissonant intervals for opposing elements and consonant intervals for compatible elements.

## A first attempt

Here's my first iteration of how you could assign notes:

- Water (Q): C4 (MIDI 60)
  - Opposite Lightning (A): F#4/Gb4 (MIDI 66) — Tritone, dissonant.
- Lightning (A): F#4/Gb4 (MIDI 66)
  - Opposite Earth (D): C#5/Db5 (MIDI 73) — Tritone, dissonant.
- Life (W): D4 (MIDI 62)
  - Opposite Arcane (S): Ab4/G#4 (MIDI 68) — Tritone, dissonant.
- Arcane (S): Ab4/G#4 (MIDI 68)
  - Opposite Life (W): D4 (MIDI 62) — Tritone, dissonant.
- Shield (E): G4 (MIDI 67) — Perfect fourth, neutral sound.
- Earth (D): C#5/Db5 (MIDI 73)
  - Opposite Lightning (A): F#4/Gb4 (MIDI 66) — Tritone, dissonant.
- Cold (R): F4 (MIDI 65)
  - Opposite Fire (F): B4 (MIDI 71) — Perfect fifth, consonant but forms a diminished fifth when combined with F4, dissonant.
- Fire (F): B4 (MIDI 71)
  - Opposite Cold (R): F4 (MIDI 65) — Perfect fifth, consonant but forms a diminished fifth when combined, dissonant.

According to Music Theory Rules:

- Consonant intervals: thirds, sixths, perfect fifths — harmonically pleasing.
- Dissonant intervals: seconds, sevenths, tritones — create tension.
- "Great" sounding chords: major or minor triads, seventh chords.
- "Wrong" sounding chords: diminished, augmented, or non-triadic dissonances.

Examples:

- Magick "Revive" (W-A): D4 (W), F#4/A (A) — D major chord, consonant.
- Magick "Confuse" (S-E-A): Ab4/G#4 (S), C5 (E), F#4/Gb4 (A) — Diminished chord, dissonant.


### Basic spells proposal

Based on these rules, the best keybindings would be those that map each Magick to a chord that musically represents its in-game effect, ensuring that Magicks with opposite elements include dissonant intervals.

| Note    | MIDI Value | Key           | Reasoning                                          |
|---------|------------|---------------|----------------------------------------------------|
| C4      | 60         | Water (Q)     | Base note                                          |
| G#4/Ab4 | 68         | Lightning (A) | Tritone from Water, very dissonant                 |
| E4      | 64         | Life (W)      | Major third from Water, sounds good                |
| B4      | 71         | Arcane (S)    | Tritone from Life, dissonant                       |
| G4      | 67         | Shield (E)    | Perfect fourth from Water, neutral                 |
| C#5/Db5 | 73         | Earth (D)     | Tritone from Lightning, dissonant                  |
| A4      | 69         | Cold (R)      | Minor sixth from Water, sounds dramatic but good   |
| F4      | 65         | Fire (F)      | Perfect fourth from Cold, but dissonant with Water |

### Magicks

| Combination | Notes                         | MIDI IDs                | Result             |
|-------------|-------------------------------|-------------------------|--------------------|
| W-A         | E4, G#4/Ab4                   | 64, 68                  | Revive             |
| Q-D-W       | C4, C#5/Db5, E4               | 60, 73, 64              | Grease             |
| A-S-F       | G#4/Ab4, B4, F4               | 68, 71, 65              | Haste              |
| S-E-QF-S    | B4, G4, F4, C4, B4            | 71, 67, 65, 60, 71      | Invisibility       |
| A-S-A       | G#4/Ab4, B4, G#4/Ab4          | 68, 71, 68              | Teleport           |
| R-S-E       | A4, B4, G4                    | 69, 71, 67              | Fear               |
| W-E-D       | E4, G4, C#5/Db5               | 64, 67, 73              | Charm              |
| QF-A-S-A    | C4+F4, G#4/Ab4, B4, G#4/Ab4  | 60+65, 68, 71, 68       | Thunder Bolt       |
| Q-QF        | C4, C4+F4                     | 60, 60+65               | Rain               |
| D-QF-Q-QF   | C#5/Db5, C4+F4, C4, C4+F4    | 73, 60+65, 60, 60+65    | Tornado            |
| R-RQ-R      | A4, A4+E4, A4                 | 69, 69+64, 69           | Blizzard           |
| F-D-FQ-D-F  | F4, C#5/Db5, F4+C4, C#5/Db5, F4 | 65, 73, 65+60, 73, 65 | Meteor Shower      |
| QF-F-FQ-F-FQ| C4+F4, F4, C4+F4, F4, C4+F4  | 60+65, 65, 60+65, 65, 60+65 | Conflagration   |
| QF-QF-A-S-A | C4+F4, C4+F4, G#4/Ab4, B4, G#4/Ab4 | 60+65, 60+65, 68, 71, 68 | Thunder Storm |
| R-E         | A4, G4                        | 69, 67                  | Time Warp          |
| RQ-S-RQ-E-RQ| A4+E4, B4, A4+E4, G4, A4+E4  | 69+64, 71, 69+64, 67, 69+64 | Vortex         |
| QR-D-S-R    | C4+E4, C#5/Db5, B4, A4       | 60+64, 73, 71, 69       | Raise Dead        |
| S-E-D-QF-S  | B4, G4, C#5/Db5, C4+F4, B4   | 71, 67, 73, 60+65, 71   | Summon Elemental  |
| S-R-RQ-R-S  | B4, A4, A4+E4, A4, B4        | 71, 69, 69+64, 69, 71   | Summon Death      |
| W-A-F       | E4, G#4/Ab4, F4               | 64, 68, 65              | Summon Phoenix    |
| S-E         | B4, G4                        | 71, 67                  | Nullify           |
| A-A-F-W     | G#4/Ab4, G#4/Ab4, F4, E4     | 68, 68, 65, 64          | Crash To Desktop  |


## References

https://lparchive.org/Magicka/Tutorial%201/
