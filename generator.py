#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Jacob Warren Stack
# Created Date: 2022-04-16, 3:49 PM
# version ='1.0'
# ---------------------------------------------------------------------------
""" This module is built for secure password generation.
    For security purposes I recommend using a password longer than 8 characters."""
# ---------------------------------------------------------------------------
import string
import random
# ---------------------------------------------------------------------------
#STEPS
# 1.store all characters as a list
# 2.prompt user for length
# 3.shuffle the char list for increased randomization
# 4.create an empty list to store pass
# 5.append random characters to the password list
    # pick a random character from the list using random.choice method
    # append that char to the pass list
# 6. randomize the pass list
# 7.convert pass list to string using join method
#   print the finalized string
# ---------------------------------------------------------------------------

# characters list
chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# title method
def title():
    print("""
  _________________________  _________  ____  __.___________________
 /   _____/\__    ___/  _  \ \_   ___ \|    |/ _|\_   _____/\______  |
 \_____  \   |    | /  /_\  \/    \  \/|      <   |    __)_  |    |   |
 /        \  |    |/    |    \     \___|    |  \  |        \ |    `   |
/_______  /  |____|\____|__  /\______  /____|__ \/_______  //_______  /
        \/                 \/        \/        \/        \/         \/""")
    print("Stacked Password Generation (SPG)")
    print("\n")

# generation method
def generate():
    # get length
    length = int(input("Enter a password length: "))

    # shuffle character list
    random.shuffle(chars)

    # create  password list containing a set amount of random characters
    passw = []
    for i in range(length):
        passw.append(random.choice(chars))

    # shuffle the list of random characters
    random.shuffle(passw)

    # print the result
    print ("Password: "+"".join(passw))
    print ("\n")


# invoking functions
title()
generate()
