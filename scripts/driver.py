#!/usr/bin/env python

from aopclient import AOLClient
client = AOLClient()
client.show_config()
client.connect()
client.get_organizations()
client.get_campaigns(7000095690)
client.get_campaigns_by_advertiser(7000095690, 7000095690)
client.get_campaigns_by_advertiser_by_campaign(7000095690, 7000095690, 131210756)
