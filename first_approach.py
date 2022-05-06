from nltk import pos_tag, word_tokenize, RegexpParser

sample_text = "Please pass me the salt."



# Find all parts of speech (PoS) in above sentence (and tokenize)
tagged = pos_tag(tokens=word_tokenize(sample_text), lang="eng")

ch = RegexpParser(grammar=
                       """
                        Adverb: {<RB>}
                        Adjective: {<JJ>}     
                        Verb: {<V.*>}   
					    Noun_Phrase: {<DT>?<JJ>*<NN>}
					    Proposition: {<IN>}
					    """)
output = ch.parse(chunk_struct=tagged, trace=0)
if output[-1] == (".", "."):
    print("MOOD: DECLARATIVE")
else:
    print("MOOD UNIDENTIFIED")
print(output)
output.draw()