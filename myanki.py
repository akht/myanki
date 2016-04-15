# coding: utf-8

import sys
import os
import random


class EnglishSentence:
    def __init__(self, sentence):
        self.sentence = sentence

    # case-insensitive
    def is_equivalent(self, target_sentence):
        if self.sentence.lower() == target_sentence.lower():
            return True
        else:
            return False

# 一度に出題する数
NUM = 10
options = sys.argv[1:]

# 出題に使うファイルを決める
res_dir = './res/'
filename = random.choice(os.listdir(res_dir))
target_file = res_dir + filename

# ファイル中のセンテンスの出題方法
# not random_mode(デフォ) = 上から順に出題
# random_mode = 順番関係なくランダムに出題
random_mode = False
if 'r' in options:
    random_mode = True


# 選択されたファイルから、
# 英語文と日本語文がペアになったリストを作る
item_list = []
with open(target_file, 'r') as f:
    for i in range(NUM):
        line = f.readline()
        item_list.append(line[:-1].split('\t'))

if random_mode:
    random.shuffle(item_list)


# 出題
print('')
print(str(filename))
print('')
for i in range(NUM):
    count = 0
    question = item_list[i][0]
    correct = EnglishSentence(item_list[i][1])

    while True:
        count += 1
        print('[ja]-> ', question)
        user_input = input('[en]-> ')
        user_answer = EnglishSentence(user_input)
        if user_answer.is_equivalent(correct.sentence):
            print('\n(˵¯͒〰¯͒˵) Good! (˵¯͒〰¯͒˵)\n')
            break
        else:
            if count < 2:
                print('\nʕ ͠° ʖ̫ °͠ ʔ Oops! ʕ ͠° ʖ̫ °͠ ʔ\n')
            else:
                print('~~~~正解は~~~~')
                print(correct.sentence)
                print('~~入力して覚えよう~~')
                input()
                break
