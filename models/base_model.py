#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

'''import public instance attributes'''


class BaseModel:
    '''
    Create a class
    '''

    def __init__(self, *args, **kwargs):
        '''Initialize the class'''
        from models import storage
        '''Define the public instance attributes'''
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
    else:
        for key, value in kwargs.items():
            if key != '__class__':
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def __str__(self):
        '''Returns the string of the class in a specific formart'''
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        '''Define public instance methods'''
        '''Update the public instance attribute with the current datetime'''
        from models import storage
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Return a dictionary containing all keys/values of __dict__'''
        dict_1 = self.__dict__.copy()
        dict_1['__class__'] = = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ('created_at', 'updated_at'):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
