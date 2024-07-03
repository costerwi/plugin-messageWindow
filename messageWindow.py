"""Abaqus CAE plugins to work with the Abaqus CAE message area

Latest version: https://github.com/costerwi/plugin-displayGrouper

Carl Osterwisch, July 2024
"""

from __future__ import print_function

def clear(lines=10):
    "Print blank lines to scroll away text in the message window"
    print('\n'*lines)
