#!/usr/bin/python3
"""
Module: initialize python.
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
