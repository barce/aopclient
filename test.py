def organization_name():
  from aopclient import AOLClient
  client = AOLClient()
  client.show_config()
  client.connect()
  orgs = client.get_organizations()
  return orgs['data'][2]['name']

def test_organization_name():
  assert organization_name() == 'Accuen Inc.'

def campaign_count():
  from aopclient import AOLClient
  client = AOLClient()
  client.show_config()
  client.connect()
  orgs = client.get_organizations()
  camps = client.get_campaigns(7000038774)
  return camps['count']

def test_campaign_count():
  assert campaign_count() >= 1

# client.get_campaigns(7000095690)
# client.get_campaigns_by_advertiser(7000095690, 7000095690)
# client.get_campaigns_by_advertiser_by_campaign(7000095690, 7000095690, 131210756)
