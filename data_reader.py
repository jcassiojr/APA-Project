import random
import string
import numpy as np


class DataReader(object):

    universe = list()

    def __init__(self, datasource):
        words = set()
        with open(datasource, 'r') as data:
            for line in data:
                _, _, sentence = line.split('|')
                new_words = sentence.split(' ')
                for word in new_words:
                    if word.strip() not in string.punctuation:
                        words = words.union(set([word.strip().lower()]))
        self.universe = list(words)

    def get_sentence_coordinates(self, sentence):
        sentence_nparray = np.zeros((len(self.universe)))
        self.universe
        for word in sentence.split(' '):
            word = word.strip().lower()
            index = -1
            try:
                index = self.universe.index(word)
            except:
                pass
            if index != -1:
                sentence_nparray[index] = 1
        return sentence_nparray


if __name__ == '__main__':
    datareader = DataReader()
    sentence = "7549 | 0.84722 | insightfully written , delicately performed"
    print datareader.get_sentence_coordinates(sentence)