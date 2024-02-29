import requests
import json

def get_ip_address():
    data = str(requests.get('http://checkip.dyndns.com/').text)
    return data.split(': ')[-1].split('<')[0]

def is_vpn(ip_address):
    API_key = ""  # your API key 
    response = requests.get(f"https://vpnapi.io/api/{ip_address}?key={API_key}")
    data = json.loads(response.text)
    return data["security"]["vpn"]

# Get IP address
ip_address = get_ip_address()
print(f"IP Address: {ip_address}")

vpn_status = is_vpn(ip_address)
if vpn_status:
    print("This IP address is using a VPN.")
else:
    print("This IP address is not using a VPN.")