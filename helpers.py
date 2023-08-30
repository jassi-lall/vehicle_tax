"""
Helper functions

Generate a random numberplate
"""

import random
import string

def random_age_identifier():
    """ Random 2 digit age identifier for a UK numberplate. e.g '61', '09' """
    return random.choice(["6", "0"]) + random.choice(string.digits)

def random_area_code():
    """ Random 2 character area code for a UK numberplate. e.g. 'WN', 'BL' """
    return "".join(random.choices(string.ascii_uppercase, k=2)) 

def random_numberplate():
    return random_area_code() + random_age_identifier() + " " + "".join(random.choices(string.ascii_uppercase, k=3))