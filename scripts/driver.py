#!/usr/bin/env python

import datetime
from aopclient import AOLClient
client = AOLClient()
client.show_config()
client.connect()
# client.get_organizations()
# client.get_campaigns(7000095690)
# client.get_campaigns_by_advertiser(7000095690, 7000095690)
# client.get_campaigns_by_advertiser_by_campaign(7000095690, 7000095690, 131210756)

print(' ')
print(' ')
print(' ')

print('------ create whitelist ------')
print(' ')
now = datetime.datetime.now()
name = 'two domains - {}'.format(now)
domains = ['https://www.google.com', 'https://slashdot.org']
apps = []
default = False
result = client.create_whitelist_by_advertiser(7000095690, 7000095690, name, domains, apps, default)
print(result)
print('------ create whitelist ------')
print(' ')
print(' ')
print(' ')

print('------ update whitelist ------')
print(' ')
# get id and update
now = datetime.datetime.now()
whitelist_id = result['whitelist']['id']
op = 'REPLACE'
path = '/name'
value = 'updated whitelist - {}'.format(now)
#   def update_whitelist_by_advertiser(self, org_id=0, ad_id=0, whitelist_id=0, op='REPLACE', path='/name', value=''):
result = client.update_whitelist_by_advertiser(7000095690, 7000095690, whitelist_id, op, path, value)
print(result)

print(' ')
print(' ')
print(' ')

print('------ create blacklist ------')
print(' ')
now = datetime.datetime.now()
name = 'two domains - {}'.format(now)
domains = ['https://www.spam.la', 'https://zynga.com']
apps = []
default = False
result = client.create_blacklist_by_advertiser(7000095690, 7000095690, name, domains, apps, default)
print(result)
print('------ create blacklist ------')
print(' ')
print(' ')
print(' ')

print('------ update blacklist ------')
print(' ')
# get id and update
now = datetime.datetime.now()
blacklist_id = result['blacklist']['id']
op = 'REPLACE'
path = '/name'
value = 'updated blacklist - {}'.format(now)
#   def update_blacklist_by_advertiser(self, org_id=0, ad_id=0, blacklist_id=0, op='REPLACE', path='/name', value=''):
result = client.update_blacklist_by_advertiser(7000095690, 7000095690, blacklist_id, op, path, value)
print(result)

print(' ')
print(' ')
print(' ')

