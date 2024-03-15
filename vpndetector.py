import requests
import json

def get_ip_address():
    data = str(requests.get('http://checkip.dyndns.com/').text)
    return data.split(': ')[-1].split('<')[0]

def is_vpn(ip_address):
    API_key = "2c1294b9924b42fe9eba83fcf032374d"  # API key (you can change it with yours )
    response = requests.get(f"https://vpnapi.io/api/{ip_address}?key={API_key}")
    data = json.loads(response.text)
    return data["security"]["vpn"]

def print_header(title):
    print(f"\n{'=' * len(title)}\n{title}\n{'=' * len(title)}\n")

while True:
    print_header("VPN IP Address CHECKER")

    ip_address = get_ip_address()
    print(f"IP Address: {ip_address}")

    vpn_status = is_vpn(ip_address)
    if vpn_status:
        print("This IP address is using a VPN. \U00002705")
    else:
        print("This IP address is not using a VPN. \U0000274C")

    choice = input("\nChoose an option:\n1 - Check again \U0001F504\n2 - Close \U0001F44B\noption = ")

    if choice == '1':
        continue
    elif choice == '2':
        break
    else:
        print("\nInvalid choice. Please try again. \U000026A0")
