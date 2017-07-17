#!/usr/bin/env python
# sample driver file for the AOLClient (display)
# 


from aopclient import AOLClient

def parse_camps(camps, org_id, client):
    for camp in camps:
        # print(str(org_id) + " " + str(camp['advertiserId']) + " " + str(camp['id']) + " " + camp['name'])
        tactics = client.get_tactics_by_campaign(org_id, camp['advertiserId'], camp['id'])
        if 'data'in tactics:
            for tactic in tactics['data']:
                print("creatives = client.get_creative_assignments({}, {}, {}, {})".format(org_id, camp['advertiserId'], camp['id'], tactic['id']))
        
client = AOLClient()
client.connect()

orgs = client.get_organizations()

org_ids = []

for org in orgs['data']:
    org_ids.append(org['organizationId'])

    
camps = client.get_campaigns(7000095690)
print(" ")
print(" ")
print("get campaigns...")
for org_id in org_ids:
    print("---- org_id: {} ----".format(org_id))
    camps = client.get_campaigns(org_id)

    if 'data' in camps:
        print("---- camps ----")
        parse_camps(camps['data'], org_id, client)
        print("---- camps ----")
        
# org_id: 7000038774
# ad_id:  7000038774
# campaign_id: 98908791
# tactic_id: 400794

print(" ")
print(" ")
print("get tactics...")
# tactics = client.get_tactics_by_campaign(7000095690, 7000095690, 131210756)
# print(tactics)


print(" ")
print(" ")
print("get tactic1 by id...")
tactic1 = client.get_tactic_by_id(7000095690, 7000095690, 131210756, 420407)
print(tactic1)
print(" ")
print(" ")
print("get tactic2 by id...")
tactic2 = client.get_tactic_by_id(7000038774, 7000038774, 98908791, 400794)
print(tactic2)


print(" ")
print(" ")
print("get creatives...")
# creatives = client.get_creative_assignments(7000095690, 7000095690, 131210756, 420407)
creatives = client.get_creative_assignments(7000038774, 7000038774, 98908791, 400794)
print(creatives)

