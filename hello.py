# print("hello world")
# print(5+5)
# # this is a single line comment
# # my name is satvik
# # i am batman
# # use ctrl+frwd slash
# '''
# this is a multi line comment
# it is made by triple quotes
# '''


# import sys
# print(sys.version)

news1 = """
Louisiana reported 27 new deaths statewide on Monday, but none in Orleans Parish, the first time the Big Easy reported no new deaths from the virus since March 22. 


Orleans Parish and the neighboring Jefferson Parish, the hardest hit areas of Louisiana, counted a combined 68 new cases Monday, with two new deaths reported in Jefferson.


However, it wasn’t to last—Orleans Parish reported four new deaths on Tuesday, with 9 in Jefferson Parish, though health officials have pointed out that daily figures can be skewed by late reporting.


The state’s coronavirus peak—for now—appears to have been in early April, when the state was seeing upwards of 1,000 new cases per day.
"""

news2 = """
The New York Times rebuked the Biden campaign on Wednesday, telling Fox News that the reported talking points that have been circulated to prominent Democrats "inaccurately" describe the paper's reporting on the candidate's accuser Tara Reade.


"Buzzfeed reported on the existence of talking points being circulated by the Biden campaign that inaccurately suggest a New York Times investigation found that Tara Reade’s allegation 'did not happen.' Our investigation made no conclusion either way," a spokesperson for the Times said in a statement. "As Buzzfeed correctly reported, our story found three former Senate aides whom Reade said she complained to contemporaneously, all of whom either did not remember the incident or said that it did not happen."
"""

try:
    from math import log10
    from sklearn.feature_extraction.text import CountVectorizer
    from collections import Counter
    import datetime
    print("All Modules Loaded ......")
except Exception as e:
    print("Some Modules are Missing : {} ".format(e))




class TextCleaner(object):


    def __init__(self, doc):
        self.doc = [str(doc)]


    def process(self):
        """
        Remove the Stop words
        :return: List []
        """
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(self.doc)
        corpus = vectorizer.get_feature_names()
        return corpus




class WordFrequency(object):


    def __init__(self, data):
        self.data = data


    def process(self):
        """
        Gets the Frequency Count
        :return: Json
        """
        data = Counter(self.data)
        return data




def main(json,query):
    helper = TextCleaner(doc=json)
    corpus = helper.process()           # get the Bags of Words


    helper = WordFrequency(data=corpus)
    corpus_freq = helper.process()      # get the Json of Words freq


    # Step 2:
    helper = TextCleaner(doc=query)
    vocubulary = helper.process()         # get the Bags of Words


    freq = []
    for key in vocubulary:
        try:
            tem = corpus_freq[key]
            freq.append(tem)
        except Exception:
            pass


    score  = sum(freq) /len(corpus)
    score = log10(len(corpus))
    return score


