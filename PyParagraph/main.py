#Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:
#Import a text file filled with a paragraph of your choosing.
#Assess the passage for each of the following:
#Approximate word count
#Approximate sentence count
#Approximate letter count (per word)
#Average sentence length (in words)


import os
import re


def average_sentences(sentences,words):
    return (words/sentences)


def average_letter_count(paragraph, words):
    letters = len(paragraph)
    avg = letters/words
    return avg


def sentence_count(paragraph):
    sentences = re.split("[\.;,]", paragraph)
    return len(sentences)


def word_count(paragraph):
#    sentences = re.split("(?&lt;=[.!?]) +", paragraph)
    sentences = re.split(" ", paragraph)
    return len(sentences)


def report(words, sentences, average_word, average_sentence):
    print('Paragraph Analysis')
    print('-------------------------------')
    print('Word count approximates '+str(words))
    print('Sentence cont approximates '+ str(sentences))
    print('Average letter counts in a word '+ str(average_word))
    print('Average sentence count '+ str(average_sentence))


def pyParagraph(input):
#    for filename in input:
#        filepath = os.path.join('data',filename)
        filepath = os.path.join('data',input)

        with open(filepath,'r') as paragraph:
            lines = paragraph.read()
            wc = word_count(lines)
            sc = sentence_count(lines)
            av_letter = average_letter_count(lines, wc)
            av_sentences = average_sentences(sc,wc)

            report(wc,sc,av_letter,av_sentences)

#files = ('paragraph_1.txt','paragraph_2.txt')
files = 'paragraph_1.txt'
pyParagraph(files)

