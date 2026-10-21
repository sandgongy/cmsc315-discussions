# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This project demonstrated object-oriented programming in Python through a network-device simulation. A parent `NetworkDevice` class and a child `ManagedSwitch` class modeled inheritance and method overriding. Separate functions demonstrated class and instance namespaces and the differences between shallow and deep copying. The scenario connected to my communications background and interest in network and cloud automation.

## Implementation Summary

- **NetworkDevice (parent class):** I implemented the class variable `category`, a constructor with the instance variables `name` and `location`, and a nested configuration dictionary containing a VLAN list. The constructor validated nonblank text. The `describe()` method returned device information, and `__str__()` made objects readable when printed.
- **ManagedSwitch (child class):** I extended `NetworkDevice`, added the class variable `device_type`, and stored two additional instance variables: `port_count` and `management_ip`. The constructor checked the port count and IPv4 address, then called `super().__init__()`. I added `management_endpoint()` and overrode `describe()` to include switch details.
- **Namespace demonstration:** I created two switches, accessed `device_type` through both the class and an object, and added `maintenance_due` to only one switch. I displayed both instance dictionaries and the class namespace keys. Assertions confirmed that the added attribute belonged only to the first object and that separately constructed switches had independent configurations.
- **Copy demonstration:** I created an original switch with VLAN 10, made shallow and deep copies, and then added VLAN 20 to the original. The original and shallow copy showed `[10, 20]` because they shared the nested configuration. The deep copy remained `[10]`. Identity checks confirmed which objects shared data.
- **Main function:** I created parent and child objects, called inherited and overridden methods, ran both demonstrations, and checked additional edge cases with labeled output.

## Student-Created Extension

I added `add_vlan()` to validate configuration updates. It accepted integer VLAN identifiers from 1 through 4094 and rejected duplicates before changing the list. The method grouped the device's state and update rules together, although the configuration remained publicly accessible in this learning example.

I tested both valid boundaries, an empty initial list, duplicate VLANs, out-of-range numbers, strings, booleans, and missing values. Constructor tests also rejected blank names, missing locations, invalid port counts, and invalid IPv4 addresses. Expected exceptions were caught and printed, and assertions confirmed that rejected VLAN updates left the configuration unchanged. All checks passed and the program continued running.

## Reflection

This assignment demonstrated how classes grouped data and behavior, how inheritance extended a parent class, and how Python resolved class and instance attributes. Using `__dict__` made the distinction visible: `maintenance_due` appeared only on one switch, while `device_type` was accessed through both the class and an instance. Special methods such as `__init__` and `__str__` controlled initialization and readable output.

Reference sharing during copying required particular attention. Adding a VLAN after creating both copies and checking object identities showed why the shallow copy changed with the original while the deep copy remained independent. Validation before mutation also kept rejected requests from changing device state.

Procedural programming organized operations into functions that received data. OOP kept device state and related operations together and allowed `ManagedSwitch` to reuse parent behavior. This reduced repetition and provided a foundation for additional device types. Classes added structure and some overhead, so a small script might not need them. For larger network or cloud tools, reusable classes could simplify maintenance. VLAN storage grew linearly, and duplicate checks scanned the list; a set could improve membership checks if the model needed to scale.

## How to Run

From the `unit1_oop` folder, run:

```bash
python unit1_discussion.py
```

The program used Python 3 and the standard library. It printed the demonstrations and test results without connecting to or configuring real network equipment.
