from boltiot import Bolt

api_key = "Your API Key"
device_id = "BOLT1488XXXX"
mybolt = Bolt(api_key, device_id)
response = mybolt.restart()
print(response)
