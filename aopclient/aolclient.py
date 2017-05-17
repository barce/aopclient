#!/usr/bin/env python

from future.standard_library import install_aliases
install_aliases()


import json
import jwt
import requests
import time
import os


use_environment_variables = None

try:
    from django.conf import settings
except ImportError:
    use_environment_variables = True


class AOLClient:
  client_id = None
  client_secret = None
  host = None

  def show_config(self):
    print(self.client_id)
    print(self.client_secret)
    print(self.host)

