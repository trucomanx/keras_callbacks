#!/usr/bin/python

import sys

sys.path.append('../src')

from keras_callbacks import PlayAudioWhenNewMaximumFound

callback_tts=PlayAudioWhenNewMaximumFound(metric_name='val_categorical_accuracy',patience=10)
