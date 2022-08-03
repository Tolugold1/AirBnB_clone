#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """program that contains the entry point of the command interpreter"""
    prompt = '(hbnb) '
    intro = 'Type help to list command'

    def emptyline(self):
        """Do nothing if no command is given"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
