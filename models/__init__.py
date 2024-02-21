#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

type_storage = os.getenv('HBNB_TYPE_STORAGE')
if type_storage == "db":

    storage = DBStorage()
else:

    storage = FileStorage()

storage.reload()
