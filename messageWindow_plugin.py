"""Abaqus CAE plugins to work with the Abaqus CAE message window

Latest version: https://github.com/costerwi/plugin-displayGrouper

Carl Osterwisch, July 2024
"""

__version__ = "0.1.0"

from abaqusGui import getAFXApp

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()

toolset.registerKernelMenuButton(
    moduleName='messageWindow',
    functionName='clear()',
    buttonText='Clear message window',
    author='Carl Osterwisch',
    description='Print blank lines to scroll away text in the message window. ' \
        'User must repeat if needed for a message window of more than 10 lines.',
    version=__version__,
    helpUrl='https://github.com/costerwi/plugin-messageWindow',
    )
