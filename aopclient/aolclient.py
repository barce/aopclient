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
  aud = None
  payload = None
  encoded_payload = None
  oauth_url = None
  payload_url = None
  headers = None
  authorized_headers = None

  def show_config(self):
    print(self.client_id)
    print(self.client_secret)
    print(self.host)


  def set_payload(self):
    now = int(time.time())
    self.payload = = {
      "aud": "https://{0}/identity/oauth2/access_token?realm=aolcorporate/aolexternals".format(self.host),
      "iss": self.client_id,
      "sub": self.client_id,
      "exp": now + 3600,
      "iat": now ,
    }
    return self.payload

  def encode_payload(self):
    self.encoded_payload = jwt.encode(self.payload, self.client_secret, algorithm='HS256')
    return self.encoded_payload


  def set_oauth_url(self):
    self.oauth_url = "https://{0}/identity/oauth2/access_token".format(host)

  def set_payload_url(self):
    self.payload_url = "grant_type=client_credentials&scope=one&realm=aolcorporate/aolexternals&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer&client_assertion={0}".format(encoded)

  def set_headers(self):
    self.headers = {
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "application/json"
    }

  def get_token(self):
    response = requests.post(self.oauth_url, headers=self.headers, data=self.encoded_payload)
    json_response = json.loads(response.text)
    self.authorized_headers = {'Authorization': "Bearer " + json_response['access_token']}

    self.authorized_headers['Content-Type'] = 'application/json'
    self.authorized_headers['x-api-key'] = os.environ['AOP_API_KEY']

