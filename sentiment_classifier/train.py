# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description: 
"""

from codecs import open

from sentiment_classifier import config
from sentiment_classifier.model_classifier import Sentiment


def train(neg_file, pos_file, model_path):
    neg = open(neg_file, 'r', 'utf-8').readlines()
    pos = open(pos_file, 'r', 'utf-8').readlines()
    neg_docs = []
    pos_docs = []
    for line in neg:
        neg_docs.append(line.rstrip("\r\n"))
    for line in pos:
        pos_docs.append(line.rstrip("\r\n"))
    global classifier
    classifier = Sentiment(model_path)
    classifier.train(neg_docs, pos_docs)


def save():
    classifier.save()


def load():
    classifier.load()


def classify(sent):
    return classifier.classify(sent)


if __name__ == '__main__':
    train('data/neg.txt', 'data/pos.txt', config.sentiment_model_path)
    save()
    txt = "苹果是一家伟大的公司"
    print(txt, ' prob: ', classify(txt))
