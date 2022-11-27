#!/usr/bin/python3
""" Module containing entry point of the command interpreter """
import sys
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ commands and for the interpreter"""

    prompt = "(hbnb) "
    file = None

    def do_create(self, arg):
        """ creates a new instance and ssaves it to the file """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """prints a string representation of an instance based on class name"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        ind = arg.find(' ')
        if ind == -1:
            print("** instance id missing **")
        elif arg[:ind] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            storage.reload()
            key = arg[:ind] + arg[ind + 1:]
            m_dict = storage.all()
            if key in m_dict:
                print(m_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ deletes an instance based on class name and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        ind = arg.find(' ')
        if ind == -1:
            print("** instance id missing **")
        elif arg[:ind] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            storage.reload()
            key = arg[:ind] + arg[ind + 1:]
            m_dict = storage.all()
            if key in m_dict:
                del m_dict[key]
                del storage._FileStorage__objects[key]
                storage.save
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ prints string rep of all instances """
        storage.reload()
        m_dict = storage.all()
        if len(arg) == 0:
            lst = []
            for key in m_dict:
                obj = BaseModel(**m_dict[key])
                lst.append(obj.__str__())
            print(lst)
            return
        if arg in ["BaseModel"]:
            lst = []
            for key in m_dict:
                val = m_dict[key]
                if val["__class__"] == arg:
                    obj = BaseModel(**val)
                    lst.append(obj.__str__())
            print(lst)
            return
        print("** class doesn't exist **")

    def do_update(self, arg):
        """ updates an instance based on cls.name and id
        usage: update cls.name id attr_name 'attr_val' """
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split(' ')
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        storage.reload()
        m_dict = storage.all()
        key = args[0] + args[1]
        if key in m_dict:
            obj = BaseModel(**m_dict[key])
            setattr(obj, args[2], args[3])
            obj.save()
            storage._FileStorage.__objects[key] = obj.to_dict()
            storage.save()
            return
        print("** no instance found **")
        
    def do_quit(self, arg):
        """ exits the program """
        sys.exit(0)

    def do_EOF(self, arg):
        """ exits the program """
        sys.exit(0)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
