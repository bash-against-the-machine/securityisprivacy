---
title: "Securing Your Small/Home Office (SOHO) Network"
excerpt: "A complete guide to segmenting your home or small office network using pfSense, VLANs, and a managed switch to limit the
damage and spread of any compromise on your network."
category: "Network Security"
difficulty: "medium"
cost: "$400 - $500"
date: 2026-05-28
is_index: true
guide_series: securing-your-soho-network
part: 0
permalink: /guides/securing-your-soho-network/
---

Most small and home office networks are "flat"(every device shares the same network). This means a single compromised device 
(a guest on WiFi, a vulnerable smart thermostat, a hacked printer) can see and attack everything else.
This is exactly how ransomware spreads so quickly in small businesses.

This guide walks you through building a properly segmented network using **pfSense** as your firewall, a **managed switch**,
and **VLANs** to isolate trusted devices, IoT gadgets, and guest traffic from one another. A device compromised on one segment
cannot reach devices on another.

## What You Will Need

| Equipment | Estimated Cost |
|---|---|
| Mini PC with dual Ethernet (for pfSense) | ~$135–$300 |
| Managed switch with VLAN support (e.g. TP-Link TL-SG105E) | ~$25–$45 |
| Two wireless access points | ~$25–$45 each |
| Admin laptop/PC (16 GB RAM recommended) | existing hardware |

## Naming Conventions and Text Styles in Guide



## Sections

[Introduction: The Network Sprawl Problem](/guides/securing-your-soho-network/01-introduction/)

[Installing pfSense](/guides/securing-your-soho-network/02-installing-pfsense/)
