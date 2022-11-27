#!/usr/bin/python3
""" FileStorage class module """
import os
import json


class FileStorage:
    """ FileStorage class deals with object storage in files """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ adds obj into __objects dict """
        ind = obj.__class__.__name__ + obj.id
        val = obj.to_dict()
        FileStorage.__objects[ind] = val
    
    def save(self):
        """ serializes __objects to JSON file """
        with open(FileStorage.__file_path, "w") as fp:
            fp.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """ deserializes JSON file int __objects """
        try:
            with open(FileStorage.__file_path, "r") as fp:
                FileStorage.__objects = json.loads(fp.read())
        except Exception:
            pass
