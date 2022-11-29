#!/usr/bin/python3
""" Module of the AirBnB base class """
from datetime import datetime, time, date
import uuid
from models import storage


class BaseModel():
    """ Base class for all files on AirBnB project files """

    def __init__(self, *args, **kwargs):
        """ initialize instance fields """
        if kwargs is not None and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k in ["created_at", "updated_at"]:
                    ind = v.find('T')
                    dt = date.fromisoformat(v[:ind])
                    tm = time.fromisoformat(v[ind + 1:])
                    v = datetime.combine(dt, tm)
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
<<<<<<< HEAD
    else:
        for key, value in kwargs.items():
            if key != '__class__':
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
=======
>>>>>>> refs/remotes/origin/main

    def __str__(self):
        """ returns a string representation of the object """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates updated_at attribute with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dict cotaining all key-value pairs from __dict__ """
        dict1 = dict()
        dict1['__class__'] = __class__.__name__
        dict1['created_at'] = self.created_at.isoformat()
        dict1['updated_at'] = self.updated_at.isoformat()
        dict2 = self.__dict__
        for k, v in dict2.items():
            if (not k.startswith("__") and not k.endswith("__") and
                    "method" not in str(v) and "function" not in str(v) and
                    k not in dict1):
                dict1[k] = v
        return dict1
