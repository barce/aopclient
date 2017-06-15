#!/usr/bin/env python
# sample driver file for the AOLClient (display)
# 


from aopclient import AOLClient
client = AOLClient()
client.connect()
camps = client.get_campaigns(7000095690)
print(camps)
tactics = client.get_tactics_by_campaign(7000095690, 7000095690, 131210756)
print(tactics)


