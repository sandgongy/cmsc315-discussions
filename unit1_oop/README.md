# Unit 1: Python OOP, Namespaces, and Copying

## Overview

For this assignment, I used network devices as my example because of my background in communications. I built a basic device class and a managed switch class, then used them to show inheritance, namespaces, and copying in Python.

## What I Built

The parent class, `NetworkDevice`, stored a device's name, location, and VLAN configuration. It also had a shared `category` variable and a `describe()` method. I used `__str__()` so printing a device produced a readable description.

The child class, `ManagedSwitch`, reused that setup through `super().__init__()`. It added a port count, a management IP address, and its own class variable, `device_type`. Its version of `describe()` included the switch details, and `management_endpoint()` returned its management URL.

For the namespace example, I created two switches and added `maintenance_due` to just one of them. Printing their `__dict__` values showed that the other switch did not get that attribute. I also accessed `device_type` through both the class and an object to show where shared class information came from.

For copying, I started with a switch that had VLAN 10. After making shallow and deep copies, I added VLAN 20 to the original. The shallow copy also showed VLAN 20 because it shared the configuration dictionary. The deep copy kept only VLAN 10.

## My Extension and Testing

I added `add_vlan()` so a device could accept valid VLANs and reject invalid or duplicate entries. Valid values ranged from 1 to 4094.

The tests covered both boundaries, duplicate entries, an empty starting list, and invalid inputs such as text, booleans, and missing values. I also checked blank device names, invalid port counts, and bad IP addresses. The program printed an explanation for each rejected input and kept running. Assertions checked that failed VLAN updates did not change the existing configuration.

## Reflection

This assignment helped connect the idea of a class to something familiar: network equipment. A switch had the same basic information as another device, but it also needed details such as a port count and management address. Inheritance let those shared parts stay in one place.

The copying example was the part that needed the most attention. A separate object did not necessarily mean separate data. Adding VLAN 20 and checking the objects with `is` made the difference clear: the shallow copy shared the configuration, while the deep copy had its own.

Compared with procedural programming, OOP kept each device's information close to the methods that used it. That made it easier to see which operations belonged to which object. For a small script, setting up classes could take more work than necessary. For a larger network-management tool, though, reusing the parent class could save repeated code and make changes easier to manage.

The VLAN list used more memory as entries were added, and duplicate checks searched through it. A set could make those checks faster if the program needed to handle a larger collection.

## Running the Program

From the `unit1_oop` folder:

```bash
python unit1_discussion.py
```

The program used Python 3 with no extra packages. It only demonstrated the device behavior; it did not make changes to real equipment.
