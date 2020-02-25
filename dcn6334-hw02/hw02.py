# -*- coding: utf-8 -*-
"""
Deion Nwaefulu
CSE 3313
1001226334
"""

import numpy as np
import soundfile as sf
import math

#Key note numbers for the song Twinkle Twinkle Little Star
NoteKey = [52, 52, 59, 59, 61, 61, 59, 59, 57, 57, 56, 56, 54, 54, 56, 52, 59, 59, 57, 57, 56, 56, 54, 54]

Amplitude = 1
fs = 8000
ts = 1/fs;
time = 0.5;

x = np.arange(0, time, ts)
sin = []

#Converting from frequencies to cosine wave and then to sound
i = 0
while i < len(NoteKey):
    frequency = 440 * 2 ** ((NoteKey[i] - 49)/12)
    cosine = np.cos(2*np.pi*frequency*x)
    sin = np.concatenate([sin,cosine])
    i = i + 1

sf.write('twinkle.wav', sin, fs)