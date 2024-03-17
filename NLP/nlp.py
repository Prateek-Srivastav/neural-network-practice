import spacy
nlp = spacy.load('en_core_web_sm') # loading the language model instance in spacy
print(nlp)

# Create a Doc object
# A Doc object is a sequence of Token objects representing a lexical token.
# Each Token object has information about a particular piece—typically one word—of text.
# You can instantiate a Doc object by calling the Language object with the input string as an argument.
introduction_doc = nlp("My name is Prateek. I am a data scientist.")
print(type(introduction_doc))

print([token.text for token in introduction_doc])

# reading text from file and creating a Doc object
import pathlib
file_name = "introduction.txt"
introduction_doc = nlp(pathlib.Path(file_name).read_text(encoding="utf-8"))
print ([token.text for token in introduction_doc])

# Sentence detection
# A Doc object can be segmented into sentences by the sents attribute.
# This attribute returns a tuple of Doc objects, each representing a sentence.
# The sents attribute is a generator, so you can iterate over the sentences in the Doc using a for loop.
for sentence in introduction_doc.sents:
    print(sentence)

# You can also customize sentence detection behavior by using custom delimiters.
# Here’s an example where an ellipsis (...) is used as a delimiter, in addition to the full stop, or period (.):
ellipsis_text = ("Prateek, can you, ... never mind, I forgot"
            " what I was saying. So, do you think"
            " we should ...")

from spacy.language import Language

@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    """Add support to use `...` as a delimiter for sentence detection"""
    for token in doc[:-1]:
        if token.text == "...":
            doc[token.i+1].is_sent_start = True
    return doc

custom_nlp = spacy.load("en_core_web_sm")
custom_nlp.add_pipe("set_custom_boundaries", before="parser")
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
    print(sentence)

# For this example, the custom component set_custom_boundaries is added to the custom_nlp pipeline.
# This component sets the is_sent_start attribute of the token following an ellipsis (...) to True.
# Parsing text with this modified Language object will now treat the word after an ellipse as the start of a new sentence.
    
# Tokenization
# Building the Doc container involves tokenizing the text.
# The process of tokenization breaks a text down into its basic units—or tokens—which are represented in spaCy as Token objects.

for token in introduction_doc:
    print(token, token.idx)

# Stop words
# In the English language, some examples of stop words are the, are, but, and they. 
# With NLP, stop words are generally removed because they aren’t significant, and they heavily distort any word frequency analysis
for token in introduction_doc:
    if not token.is_stop:
        print(token)

# Lemmatization
# Lemmatization is the process of reducing inflected forms of a word while still ensuring that the reduced form belongs to the language.
# This reduced form, or root word, is called a lemma.
for token in introduction_doc:
    print(f"{str(token):>10} : {token.lemma_}")