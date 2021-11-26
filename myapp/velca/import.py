from datetime import *
from dateutil import tz
import scraping as sc
from django.db import IntegrityError

import sys
import os
import django

from velca.myapp.velca.models import Player

sys.path.append("C:\myapp")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","myapp.settings")

django.setup()
from player.models import *

for list in sc.spnav_scraping():
  first_name = list[0]
  last_name = list[0]
  try:
    Player.objects.create(first_name=first_name, last_name=last_name)
  except IntegrityError:
    pass