# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

For this assignment, I created a network-device example based on my background in communications. I used a parent class and a child class to demonstrate inheritance, class and instance namespaces, and shallow and deep copying.

## Implementation Documentation

### Parent Class

I created a parent class named `NetworkDevice` to represent basic network equipment. It included the class variable `category` and instance variables for the device's name, location, and configuration. The configuration contained a list of VLANs.

I used `__init__()` to set up each device and check that its name and location were not blank. The `describe()` method returned the device's information, and `__str__()` made that information readable when the object was printed.

### Child Class and Inheritance

I created `ManagedSwitch` as a child of `NetworkDevice`. It called `super().__init__()` to reuse the parent's setup and added a port count and management IP address. It also included its own class variable, `device_type`.

I overrode `describe()` to include the switch's additional information. The new `management_endpoint()` method returned a management URL using the switch's IP address.

### Class and Instance Namespaces

I created two `ManagedSwitch` objects and accessed `device_type` through both the class and an object. I then added a `maintenance_due` attribute to only the first switch.

I displayed the objects' `__dict__` values and the class namespace keys. The output showed that the added attribute belonged only to the first switch. I also checked that each newly created switch had its own configuration dictionary.

### Shallow and Deep Copying

I created a switch with VLAN 10, then made a shallow copy with `copy()` and a deep copy with `deepcopy()`. After I added VLAN 20 to the original, the original and shallow copy both displayed `[10, 20]`. The deep copy still displayed `[10]`.

I used `is` to check which objects shared data. The shallow copy shared the original's configuration dictionary, while the deep copy had a separate VLAN list.

### Testing

I completed `main()` by creating objects from both classes and calling their methods. The switch used the inherited `add_vlan()` method and its own version of `describe()`. I also called the namespace and copying functions.

The program ran successfully in Python 3. Assertions checked the expected results, and the output labeled each demonstration.

### Student-Created Extension

I added `add_vlan()` to let an existing device's configuration be updated. It accepted integer VLAN identifiers from 1 through 4094 and rejected duplicate entries. Since `ManagedSwitch` inherited this method, both classes could use the same validation.

### Edge Case Testing

I tested VLANs 1 and 4094, an empty starting list, duplicate entries, and invalid values such as 0, 4095, text, booleans, and missing values. I also tested blank names, missing locations, invalid port counts, and invalid IP addresses.

The program caught the expected errors, displayed a message, and continued running. I checked that rejected VLAN updates left the existing configuration unchanged.

### Real-World Application

This example could be expanded into a network inventory or configuration tool. Different device types could share basic information while keeping their own settings and methods. Keeping validation in one place could also make configuration changes easier to manage.

Each device had its own configuration when first created. The VLAN list used more memory as entries were added, and checking for duplicates required searching the list. A set could improve membership checks if the program needed to handle more entries.

## Discussion Board Reflection

### 1. What concepts or skills did you learn while completing this assignment?

I learned how a child class reused a parent's code while adding its own details. Using `__dict__` also helped me see the difference between shared class variables and attributes that belonged to one object.

### 2. What challenges did you encounter, and how did you overcome them?

The copying example needed the most attention. I checked the results after adding a VLAN to the original and used `is` to compare references. This showed why the shallow copy changed too, while the deep copy stayed independent.

### 3. Compare OOP to procedural programming.

With procedural programming, I would pass device information between functions. OOP kept that information with the methods that used it. This made the relationship between a device and its operations easier to follow.

### 4. Discuss the benefits of maintainability and reusability, including overhead, practical application development, and future use.

I could add another device type without rewriting the shared setup and VLAN checks. That would make maintenance easier as the program grew. Classes added some structure and memory overhead, so they might be unnecessary for a short script. For a larger network or cloud-management tool, I could reuse this approach to keep common behavior consistent.

## How to Run

From the `unit1_oop` folder, run:

```bash
python unit1_discussion.py
```

No extra packages were required. The program demonstrated device behavior without connecting to real equipment.
