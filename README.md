# Install keras_callbacks

Install keras_callbacks following [doc/INSTALL.md](doc/INSTALL.md)

# keras_callbacks example code

The next code shows an example use of keras_callbacks library.

```python
from keras_callbacks import PlayAudioWhenNewMaximumFound

callback_tts=PlayAudioWhenNewMaximumFound(metric_name='val_categorical_accuracy',patience=10);
```

# keras_callbacks example files

Example files can be found at [test/example.py](test/example.py).
