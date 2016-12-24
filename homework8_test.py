from homework8 import *
import time

### TEST load_corpus()

t0 = time.time()
c = load_corpus("brown_corpus.txt")
print("Testing: load_corpus()")
print(time.time() - t0)
print(c[1402] == [('It', 'PRON'), ('made', 'VERB'), ('him', 'PRON'),
                  ('human', 'NOUN'), ('.', '.')])
print(c[1799] == [('The', 'DET'), ('prospects', 'NOUN'), ('look', 'VERB'),
                  ('great', 'ADJ'), ('.', '.')])

### TEST __init__():
print("Testing: __init__()")
t0 = time.time()
t = Tagger(c)
t1 = time.time()
print("__init__: ", t1 - t0)

### TEST most_probable_tags():
print("Testing: most_probable_tags()")
test1 = ["The", "man", "walks", "."]
test2 = ["The", "blue", "bird", "sings"]

t0 = time.time()
print("Is test 1 correct?", t.most_probable_tags(test1) == ['DET', 'NOUN', 'VERB', '.'])
print("Is test 2 correct?", t.most_probable_tags(test2) == ['DET', 'ADJ', 'NOUN', 'VERB'])
print("most_probable_tags: {} seconds.".format(time.time() - t0))