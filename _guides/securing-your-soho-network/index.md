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

While there are arguably better solutions that approach Enterprise grade quality using Ubiquity UniFi ecosystem, you will be
locked in to a single vendor at double the cost of this set up.

## What You Will Need

| Equipment | Estimated Cost |
|---|---|
| Mini PC with dual Ethernet (for pfSense) | ~$200–$300 |
| Managed switch with VLAN support (e.g. TP-Link TL-SG105E) | ~$25–$45 |
| Two wireless access points | ~$25–$45 each |
| Admin laptop/PC (16 GB RAM recommended) | existing hardware |

## Naming Conventions and Text Styles in Guide

- The main device used to configure and manage the network will be refered to as **Admin_Device** in this guide
- Once pfSense is installed, the mini PC will be refered to as **pfSense_Appliance**
- The word **terminal** will refer to whatever terminal you're using in Linux (I prefer terminator) or Command Prompt or
Powershell prompt if you're on Windows. I will not provide Windows commands so you can use ChatGPT or other AI chatbot to
convert my commands to windows equivalent. I personally recommend that you install Ubuntu as WSL on your Windows to use instead
- Instructions for a command that has a variable input will enclose the input in carrots like this: `command <variable_input>`
- Input that is to be typed will be called out like this: `custom input to be typed`
- A button to be clicked or drop down selection to be selected will be in bold: **Click** or **Select**
- A menu selection on the page will be in bold italics: ***Menu***
- A block of code to run in your terminal:
```bash
sudo apt upgrade && sudo apt update -y
```

## Sections

[Introduction: The Network Sprawl Problem](/guides/securing-your-soho-network/01-introduction/)

[Installing pfSense](/guides/securing-your-soho-network/02-installing-pfsense/)
