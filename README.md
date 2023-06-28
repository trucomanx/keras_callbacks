# Install keras_callbacks

Install keras_callbacks following https://github.com/trucomanx/keras_callbacks/blob/main/README_install.md 

# keras_callbacks example code

The next code shows an example use of keras_callbacks library.

```python
from keras_callbacks import WhenNewMaximumFound

callback_tts=WhenNewMaximumFound(metric_name='val_categorical_accuracy',patience=10);
```

# keras_callbacks example files

Example files can be found at [example.py](example.py).
