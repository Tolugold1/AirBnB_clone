#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """program that contains the entry point of the command interpreter"""
    prompt = '(hbnb) '
    intro = 'Type help to list command'

    list_of_class = ["BaseModel"]

    def do_create(self, arg):
        """Create a new class"""
        if not arg:
            print("** class name missing **")
            return
        new = arg.split()  # in case arg has a space in between
        if new[0] not in self.list_of_class:
            print("** class doesn't exist **")
        else:
            new_clas = eval(new[0] + "()")
            print(new_clas.id)
            new_clas.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        new_arg = arg.split()
        if new_arg[0] not in self.list_of_class:
            print("** class doesn't exist **")
        if len(new_arg) < 2:
            print("** instance id missing **")
        else:
            try:
                j = new_arg[0] + '.' + new_arg[1]
                print(storage.all()[j])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        new_arg = arg.split()
        if new_arg[0] not in self.list_of_class:
            print("** class doesn't exist **")
        elif len(new_arg) < 2:
            print("** instance id missing **")
        else:
            try:
                j = new_arg[0] + '.' + new_arg[1]
                storage.all().pop(j)
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            dic_str_list = []
            for key, value in storage.all().items():
                dic_str_list.append(str(value))
            if dic_str_list != 0:
                print(dic_str_list)
        else:
            arg = arg.split()
            if arg[0] in self.list_of_class:
                dic_str_list = []
                for key, value in storage.all().items():
                    if str(key.split(".")[0]) == arg[0]:
                        dic_str_list.append(str(value))
                if dic_str_list != 0:
                    print(dic_str_list)
            else:
                print("** class doesn't exist **")

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