#!/usr/bin/python

import sys

sys.path.append('../src')

from keras_callbacks import WhenNewMaximumFound


callback_tts=WhenNewMaximumFound(metric_name='val_categorical_accuracy',patience=20);

