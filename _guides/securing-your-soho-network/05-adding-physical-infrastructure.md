---
title: "Securing Your Small/Home Office Network: Adding Physical Infrastructure"
excerpt: "Adding and configuring the switch and wireless access points."
category: "Network Security"
difficulty: "medium"
date: 2025-05-28
guide_series: securing-your-soho-network
part: 5
---
# Adding and Configuring the Switch

This was a little tricky because to access the webGUI of the switch the default IP is 192.168.0.1, however, that is the IP address
of my Quantum Fiber Modem (and probably the default IP address of whatever ISP modem you’re using as well) which will result in
pulling up the modem webGUI and not the one for the switch.

The workaround is to not plug the switch into the LAN port (re1) on pfSense yet, so make sure it is not connected to the
**pfSense_Appliance**. Power on the switch and connect your **Admin_Device** to port 5 on the switch. Go to configure your wired
network settings and set your IP address for the Wired or Ethernet connection to be on the same network as the switch:
192.168.0.x (I used `192.168.0.15`). Set the **Netmask** to `255.255.255.0` and leave the **Gateway** blank for now.

![Switch Network Configuration](/assets/images/48-switch-network-config.png "Switch Network Configuration")

This is how it looks on Ubuntu settings. In Windows, you simply right click the internet connection icon in the tray in lower
right-hand corner and select **Network and Internet Settings**. Click on **Ethernet**. In the section that starts with IP
assignment it will have **Automatic** listed and an **Edit** button on the far-right of the section. Click **Edit** and select
**Manual** from the drop down menu at the top and toggle on **IPv4**. Fill in the same fields as above.

Now in your web browser, navigate to `192.168.0.1` and you’re presented with a login page for the web console of the switch:

![Switch login to web console](/assets/images/49-switch-webconsole-login.png "Switch login to web console")

Use `admin` for **User Name** and `admin` for the **Password**. You’ll be immediately prompted to change the password, utilize your
password manager here.

![Switch configuration](/assets/images/50-switch-configuration.png "Switch configuration")

1. Click ***System***
2. Click ***IP Setting***
3. Select **Disable** for **DHCP Setting**
4. Change **IP Address** to `192.168.1.5`, **Subnet Mask** to `255.255.255.0` and **Default Gateway** to `192.168.1.1`
(our pfSense will be the Gateway that will route all networks on the switch to the internet)
5. Click **Apply**

Use an Ethernet cable to connect the LAN port on your ***pfSense_Appliance*** to Port 1 on the switch. Now close the web browser on
your ***Admin_Device*** and go back to your **Internet and Network Settings** for the **Ethernet** and for **IPv4** change it from
**Manual** to **Automatic**. Disconnect and reconnect the Ethernet cable connecting you to Port 5 on the switch. When you reconnect,
pfSense DHCP LAN server should issue you an IP address automatically. Open the web browser and navigate to `192.168.1.5` and you
should be able to access the switch web console again.

![Switch VLAN configuration](/assets/images/51-switch-vlan-config.png "Switch VLAN configuration")

1. Click **VLAN**
2. Click **802.1Q VLAN**
3. Select **Enable**
4. Click **Apply**

Next steps are on the same page:

![Switch VLAN configuration](/assets/images/52-switch-vlan-config.png "Switch VLAN configuration")

1. For **VLAN ID** I used `10`
2. For **VLAN Name** I used `VLAN10`
3. For **Port 1** select **Tagged**
4. For **Port 2** select **Untagged** and leave all others as **Not Member**
5. Click **Add/Modify**

![Switch VLAN configuration](/assets/images/53-switch-vlan-config.png "Switch VLAN configuration")

Repeat the same for `VLAN20` but notice **Port 3** is **Untagged** and **Port 1** is **Tagged**, all others set to **Not Member**.

Your 802.1Q VLAN Configuration should look like this:

![Switch final VLAN configuration](/assets/images/57-switch-final-configuration.png "Switch final VLAN configuration")

Now let’s add PVIDs:

![Switch adding PVIDs](/assets/images/54-switch-adding-pvids.png "Switch adding PVIDs")

1. Click **VLAN**
2. Click **802.1Q VLAN PVID Setting**
3. Type `10` in **PVID**
4. Check **Port 2**
5. Click **Apply**

![Switch adding PVIDs](/assets/images/55-switch-adding-pvids.png "Switch adding PVIDs")

1. Type `20` in **PVID**
2. Check **Port 3**
3. Click **Apply**

Your page should now look like this:

![Switch final PVIDs configuration](/assets/images/56-switch-adding-pvids.png "Switch final PVIDs configuration")

What did we just do? We created `VLAN10` and `VLAN20` on our switch. Because **Port 1** will carry traffic from both VLANs to our
pfSense, we set **Port 1** as **Tagged** on each VLAN, this way pfSense will know which traffic belongs to each VLAN since they
will be on the same cable. This means our switch will add additional information to each packet so that pfSense knows which port to
route it to. Because all traffic connected to **Port 2** will be isolated to `VLAN10`, we can leave **Port 2** as **Untagged**.
All other ports are not members of `VLAN10` therefore they will not be able to reach devices in `VLAN10`. This same is repeated for
`VLAN20` and **Port 3**.

# Adding and Configuring VLAN10 Wireless Access Point
