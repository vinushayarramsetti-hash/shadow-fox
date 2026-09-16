justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]
# 1. Number of members
print("Number of members:", len(justice_league))
# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding members:", justice_league)
# 3. Move Wonder Woman to beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman:", justice_league)
# 4. Put Green Lantern between Aquaman and Flash
index = justice_league.index("Aquaman")
justice_league.insert(index + 1, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)
# 5. Replace the list
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]
print("New Justice League:", justice_league)
# 6. Sort alphabetically
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader:", justice_league[0])