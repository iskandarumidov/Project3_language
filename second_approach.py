with open("adjectives.txt") as file:
    adjectives = [line.rstrip() for line in file]
with open("nouns.txt") as file:
    nouns = [line.rstrip() for line in file]
with open("prepositions.txt") as file:
    prepositions = [line.rstrip() for line in file]
with open("verbs.txt") as file:
    verbs = [line.rstrip() for line in file]
with open("input.txt") as file:
    input = [line.rstrip() for line in file]
# print(lines)



def getSentenceMood(str):
  if str[-1] == ".":
    return "declarative"
  if str[-1] == "?":
    return "question"
  if str[-1] == "!":
    return "exclamation"
  if str[-1] == "?":
    return "question"
  return "error"

def getWordType(word):
  if word.lower() in adjectives:
    return "adjective"
  if word.lower() in nouns:
    return "noun"
  if word.lower() in prepositions:
    return "preposition"
  if word.lower() in verbs:
    return "verb"
  return "wordError"


def getNoun(sent):
  nounLen = 0
  noun = ""
  for i in range(len(sent)):
    if sent[i] != ' ':
      noun = noun + sent[i]
    else:
      if noun.lower() == "the" or noun.lower() == "a":
        print("Article: ", noun)
        nounLen = len(noun)+1
        noun = ""
      else:
        print("Noun Phrase: ", noun)
        break
  firstPerson = ["i", "me", "my"]
  if noun.lower() in firstPerson:
    print("Noun is First Person")
  else:
    print("Noun is Third Person")
  nounLen = nounLen + len(noun) + 1;
  return nounLen;

def analyzeSentence(input):
  for curSent in input.split():
    print(curSent, ": ", getWordType(curSent))

s = "Bob is a heavy drinker."
getNoun(s)
analyzeSentence(s)