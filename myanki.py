#!/user/bin/env python3
# coding: utf-8

import sys
import os
import random

NUM = 10


options = sys.argv[1:]
dir = './files/'
filename = random.choice(os.listdir(dir))
pattern = '^[0-9]{1,2}$'
for i in options:
    if re.match(pattern, i):
        filename = i + '.txt'

target_file = dir + filename

random_mode = False
if 'r' in options:
    random_mode = True



item_list = []
with open(target_file, 'r') as f:
    for i in range(NUM):
        line = f.readline()
        item_list.append(line[:-1].split('\t'))

        if random_mode:
            random.shuffle(item_list)

for i in range(NUM):
    count = 0
    question = item_list[i][0]
    correct_sentence = item_list[i][1]
    while True:
        count += 1
        print('[ja]-> ', question)
        user_answer = input('[en]-> ')
        if user_answer == correct_sentence:
            print('✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔')
            break
        else:
            if count < 2:
                print('✗✗✗✗✗✗✗✗✗✗✗✗✗✗✗')
            else:
                print('==========正解は・・・========')
                print(correct_sentence)
                print('~~~~~~2回入力して覚えよう~~~~~~')

                for i in range(2):
                    input()
                break