# Code example – Simulating DHCP-like allocation in Python:
import random
class DHCPServer:
   def __init__(self, ip_pool):
       self.ip_pool = ip_pool
       self.leases = {}
   def assign_ip(self, device_id):
       if device_id in self.leases:
           return self.leases[device_id]
       ip = self.ip_pool.pop(0)
       self.leases[device_id] = ip
       return ip
# Example usage
dhcp = DHCPServer(["192.168.1." + str(i) for i in range(100, 200)])
print(dhcp.assign_ip("Laptop-01")) # Assigns first available IP
print(dhcp.assign_ip("Laptop-02")) # Assigns next available IP