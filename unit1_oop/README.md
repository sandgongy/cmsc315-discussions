# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Implementation documentation

The implementation modeled network infrastructure with `NetworkDevice` and `ManagedSwitch`. The parent stored the shared `category`, each device's name and location, and a nested configuration dictionary. Its constructor validated nonblank text. Its `describe()` and `__str__()` methods supplied readable output. The child inherited the parent behavior through `super().__init__()`, added the class variable `device_type`, and stored a port count and management IPv4 address. It added `management_endpoint()` and overrode `describe()` to display switch-specific information.

The namespace demonstration created two switches, accessed `device_type` through both the class and an object, and displayed the instance dictionaries and class dictionary keys. It added `maintenance_due` only to the first switch. Assertions confirmed that the second switch did not acquire that attribute and that independently constructed switches did not share configuration dictionaries.

The copying demonstration began with VLAN 10, created shallow and deep copies, and added VLAN 20 to the original. The original and shallow copy displayed `[10, 20]`, while the deep copy displayed `[10]`. Identity checks established that the shallow copy shared the configuration dictionary and that the deep copy held an independent VLAN list.

The student-created extension, `add_vlan()`, validated VLAN identifiers and rejected duplicates before mutation. It demonstrated how encapsulation grouped a device's data and validation rules. The configuration remained publicly accessible in this learning example; callers could bypass validation by editing it directly, so the design did not claim strict privacy or production security.

## Validation results

The program ran successfully with Python 3 and its built-in assertions enabled. It accepted boundary VLAN values 1 and 4094; rejected 0, 4095, negative values, text, booleans, missing values, and a duplicate VLAN; and confirmed rejected updates left the configuration unchanged. Constructor checks rejected blank names, missing locations, invalid port counts, blank management addresses, and malformed IPv4 addresses. Empty VLAN lists were valid initial states. The output reported descriptive errors and execution continued after each expected failure. The namespace and copying assertions also passed.

The command used was `python unit1_discussion.py` from this folder. No third-party packages were required. The displayed management endpoints used documentation-only IP addresses and did not initiate network connections.

## Memory and performance

Each independently constructed device received its own configuration dictionary and list. Class variables were resolved through class namespaces rather than duplicated in each instance dictionary. VLAN storage grew linearly with the number of stored identifiers. Duplicate detection scanned the list in O(n) time; appending took amortized O(1) time. A shallow copy duplicated the outer instance while sharing nested configuration, whereas a deep copy required time and memory proportional to the copied configuration. These estimates treated fixed device metadata as constant size. For a larger inventory, a set could improve membership checks, with a separate ordering strategy if stable display order remained necessary.

## Practical application

This model connected to communications equipment maintenance and future network or cloud automation. Shared device behavior could remain in the parent while additional subclasses represented routers or firewalls. Validation could keep an invalid VLAN request from changing the modeled configuration. The program simulated configuration management; it did not configure real equipment.

## Submission status

Code and documentation were completed and tested locally. The repository was created at https://github.com/sandgongy/cmsc315-discussions. Discussion submission status was tracked separately.
