#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file
 and deserializes JSON file to instances
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """file storing class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary object"""
        return self.__objects

    def new(self, obj):
        """setting __object"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "w") as file:
            dic = {key: obj.to_dict() for key, obj in
                   self.__objects.items()}
            json.dump(dic, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                dic = json.load(file)
                for key, value in dic.items():
                    self.__objects[key] = eval(key.split(".")[0])(**value)
