from random import randint

jokes = ["What’s the best thing about Switzerland? I don't know, but the flag is a big plus.", "I invented a new word! Plagiarism!", "Hear about the new restaurant called Karma? There's no menu: You get what you deserve.", "Did you hear about the actor who fell through the floorboards? He was just going through a stage."]

# Generate a random number between 0 and the length of the jokes list
rnd_num = randint(0, len(jokes))

print(jokes[rnd_num])