############################################################
# CIS 521: Homework 8
############################################################

student_name = "James Wang"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
from collections import defaultdict
import math

############################################################
# Section 1: Hidden Markov Models
############################################################


def load_corpus(path):
    with open(path, "r") as f:
        lst = [j.split() for j in [i.strip() for i in f]]
        return [[tuple(j.split("=")) for j in i] for i in lst]


class Tagger(object):

    def __init__(self, sentences):
        ### initial tag probabilities
        pos1_tags = [i[0][1] for i in sentences]
        unq_tags = list(set(pos1_tags))
        self.init_probs = {i: math.log(sum([1 for j in pos1_tags if j == i]) / float(len(sentences)))
                           for i in unq_tags}

        ### transition probabilities
        # bigram counts
        tags_lst = [[j[1] for j in i] for i in sentences]
        tag_bigrams = defaultdict(float)
        for lst in tags_lst:
            idx = 1
            while idx < len(lst):
                tag_bigrams[(lst[idx-1], lst[idx])] += 1
                idx += 1
        # all tag counts
        trunc_tags_lst = []
        map(trunc_tags_lst.extend, [i[:-1] for i in tags_lst])
        all_tag_probs = defaultdict(float)
        for i in trunc_tags_lst:
            all_tag_probs[i] += 1
        # tag transition probs
        self.tran_probs = {key: math.log(float(tag_bigrams[key]) / all_tag_probs[key[0]])
                           for key in tag_bigrams}

        ### emission probabilities
        trunc_sentences = []
        map(trunc_sentences.extend, sentences)
        self.emit_probs = defaultdict(dict)
        smoothing = 1e-10
        adv_dict = []
        noun_dict = []
        adp_dict = []
        prt_dict = []
        det_dict = []
        punc_dict = []
        pron_dict = []
        verb_dict = []
        x_dict = []
        num_dict = []
        conj_dict = []
        adj_dict = []
        for i in trunc_sentences:
            if i[1] == "ADV":
                adv_dict.append(i[0])
            elif i[1] == "NOUN":
                noun_dict.append(i[0])
            elif i[1] == "ADP":
                adp_dict.append(i[0])
            elif i[1] == "PRT":
                prt_dict.append(i[0])
            elif i[1] == "DET":
                det_dict.append(i[0])
            elif i[1] == ".":
                punc_dict.append(i[0])
            elif i[1] == "PRON":
                pron_dict.append(i[0])
            elif i[1] == "VERB":
                verb_dict.append(i[0])
            elif i[1] == "X":
                x_dict.append(i[0])
            elif i[1] == "NUM":
                num_dict.append(i[0])
            elif i[1] == "CONJ":
                conj_dict.append(i[0])
            elif i[1] == "ADJ":
                adj_dict.append(i[0])
            else:
                next
        subsets = [adv_dict, noun_dict, adp_dict, prt_dict, det_dict, punc_dict,
                   pron_dict, verb_dict, x_dict, num_dict, conj_dict, adj_dict]
        for i, j in zip(unq_tags, subsets):
            subset = j
            word_probs = defaultdict(float)
            for word in subset:
                word_probs[word] += 1
            # laplace smoothing
            word_probs["<UNK>"] = smoothing / (len(subset) + smoothing * len(set(subset)))
            self.emit_probs[i] = {word: math.log(word_probs[word] / len(subset))
                                  for word in word_probs}

    def most_probable_tags(self, tokens):
        all_tags = []
        for i in tokens:
            tag_candidates = []
            for j in self.emit_probs:
                tag_dict = self.emit_probs[j]
                if i in tag_dict.keys():
                    tag_candidates.append((j, tag_dict[i]))
                else:
                    tag_candidates.append((j, tag_dict["<UNK>"]))
            all_tags.append(tag_candidates)
        return [sorted(i, key=lambda x: x[1], reverse=True)[0][0] for i in all_tags]

    def viterbi_tags(self, tokens):
        pass

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
9 hours
"""

feedback_question_2 = """
The assignment was reasonably challenging, although the lecture slides and TA's
provided good guidance through the problems.
"""

feedback_question_3 = """
This was a very unique way of looking at speech and I'm surprised at how we've
broken down something as complicated as language in such a systematic manner.
I wonder how HMMs perform of non-English languages...
"""
