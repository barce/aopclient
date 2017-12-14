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

print('------ update inventory sources ------')
print(' ')

now = datetime.datetime.now()

print(' ')
print(' ')
print(' ')
print('------ get tactics by campaign ------')
print(' ')

orgs = client.get_organizations()
print('organizations: ')
print(orgs)

print(' ')
print(' ')
print(' ')
# org_id: 7000095690
ads = client.get_advertisers(7000095690)
print('advertisers: ')
print(ads)

camps = client.get_campaigns(7000095690)

print(' ')
print(' ')
print(' ')
print(' ')
print('campaigns')
print(camps)

# campaigns: 131211833, 131210756
# ad_id: 7000095690
tactics = client.get_tactics_by_campaign(7000095690, 7000095690, 131211833)
print(' ')
print(' ')
print(' ')
print(' ')
print('tactics')
print(tactics)

# tactics: 439356, 439354
isources = client.get_inventory_sources_by_tactic(7000095690, 7000095690, 131211833, 439356)
print(' ')
print(' ')
print(' ')
print(' ')
print('isources')
print(isources)
a_sources = isources['data']
a_sources_ids = []
for source in a_sources:
  print(source['id'])
  a_sources_ids.append(source['id'])
print(a_sources_ids)

avails = client.get_avails_by_tactic(7000095690, 7000095690, 131211833, 439356)
print(' ')
print(' ')
print(' ')
print(' ')
print('avails')
print(avails)
a_avails = avails['data']
a_avails_ids = []
for avail in a_avails:
  print(avail['id'])
  a_avails_ids.append(avail['id'])
print(a_avails_ids)

print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print('update the list of inventory sources')
updated_list = client.update_inventory_sources_by_tactic(7000095690, 7000095690, 131211833, 439356,[1, 2, 9])
print(' ')
print(' ')
print('updated_list:')
print(updated_list)
print(' ')
print(' ')
print(' ')
print('restore list')
# [1, 2, 9, 17, 7, 18, 16, 4, 12, 13, 10, 8, 6, 5, 19]
updated_list = client.update_inventory_sources_by_tactic(7000095690, 7000095690, 131211833, 439356,[1, 2, 9, 17, 7, 18, 16, 4, 12, 13, 10, 8, 6, 5, 19])
print(' ')
print(' ')
print('restored list::')
print(updated_list)
