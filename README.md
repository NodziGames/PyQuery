PyQuery is a digital assistant written in Python.

PyQuery directs your questions to the Wolfram API, and if no results are found, it redirects it to the Wikipedia API.

To use PyQuery, you'll require the following libraries

pip install wolframalpha

pip install wikipedia

pip install -U wxPython

Please note that you'll also need to grab an API key for Wolfram, and replace the key on line 8 of pyquery.py with your own. These are freely obtainable on the wolfram alpha website

Lastly, you'll require mpg123 in order for PyQuery to read the answers to you. It will function without it, but if you'd like to experience the full potential, please download mpg123, and be sure to configure your path correctly.
