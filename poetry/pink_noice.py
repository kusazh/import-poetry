# Pink Noise
# Based on the work of Pink Noise, an iOS app, 2016.
# This file can be actually executed.

import random


noun = ['church', 'shadow', 'letter', 'man', 'neck', 'day', 'eye', 'grass',
        'you', 'diary', 'yesterday', 'stomach', 'newspaper', 'mailbox', 'expression', 'tie',
        'foot', 'smile', 'tea', 'sun', 'fish', 'land', 'day', 'poetry',
        'clock', 'window', 'skin', 'stone', 'lighthouse', 'pigeon', 'bone']
verb = ['sing', 'forget', 'hate', 'write', 'speak', 'agree', 'praise', 'open',
        'heal', 'read', 'beat', 'cut', 'make', 'dream', 'wear', 'listen',
        'build', 'care', 'leave', 'name', 'look', 'act', 'love', 'trust', 'dry']
for i in range(4):
    verse = (noun[random.randint(0, len(noun) - 1)] + ' ' + 
             verb[random.randint(0, len(verb) - 1)] + ' ' +
             noun[random.randint(0, len(noun) - 1)])
    print(verse)
