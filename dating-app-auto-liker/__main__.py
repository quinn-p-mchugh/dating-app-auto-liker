"""Module containing code to begin auto liking.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

import threading
from account import *
from website import *

"""Input user account information here:"""
# OkCupid email and password
ok_cupid_email = ""
ok_cupid_password = ""
# Tinder email and password
tinder_email = ""
tinder_password = ""

# Initialize dating websites
ok_cupid  = OkCupid(Account(email = ok_cupid_email,
    password = ok_cupid_password))
tinder = Tinder(Account(email = tinder_email,
    password = tinder_password))

# Begin login & auto liking sequences in separate threads
threading.Thread(target=ok_cupid.run_auto_liker).start()
threading.Thread(target=tinder.run_auto_liker).start()
