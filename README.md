# secure-password-generator
This module is built for secure password generation. For security purposes I recommend using a password longer than 8 characters.

STEPS
1. store all characters as a list
2. prompt user for length
3. shuffle the char list for increased randomization
4. create an empty list to store pass
5. append random characters to the password list
      pick a random character from the list using random.choice method
      append that char to the pass list
6. randomize the pass list
7. convert pass list to string using join method
      print the finalized string
