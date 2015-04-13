from mrjob.job import MRJob
import string
import nltk 

# Just a helper function that is going to strip all the punctuation away
def clean(s):
    return ''.join(c for c in s if not c in string.punctuation)

# The list of stopwords from nltk
# stopwords are words that are common and don't have much meaning alone, like "the"
STOPWORDS = nltk.corpus.stopwords.words('english')

# We start with a class that inherits from MRJob (what we imported earlier)
class WordCount(MRJob):

    # The mapper function takes in one item, line by line
    # The string of the line gets passed into "line".
    # "_" here is the position in the file, which is typically useless
    def mapper(self, _, line):
        # Clean up the line
        line = unicode(clean(line.lower()), errors='ignore')

        # split the line into tokens on whitespace
        for token in line.split():
            # If the word is a stopword, just ignore it
            if token in STOPWORDS:
                continue
                
            # yield is used to "return" words to the MapReduce framework from the mapper
            # In this case, we are basically saying "we saw 'token' once.
            yield token, 1

    # The reducer function receives a single key and a list (generator) of vaues.
    #   the key is the left side of the yield in the mapper
    #   the values are all of the items in the right side of the yield in the mapper ...
    #      ... that had that key.
    def reducer(self, key, values):
        # for example, key might be "python" and values might be "[1,1,1,1,1,1,1]"
        s = sum(values)

        # only output words that were seen more than three times
        if s > 3:
            # yield is used again here to tell the MapReduce framework we want to output
            yield key, s

    # The combiner is a mini-reduce that is performed on the map side
    # It basically does a word count on just one input split and has the same logic as the
    #    reducer here.
    combiner = reducer


if __name__ == '__main__':
    WordCount.run()




