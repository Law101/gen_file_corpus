#! /usr/bin/env python

import os
import os.path
import sys


# <------------------------------------------------------------------------------>

def wav_scp(folder):
    scp = []
    name_file = []
    for spk in os.listdir(f'digits_audio/{folder}'):
        for filename in os.listdir(f'digits_audio/{folder}/{spk}/recordings'):
                scp.append(os.path.join(f'/home/lawrence/kaldi/egs/yoruba/digits_audio/{folder}/{spk}/recordings/{filename}'))
                name_file.append(filename.strip('.wav'))
    return scp,name_file

with open('data/train/train_wav.scp', 'w') as train_text, open('data/test/test_wav.scp', 'w') as test_text:
    train_scp, names = wav_scp('train')
    for i in zip(names,train_scp):
        train_text.write(f'{i[0]} {i[1]}\n')

    test_scp, names = wav_scp('test')
    for j in zip(names,test_scp):
        test_text.write(f'{j[0]} {j[1]}\n')

#<------------------------------------------------------------------------------>

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

# <------------------------------------------------------------------------------------------------------------->
#Generate Utterance to Speaker
audio_train = []
audio_test = []

for folder in os.listdir('digits_audio'):
    for spk in os.listdir(f'digits_audio/{folder}'):
        if folder=='train':
            for i in os.listdir(f'digits_audio/{folder}/{spk}/recordings'):
                audio_train.append(os.path.join(f'{spk} {i}'))
        else:
            for i in os.listdir(f'digits_audio/{folder}/{spk}/recordings'):
                audio_test.append(os.path.join(f'{spk} {i}'))

with open('data/train/train_utt2spk.txt', 'w') as train_text, open('data/test/train_utt2spk.txt', 'w') as test_text:
    for file in audio_train:
        train_text.write(f'{file}\n')

    for file in audio_test:
        test_text.write(f'{file}\n')

# <------------------------------------------------------------------------------------------------------------->

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
