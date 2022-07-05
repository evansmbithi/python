text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. 
The highest daylight temperature of the Moon is 127 C."""

# break the paragraph into difference sentences
sentences = text.split('. ')
# print(sentences)

# find any sentences which mention temperature.
print('sentences which mention temperature.')
 
# Add code to loop through the sentences variable. 
# For each sentence, search for the word temperature. 
# If the word is found, print the sentence.
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)

# String formatting
name = 'Ganymede'
planet = 'Mars'
gravity = 1.43

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

# .format() function
print(template.format(name=name,planet=planet, gravity=gravity))