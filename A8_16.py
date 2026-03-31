modes = {
    "Ionian": 1,
    "Dorian": 2,
    "Phrygian": 3,
    "Lydian": 4,
    "Mixolydian": 5,
    "Aeolian": 6
}
print(modes)
print(list(modes.items()))
print(list(modes.keys()))
print(list(modes.values()))
modes.update({"Locrian": 7})
print(modes)
