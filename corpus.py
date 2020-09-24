#! /usr/bin/env python

import os
import os.path
import sys


def corpus(folder_name):
    utt = []
    for spk in os.listdir(f'digits_audio/{folder_name}'):
        with open(f'digits_audio/{folder_name}/{spk}/utts.data', 'r') as filehandler:
            cont = filehandler.readlines()
            utt.append(cont)
    place = []
    for spk in utt:
        for utterance in spk:
            new_val = utterance.strip('\n')
            new_val = new_val.strip('(')
            new_val = new_val.strip(')')
            new_val = new_val.strip(' ')
            new_val = new_val.split()[1:]
            new_val = ' '.join(new_val)
            place.append(new_val)
    return place

with open('data/local/corpus.txt', 'w') as train_text:
    train_plain = corpus('train')
    test_plain = corpus('test')
    for train_pair in train_plain:
        train_text.write(f'{train_pair}\n')
    for test_pair in test_plain:
        train_text.write(f'{test_pair}\n')
