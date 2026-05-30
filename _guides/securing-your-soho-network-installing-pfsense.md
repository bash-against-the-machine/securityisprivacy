---
title: "Securing Your Small/Home Office (SOHO) Network: Installing pfSense"
excerpt: "Secure your home or small office network like a pro"
category: "Network Security"
difficulty: "medium"
cost: "$400 - $500"
date: 2025-05-28
---
# Installing pfSense

If you're not too computer savvy, it can be confusing to know where to locate the pfSense installer files and which one to choose
as well as how to actually install it on your mini PC. The next steps walk you through the process.

### Downloading the Installer

Go to [https://shop.netgate.com/products/netgate-installer](https://shop.netgate.com/products/netgate-installer) and for the
Installation Image option choose **AMD64 ISO IPMI/Virtual Machines** in the dropdown. You will have to add it to cart and go
through a checkout process even though the cost is $0.00.

### Creating USB Installation Disk

Once downloaded, if you're using a Linux, simply run `gunzip <file_name>` using terminal while in the directory where the
downloaded file is located. If you're using Windows, download 7-Zip and extract the file.

The file is a .iso file and can't simply be copied to USB disk to accomplish the installation. Plug in a USB drive in your
**Admin_Device** and if you're using Linux use the Disk utility to **Create Disk image** or download and install balenaEtcher
to handle this. I prefer balenaEtcher as it makes it very easy and has checks to make sure you're writing to the USB drive and
not your hard drive by mistake. If you're using Windows, download and use Rufus application to do the same.

### Installing pfSense on mini PC


