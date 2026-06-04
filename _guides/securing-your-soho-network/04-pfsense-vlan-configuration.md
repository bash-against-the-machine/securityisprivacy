---
title: "Securing Your Small/Home Office Network: pfSense VLAN Configuration"
excerpt: "Adding and configuring VLANs in pfSense."
category: "Network Security"
difficulty: "easy"
date: 2025-05-28
guide_series: securing-your-soho-network
part: 4
---
# Adding VLAN Interfaces in pfSense

Next, the LAN (local area network) port facing pfSense and connecting to the switch must be a trunk because it will carry all
traffic including **VLAN10** and **VLAN20** on one cable. On the pfSense side, the LAN NIC (network interface controller) is just
the physical parent interface (the actual LAN port you plug the Ethernet cable into); VLANs (virtual local area networks) are
created on top of it.

Log into your pfSense Web Dashboard using the web browser. From the top menu select ***Interfaces*** and then from the drop down
menu click on ***Assignments***.

![pfSense adding VLANs](/assets/images/31-pfsense-adding-vlans.png "pfSense adding VLANs")

1. ***VLANs***
2. **Add**


![pfSense adding VLANs](/assets/images/32-pfsense-adding-vlans.png "pfSense adding VLANs")

1. Ensure your LAN port is selected, in my case **re1** but your may be different, however it will say **lan** at the end
2. For **VLAN Tag** use `10`
3. For **Description** I used `Personal Devices` as I will used it for personal devices like Laptops, PCs, tablets, etc.
4. Make sure to click **Save**

![pfSense adding VLAN20](/assets/images/33-pfsense-adding-vlan20.png "pfSense adding VLAN20")

Repeat the process for `IoT and Untrusted Devices` VLAN but use `20` for **VLAN Tag**.

You should have the following list of interfaces for your VLANs:

![pfSense list of VLANs](/assets/images/34-pfsense-list-vlans.png "pfSense list of LANs")

We now need to assign the VLANs to an Interface.

![pfSense assigning VLANs to Interface](/assets/images/35-pfsense-assign-vlan.png "pfSense assigning VLANs to Interface")

1. Select ***Interfaces*** on the top menu
2. Click on ***Assignments*** from the drop-down menu
3. Select **VLAN 10 on re1 - lan** (yours may have something different than **re1** in the name)
4. Click **Add** and repeat for VLAN20 but select **VLAN 20 on re1 - lan**
5. Click **Save**

Your Interfaces should now look something like this:

![pfSense Interfaces with VLANs assigned](/assets/images/36-pfsense-interfaces-with-vlans.png "pfSense Interfaces with VLANs assigned")

You can modify the interface name by actually clicking on the name:

![pfSense changing Interface name](/assets/images/37-pfsense-changing-interface-name.png "pfSense changing Interface name")

![pfSense changing Interface name](/assets/images/38-pfsense-changing-interface-name.png "pfSense changing Interface name")

1. Make sure **Enabled** box is checked
2. Change the **Description** to be relevant, I used `VLAN10_Personal`
3. For **IPv4 Configuration Type** select **Static IPv4**
4. For **IPv4 Address** use `192.168.10.1/24` (up to 253 devices can connect)

Click **Save**.

The page will refresh and you will see:

![pfSense changing Interface name](/assets/images/39-pfsense-changing-interface-name.png "pfSense changing Interface name")

Click **Apply Changes**.

Repeat the steps for VLAN20 but use `192.168.20.1/24` in the last step and click **Save**.

![pfSense changing Interface name](/assets/images/40-pfsense-changing-interface-name.png "pfSense changing Interface name")

Your Interface Assignments page should look something like this:

![pfSense Interface Assignments completed](/assets/images/41-pfsense-interface-assignments-completed.png "pfSense Interface Assignments completed")

### Activating DHCP (Dynamic Host Configuration Protocol) on the Network

We now also need to make sure we have DHCP set up in pfSense that will handle handing out IP addresses on our network when devices
connect.

From the top menu select ***System*** and then click on ***Advanced*** from the drop down menu.

![pfSense activating Kea DHCP](/assets/images/42-pfsense-keadhcp.png "pfSense activating Kea DHCP")

1. Click ***Networking***
2. Select **Kea DHCP**

You can leave all the other options for now as default, scroll down and click **Save**.

Next, you need to activate it. In the top menu, click on ***Services*** and then ***DHCP Server*** from the drop down menu.

![pfSense activating DHCP on LAN](/assets/images/43-pfsense-landhcp.png "pfSense activating DHCP on LAN")

1. Click on ***LAN***
2. Make sure **Enable** checkbox is checked
3. You can leave the default values or adjust them as I’ve done (this means when a device joins 192.168.1.0/24 network, the DHCP
server will assign it an IP address within the range specified)

![pfSense activating DHCP on LAN](/assets/images/44-pfsense-landhcp.png "pfSense activating DHCP on LAN")

1. Set **DNS Servers** as `192.168.1.1`
2. Set **Gateway** as `192.168.1.1`
3. Use the default name for **Domain Name** (yours might be different, it’s pre-filled in light gray letters)
4. Use the default **Default Lease Time**
5. Use the default **Maximum Lease Time**

You can leave everything else at default, scroll down and click **Save**.

![pfSnese activating DHCP on VLAN10](/assets/images/45-pfsense-vlan10dhcp.png "pfSense activating DHCP on VLAN10")

![pfSnese activating DHCP on VLAN10](/assets/images/46-pfsense-vlan10dhcp.png "pfSense activating DHCP on VLAN10")

Repeat the steps for **VLAN10_PERSONAL** but make sure to use `192.168.10.1` for your **DNS Servers** and **Gateway**.

Do the same with **VLAN20_IOT_UNTRUSTED** settings, just remember to use IP addresses that start with `192.168.20.x`.

### Backup and Restore of your pfSense Configuration

At this point, we’re done with the pfSense web console configuration settings and will be moving on to set up the switch. To be on
the safe side and to avoid repeating all the work we've done so far, it’s recommended that you do a backup of all your settings on
pfSense.

![pfSense backup and restore](/assets/images/47-pfsense-backup-restore.png "pfSense backup and restore")

1. Click ***Diagnostics***
2. From drop-down menu select ***Backup & Restore***
3. Encryption is highly recommended, remember to use your password manager
4. Download the file

I recommend the tried and true **3-2-1 backup** strategy. Three copies of your data, on 2 different storage media, one stored
off-site. I have 1 on my **Admin_Device** hard drive, 1 on a USB, and 1 uploaded to a secure cloud storage service I trust (Proton
Drive).

In the screenshot above, you can see where you are able to upload your backup file to restore your configuration settings.

Next, we will add our switch and wireless access points.


