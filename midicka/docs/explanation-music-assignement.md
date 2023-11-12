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


## Basic spells proposal

Based on these rules, the best keybindings would be those that map each Magick to a chord that musically represents its in-game effect, ensuring that Magicks with opposite elements include dissonant intervals.

| Key           | Note | MIDI | Explanation                                         |
|---------------|------|------|-----------------------------------------------------|
| Water (Q)     | C4   | 60   | Base note                                           |
| Lightning (A) | G#4  | 68   | Tritone from Water, very dissonant                  |
| Life (W)      | E4   | 64   | Major third from Water, sounds good                 |
| Arcane (S)    | B4   | 71   | Tritone from Life, dissonant                        |
| Shield (E)    | G4   | 67   | Perfect fourth from Water, neutral                  |
| Earth (D)     | C#5  | 73   | Tritone from Lightning, dissonant                   |
| Cold (R)      | A4   | 69   | Minor sixth from Water, sounds dramatic but good    |
| Fire (F)      | F4   | 65   | Perfect fourth from Cold, dissonant with Water      |

## Armonic elements

| Spell   | Notes     | MIDIs  | Keys       |
|---------|-----------|--------|------------|
| Steam   | C4, F4    | 60, 65 | Q, F       |
| Ice     | C4, A4    | 60, 69 | Q, R       |
| Poison  | C4, B4    | 60, 71 | Q, S       |

## Dissonant elements:

| Spell   | Notes     | MIDIs  | Keys       |
|---------|-----------|--------|------------|
| FAIL    | G4, G#4   | 67, 68 | E, A       |
| FAIL    | C4, G#4   | 60, 68 | A, Q       |
| FAIL    | B4, E4    | 71, 64 | S, W       |
| FAIL    | F4, A4    | 65, 69 | F, R       |

## Magicks

| Spell            | Notes                    | Combination      | MIDI IDs               |
|------------------|--------------------------|------------------|------------------------|
| Revive           | E4, G#4                  | W, A             | 64, 68                 |
| Grease           | C4, C#5, E4              | Q, D, W          | 60, 73, 64             |
| Haste            | G#4, B4, F4              | A, S, F          | 68, 71, 65             |
| Invisibility     | B4, G4, F4, C4, B4       | S, E, Q, F, S    | 71, 67, 65, 60, 71     |
| Teleport         | G#4, B4, G#4             | A, S, A          | 68, 71, 68             |
| Fear             | A4, B4, G4               | R, S, E          | 69, 71, 67             |
| Charm            | E4, G4, C#5              | W, E, D          | 64, 67, 73             |
| Thunder Bolt     | C4, F4, G#4, B4, G#4     | Q, F, A, S, A    | 60, 65, 68, 71, 68     |
| Rain             | C4, F4                   | Q, F             | 60, 65                 |
| Tornado          | C#5, C4, F4, C4, F4      | D, Q, F, Q, F    | 73, 60, 65, 60, 65     |
| Blizzard         | A4, E4, A4               | R, Q, R          | 69, 64, 69             |
| Meteor Shower    | F4, C#5, C4, F4, C#5, F4 | F, D, F, Q, D, F | 65, 73, 60, 65, 73, 65 |
| Conflagration    | C4, F4, F4, C4, F4       | Q, F, F, Q, F    | 60, 65, 65, 60, 65     |
| Thunder Storm    | C4, F4, G#4, B4, G#4     | Q, F, A, S, A    | 60, 65, 68, 71, 68     |
| Time Warp        | A4, G4                   | R, E             | 69, 67                 |
| Vortex           | A4, E4, B4, G4, E4       | R, Q, S, E, Q    | 69, 64, 71, 67, 64     |
| Raise Dead       | C4, E4, C#5, B4, A4      | Q, R, D, S, R    | 60, 64, 73, 71, 69     |
| Summon Elemental | B4, G4, C#5, C4, F4      | S, E, D, Q, F    | 71, 67, 73, 60, 65     |
| Summon Death     | B4, A4, E4, A4, B4       | S, R, Q, R, S    | 71, 69, 64, 69, 71     |
| Summon Phoenix   | E4, G#4, F4              | W, A, F          | 64, 68, 65             |
| Nullify          | B4, G4                   | S, E             | 71, 67                 |
| Crash To Desktop | G#4, G#4, F4, E4         | A, A, F, W       | 68, 68, 65, 64         |

## References

https://lparchive.org/Magicka/Tutorial%201/
