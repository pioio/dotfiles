###################################################################################################
# Original source of this code:
# https://gist.github.com/AffanIndo/af35873adb65a689f370a7cd988d12fc  (thank you)
###################################################################################################
# This is set of plugins for the Ranger terminal file browser
# https://github.com/ranger/ranger
#
# To install, copy this file to ~/.config/ranger/plugins
###################################################################################################

from ranger.api.commands import *

class terminal(Command):
    """:terminal
    Open new tmux split in the current directory.

    Allows for more seamless integration with tmux.
    """
    def execute(self):
        import os
        from ranger.ext.get_executables import get_executables
        if os.environ.get('TMUX'):
            command = 'tmux split-window -v'
        else:
            command = os.environ.get('TERMCMD', os.environ.get('TERM'))
            if command not in get_executables():
                command = 'x-terminal-emulator'
            if command not in get_executables():
                command = 'xterm'
        self.fm.run(command, flags='f')
