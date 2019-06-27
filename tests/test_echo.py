#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess
# Your test case class goes here


class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()

    def test_Help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def test_Upper_U(self):

        args = ["-u", "hello"]

        usage = "HELLO"
        self.assertEquals(echo.main(args), usage)

    def test_Upper(self):
        args = ["--upper", "hello"]

        usage = "HELLO"
        self.assertEquals(echo.main(args), usage)

    def test_Lower_L(self):
        args = ["-l", "HELLO"]

        usage = "hello"
        self.assertEquals(echo.main(args), usage)

    def test_Lower(self):
        args = ["--lower", "HELLO"]

        usage = "hello"
        self.assertEquals(echo.main(args), usage)

    def test_Title_T(self):
        args = ["-t", "hello"]

        usage = "Hello"
        self.assertEquals(echo.main(args), usage)

    def test_Title(self):
        args = ["--title", "HELLO"]

        usage = "Hello"
        self.assertEquals(echo.main(args), usage)

    def test_All(self):
        args = ["-tul", "heLLo"]

        usage = "Hello"
        self.assertEquals(echo.main(args), usage)

    def test_Two(self):
        args = ["-ul", "heLLo"]

        usage = "hello"
        self.assertEquals(echo.main(args), usage)

    def test_No_Args(self):
        args = ["hello"]

        usage = "hello"
        self.assertEquals(echo.main(args), usage)


if __name__ == '__main__':
    unittest.main()
