#!/usr/bin/python3
"""
The console:Contains the entry point of the command interpreter
"""
import cmd
import json
import re
import models
#from models import storage
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.city import city

class HBNBCommand(cmd.Cmd):
    """Custom console class"""

    prompt = '(hbnb)'

    def my_errors(self, line, num_of_args):
        """Display error message to the user

        Description:
        Displays output to the user based on input command

        """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        msg = ["** class name is missing **",
               "** class does not exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name is missing **",
               "** value is missing **"]


