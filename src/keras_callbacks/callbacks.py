#!/usr/bin/python

import tensorflow as tf

from gtts import gTTS

from IPython.display import Audio
from IPython.core.display import display


import numpy as np

class PlayAudioWhenNewMaximumFound(tf.keras.callbacks.Callback):
    """
    when new maximum was found.

    Arguments:

    """

    def __init__(self, metric_name,decimals=3,patience=0):
        super().__init__()
        self.metric_name = metric_name;
        self.decimals=decimals;
        self.best = -np.Inf;
        self.wn=None;
        self.patience=patience;
        self.count=0;

    def on_train_begin(self, logs=None):
        # Initialize the best as infinity.
        self.best = -np.Inf;

    def on_epoch_end(self, epoch, logs=None):
        current = logs.get(self.metric_name);
        
        if np.greater(current, self.best):
            self.best = current;

            if self.count>=self.patience:
                metric_around = np.around(self.best,decimals=self.decimals);
                mytext= 'The metric has been improved to '+str(metric_around);
                print(mytext)
                myobj = gTTS(text=mytext, lang='en', slow=False);
                myobj.save("temporal_file.mp3");
                self.wn = Audio('temporal_file.mp3', autoplay=True)
                display(self.wn);
        
        self.count=self.count+1;

