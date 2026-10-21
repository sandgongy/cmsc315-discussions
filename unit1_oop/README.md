# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

For this assignment, I created a network-device example based on my background in communications. I applied the parent class and child class to illustrate inheritance, class namespace, instance namespace, shallow copying and deep copying.

## Implementation Documentation

### Parent Class

I developed a super-class NetworkDevice to define basic network equipment. It contained the class variable ‘category' and instance variables for name, location and configuration of the device. A list of VLANs was included in the configuration.

Each device was set up using `__init__()` and was tested to ensure that its name and location weren't empty. The method describe() retrieved the information of the device and the method __str__() returned the information into readable form when the device was printed.

Child class and inheritance is an article of faith.Child class and inheritance is a faith.

ManagedSwitch is a child of NetworkDevice class. It invoked super().__init__() to inherit the parent's initialisation, and added a port count and management IP address. It was also accompanied by its own class variable called `device_type`.

I overrode describe so that it will contain the extra info for the switch. A management URL was returned by the new `management_endpoint()` method, based on the switch's IP address.

### Class and Instance Namespaces

I made two objects of the type `ManagedSwitch` and used both the class and an object to call the device_type. I've then added a `maintenance_due` attribute to the first switch only.

Printed the attributes of the objects (their `__dict__`), and the keys of the class (their namespace). This led to the output indicating that the added attribute only applied to the first switch. I also verified that every switch created also included a configuration dictionary.

Shallow Copying and Deep Copying.

I have made a switch with VLAN 10, then a shallow copy using the copy() function and a deep copy using deepcopy(). I added VLAN 20 to the original, and when it was displayed, both the original and the shallow copy showed `[10, 20]`. The deep copy still displayed `[10]`.

To see which objects had data in common, I used the test `is`. The shallow one shared the same configuration dictionary and the deep one had a list of VLANs.

### Testing

Made objects of both classes and called their methods to complete `main()`. The switch used the inherited `add_vlan()` method and its own version of `describe()`. I also called the namespace and copying functions.

The program was successfully run in Python 3. The expected results were checked by assertions and the output named the demonstrations.

### Student-Created Extension

I added add_vlan() to allow for updating the configuration of an existing device. It could assign integer VLAN IDS from 1 through 4094 and it would not accept duplicates. This method was inherited from `ManagedSwitch`, thus allowing the same validation for both classes.

### Edge Case Testing

I tried the following: VLANs 1 and 4094, a blank starting list, a duplicate list, invalid values (0, 4095, Text, Booleans, empty), etc. I also tried invalid port numbers, blank names, missing locations and invalid IP address.

The program identified the expected errors and printed a message and then ran. I verified that the old configuration did not change when the update to the VLAN was rejected.

### Real-World Application

This example could be extended to a network inventory or configuration tool. Different device types might have the same information but use a variety of methods and settings. Having validation centralized may facilitate configuration changes as well.

The initial configuration for each device was different. As more VLANs were added, the VLAN list consumed more memory, and to check for a duplicate VLAN, the list had to be searched. In a scenario where there were more entries to process, a set could be used as an improvement to membership checks.

## Discussion Board Reflection

### 1. What concepts or skills did you learn while completing this assignment?

I was learning how to make a pie chart that shows the details of a child class using a parent class's code. Also, by using the `__dict__` property I was able to visually distinguish between shared class variables and variables that were attributes to a single object.

### 2. What challenges did you encounter, and how did you overcome them?

The copy example required the most work. After adding a VLAN to the original, I checked the results, and used is to compare references. This showed why the shallow copy changed too, while the deep copy stayed independent.

### 3. Compare OOP with procedural programming.

In procedural programming, I would send information about the device between functions. In an OOP, it was retained by the methods which used it. This facilitated the relationship of the device and its operation.

### 4. Discuss the benefits of maintainability and reusability, including overhead, practical application development, and future use.

I can add another device type without having to rewrite shared setup & VLAN checks. That would make the maintenance effort easier as the program expands. Classes introduced some structure and memory overhead, which might not be necessary for a short script. If I was to have a larger network or cloud-management tool I could apply this again to maintain uniform behavior.
## How to Run

From the `unit1_oop` folder, run:

```bash
python unit1_discussion.py
```

No extra packages were required. The program demonstrated device behavior without connecting to real equipment.
