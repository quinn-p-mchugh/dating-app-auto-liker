"""Module containing code to begin auto liking."""

import threading
from website import *

"""Input user account information here:"""
# OkCupid email and password
ok_cupid_email = "(Your Facebook Email)"
ok_cupid_password = "(Your Facebook Password)"
# Tinder email and password
tinder_email = "(Your Facebook Email)"
tinder_password = "(Your Facebook Password)"

# Initialize dating websites
ok_cupid  = OkCupid(Account(email = ok_cupid_email,
    password = ok_cupid_password))
tinder = Tinder(Account(email = tinder_email,
    password = tinder_password))

# Begin login & auto liking sequences in separate threads
threading.Thread(target=ok_cupid.run_auto_liker).start()
threading.Thread(target=tinder.run_auto_liker).start()
