# network_info.py
# A part of System inspect
# This file is covered by the GNU General Public License.
# Copyright (C) 2023 kefaslungu

import io
import wmi

def networkCards():
    """Provides information about network adapters and their IP configurations."""
    c = wmi.WMI()
    nic_info = io.StringIO()
    for nic in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        nic_info.write(f"Name: {nic.Description}\n")
        if nic.MACAddress:
            nic_info.write(f"MAC Address: {nic.MACAddress}\n")
        nic_info.write(f"IP Address(es): {', '.join(nic.IPAddress.split() if isinstance(nic.IPAddress, str) else list(nic.IPAddress))}\n")
        nic_info.write(f"Subnet Mask(s): {', '.join(nic.IPSubnet.split() if isinstance(nic.IPSubnet, str) else list(nic.IPSubnet))}\n")
        nic_info.write(f"Default Gateway(s): {', '.join(nic.DefaultIPGateway.split() if isinstance(nic.DefaultIPGateway, str) else list(nic.DefaultIPGateway))}\n")
        nic_info.write(f"DNS server(s): {', '.join(list(nic.DNSServerSearchOrder))}\n")
        nic_info.write("\n")
    return nic_info.getvalue()
