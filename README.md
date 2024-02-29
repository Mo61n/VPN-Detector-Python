# Getting Started:

To use this tool, clone the repository, replace the placeholder API key with your own from [vpnapi.io](https://vpnapi.io/)
, and run the script. Make sure you have Python and the Requests library installed on your system

## Key Features:
* **Automatic IP Detection :** It uses http://checkip.dyndns.com/ to retrieve the user's current IP address
* **VPN Detection :** It uses the vpnapi.io API to verify whether the IP address is obtained from a VPN or not, and provides a high accuracy rate of 95% to 98%.
* **Security Focused :** Helps identify potential security risks associated with VPN use in network traffic

# How It Works:

1. **Get IP Address :** The script first retrieves the user's current IP address
2. **Check VPN Status :** It then requests the vpnapi.io API with the IP address to check if it is associated with a VPN service.
3. **Display Results :** The output shows whether the IP address is using a VPN or not, increasing network security awareness and control

# Use Cases:
* **Security Monitoring :** Ideal for organizations looking to monitor and block VPN-based access to sensitive systems
* **Network Analysis :** Useful for network administrators and cyber security professionals in analyzing traffic sources

# License

[MIT License](https://choosealicense.com/licenses/mit/)
