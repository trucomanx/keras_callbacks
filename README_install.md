# Requirements
Install the requirements.

    pip3 install -r requirements.txt

# Packaging

Download the source code

    git clone https://github.com/trucomanx/keras_callbacks

The next command generates the `dist/keras_callbacks-VERSION.tar.gz` file.

    cd keras_callbacks/src
    python setup.py sdist

For more informations use `python setup.py --help-commands`

# Install 

Install the packaged library

    pip3 install dist/keras_callbacks-VERSION.tar.gz
