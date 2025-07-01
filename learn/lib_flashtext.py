#Quick search and string replacement
from flashtext import KeywordProcessor

kp = KeywordProcessor()
kp.add_keyword("JavaScript", "JS")

text = "I love JavaScript!"
result = kp.replace_keywords(text)

print(result)
