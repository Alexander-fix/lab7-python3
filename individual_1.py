#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()

    # Разбить текст на слова.
    words = text.split(" ")

    for i in range(1, len(words), 2):
        words[i], words[i - 1] = words[i - 1], words[i]
    print(' '.join(words))
