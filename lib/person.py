#!/usr/bin/env python3

class Person:
    # dunder method very important
    def __init__(self, name):

        self.name = name

    def talk(self):
        
        print("Hello World!") 

    def walk(self):

        print("The person is walking.")       
