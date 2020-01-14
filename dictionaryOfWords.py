"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["maganda"] = "beautiful"
word_definitions["mahal kita"] = "I love you"
word_definitions["kumusta"] = "hello"
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print("maganda", word_definitions['maganda'])
print("kumusta", word_definitions['kumusta'])
"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (key, value) in word_definitions.items():
    print(f"{key}: {value}")