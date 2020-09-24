#! /usr/bin/env python

import os
import os.path
import sys

audio_train = []
audio_test = []

for folder in os.listdir('digits_audio'):
    for spk in os.listdir(f'digits_audio/{folder}'):
        if folder=='train':
            for i in os.listdir(f'digits_audio/{folder}/{spk}/recordings'):
                audio_train.append(os.path.join(f"{i.strip('.wav')} {spk}"))
        else:
            for i in os.listdir(f'digits_audio/{folder}/{spk}/recordings'):
                audio_test.append(os.path.join(f"{i.strip('.wav')} {spk}"))

with open('data/train/utt2spk', 'w') as train_text, open('data/test/utt2spk', 'w') as test_text:
    for file in audio_train:
        train_text.write(f'{file}\n')

    for file in audio_test:
        test_text.write(f'{file}\n')
