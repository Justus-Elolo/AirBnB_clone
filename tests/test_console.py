#!/usr/bin/python3
"""
Checks console for capturing stdout into a StringIO object
"""

import sys
import unittest
import os
from unittest.mock import create_autospec, patch
from io import StringIO
from console import HBNBCommand
from models.user import User
from models.state import State
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity

class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """Redirecting stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err = ["** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    ]

        self.cls = ["BaseModel",
                    "User",
                    "State",
                    "City",
                    "Place",
                    "Amenity",
                    "Review"]
         def last_write(self, nr=None):
        """Returns last n output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))

    def test_quit(self):
        """Quit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

    def create(self, server=None):
        """
        Redirects stdin and stdout to the mock module
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    if __name__ == '__main__':
    unittest.main()



