#!/usr/bin/python3
###############################################################################
# Copyright 2021 - 2022, Inesonic, LLC.
#
# GNU Public License, Version 3:
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the Free
#   Software Foundation, either version 3 of the License, or (at your option)
#   any later version.
#   
#   This program is distributed in the hope that it will be useful, but WITHOUT
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#   more details.
#   
#   You should have received a copy of the GNU General Public License along
#   with this program.  If not, see <https://www.gnu.org/licenses/>.
###############################################################################

"""
Python script that runs certbot at regular intervals.

"""

###############################################################################
# Imports
#

import random
import time
import os
import sys

###############################################################################
# Globals:
#

MEAN_SERVICE_INTERVAL = 2 * 24 * 3600
"""
The average service interval, in seconds.

"""

DELTA_SERVICE_INTERVAL = 24 * 3600
"""
The maximum variability desired around the requested service interval.  Value
is in seconds.

"""

CERTBOT_COMMAND = "/usr/bin/certbot renew"
"""
Command to be executed.

"""

###############################################################################
# Main:
#

r = random.SystemRandom()
while True:
      next_delay = r.randint(
	  -DELTA_SERVICE_INTERVAL / 2,
	  +DELTA_SERVICE_INTERVAL / 2
      ) + MEAN_SERVICE_INTERVAL

      days = int(next_delay / (24 * 3600))
      days_residue = next_delay - 24 * 3600 * days
      hours = int(days_residue / 3600)
      hours_residue = days_residue - 3600 * days
      minutes = int(hours_residue / 60)
      seconds = hours_residue - 60 * minutes
      sys.stdout.write("""
*******************************************************************************
Sleeping for %d days, %d hours, %d minutes, %d seconds.
"""%      (
              days,
              hours,
              minutes,
              seconds
          )
      )

      time.sleep(next_delay)

      os.system(CERTBOT_COMMAND)
