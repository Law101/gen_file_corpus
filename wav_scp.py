#! /usr/bin/env python

import os
import os.path
import sys

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