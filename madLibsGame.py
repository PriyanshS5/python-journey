# Mad Libs game 
# It is where you have a story but the user gets to submit nouns verbs adjectives within your story.

# noun1 = input ("Enter noun 1: ")
# adjective1 = input ("Enter adjective 1: ")
# verb1 = input ("Enter verb 1: ")
# print(f"The {adjective1} {noun1} decided to {verb1} on my breakfast table.")
# noun2 = input ("Enter noun 2: ")
# adjective2 = input ("Enter adjective 2: ")
# verb2 = input ("Enter verb 2: ")
# print(f"Yesterday, a {adjective2} {noun2} began to {verb2} inside the bathroom.")
# noun3 = input ("Enter noun 3: ")
# adjective3 = input ("Enter adjective 3: ")
# verb3 = input ("Enter verb 3: ")
# print(f"My neighbor's {adjective3} {noun3} loves to {verb3} whenever music plays.")
# noun4 = input ("Enter noun 4: ")
# adjective4 = input ("Enter adjective 4: ")
# verb4 = input ("Enter verb 4: ")
# print(f"At school, the {adjective4} {noun4} suddenly started to {verb4} during class.")
# noun5 = input ("Enter noun 5: ")
# adjective5 = input ("Enter adjective 5: ")
# verb5 = input ("Enter verb 5: ")
# print(f"Last night, a {adjective5} {noun5} tried to {verb5} through my window.")


import random

adjectives = ["smelly", "crazy", "hairy", "tiny", "sleepy"]
nouns = ["banana", "teacher", "dinosaur", "robot", "pillow"]
verbs = ["dance", "scream", "jump", "crawl", "sing"]

sentence1 = f"The {random.choice(adjectives)} {random.choice(nouns)} decided to {random.choice(verbs)} on my breakfast table."

sentence2 = f"Yesterday, a {random.choice(adjectives)} {random.choice(nouns)} began to {random.choice(verbs)} inside the bathroom."

sentence3 = f"My neighbor's {random.choice(adjectives)} {random.choice(nouns)} loves to {random.choice(verbs)} whenever music plays."

sentence4 = f"At school, the {random.choice(adjectives)} {random.choice(nouns)} suddenly started to {random.choice(verbs)} during class."

sentence5 = f"Last night, a {random.choice(adjectives)} {random.choice(nouns)} tried to {random.choice(verbs)} through my window."

print(sentence1)
print(sentence2)
print(sentence3)
print(sentence4)
print(sentence5)


