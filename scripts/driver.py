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


now = datetime.datetime.now()
name = 'two domains - {}'.format(now)
domains = ['https://www.google.com', 'https://slashdot.org']
apps = []
default = False
result = client.create_whitelist_by_advertiser(7000095690, 7000095690, name, domains, apps, default)
print(result)

# get id and update
now = datetime.datetime.now()
whitelist_id = result['whitelist']['id']
op = 'REPLACE'
path = '/name'
value = 'updated whitelist - {}'.format(now)
#   def update_whitelist_by_advertiser(self, org_id=0, ad_id=0, whitelist_id=0, op='REPLACE', path='/name', value=''):
result = client.update_whitelist_by_advertiser(7000095690, 7000095690, whitelist_id, op, path, value)
print(result)
