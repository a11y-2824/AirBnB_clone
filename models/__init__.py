#!/usr/bin/python3
""" Create an init dunder """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
