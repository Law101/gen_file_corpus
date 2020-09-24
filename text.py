#! /usr/bin/env python

import os
import os.path
import sys

def text(folder_name):
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
            place.append(new_val)
    return place

with open('data/train/train_text.txt', 'w') as train_text, open('data/test/test_text.txt', 'w') as test_text:
    train_plain = text('train')
    for pair in train_plain:
        train_text.write(f'{pair}\n')
    
    test_plain = text('test')
    for pair in test_plain:
        test_text.write(f'{pair}\n')