"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class NetworkDevice:
    category = "Network infrastructure"

    def __init__(self, name, location):
        self.name = self._require_text(name, "name")
        self.location = self._require_text(location, "location")
        self.configuration = {"vlans": []}

    @staticmethod
    def _require_text(value, label):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{label} must contain nonblank text")
        return value.strip()

    def describe(self):
        return f"{self.name} at {self.location}"

    def __str__(self):
        return self.describe()

    # Student-created extension: validated configuration updates kept together
    # with device state. A failed update leaves the configuration unchanged.
    def add_vlan(self, vlan):
        if type(vlan) is not int or not 1 <= vlan <= 4094:
            raise ValueError("VLAN must be an integer from 1 through 4094")
        if vlan in self.configuration["vlans"]:
            raise ValueError("VLAN already exists")
        self.configuration["vlans"].append(vlan)


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ManagedSwitch(NetworkDevice):
    device_type = "Managed switch"

    def __init__(self, name, location, port_count, management_ip):
        if type(port_count) is not int or port_count <= 0:
            raise ValueError("port_count must be a positive integer")
        management_ip = self._require_text(management_ip, "management_ip")
        from ipaddress import IPv4Address
        IPv4Address(management_ip)
        super().__init__(name, location)
        self.port_count = port_count
        self.management_ip = management_ip

    def management_endpoint(self):
        return f"https://{self.management_ip}"

    def describe(self):
        return (f"{super().describe()}: {self.port_count} ports, "
                f"management IP {self.management_ip}, "
                f"VLANs {self.configuration['vlans']}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    first = ManagedSwitch("Access-1", "Office", 24, "192.0.2.10")
    second = ManagedSwitch("Access-2", "Lab", 48, "192.0.2.11")
    print("Class access:", ManagedSwitch.device_type)
    print("Object access:", first.device_type)
    first.maintenance_due = True
    print("First instance namespace:", first.__dict__)
    print("Second instance namespace:", second.__dict__)
    print("Child class namespace keys:", sorted(ManagedSwitch.__dict__))
    print("Inherited category:", NetworkDevice.__dict__["category"])
    assert first.device_type == ManagedSwitch.device_type
    assert "maintenance_due" not in second.__dict__
    assert first.configuration is not second.configuration


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = ManagedSwitch("Core-1", "Server room", 48, "192.0.2.1")
    original.add_vlan(10)
    shallow = copy(original)
    deep = deepcopy(original)
    original.add_vlan(20)
    # A shallow copy creates an outer object but shares nested configuration.
    # A deep copy recursively duplicates that configuration and its VLAN list.
    print("Original:", original)
    print("Shallow copy (shared configuration):", shallow)
    print("Deep copy (independent configuration):", deep)
    print("Shallow shares dictionary:", shallow.configuration is original.configuration)
    print("Deep shares list:", deep.configuration["vlans"] is original.configuration["vlans"])
    assert shallow is not original
    assert shallow.configuration is original.configuration
    assert deep.configuration["vlans"] == [10]
    assert deep.configuration["vlans"] is not original.configuration["vlans"]


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    parent = NetworkDevice("Router-1", "Main office")
    print("Parent:", parent)
    assert parent.configuration["vlans"] == []
    parent.add_vlan(1)
    parent.add_vlan(4094)
    assert parent.configuration["vlans"] == [1, 4094]

    child = ManagedSwitch("Access-3", "Training room", 24, "192.0.2.12")
    child.add_vlan(100)  # Inherited method
    print("Child override:", child.describe())
    print("Child-specific method:", child.management_endpoint())
    assert isinstance(child, NetworkDevice)
    assert child.management_endpoint() == "https://192.0.2.12"

    print("\n=== Edge Cases ===")
    for invalid in (0, 4095, -1, "10", True, None, 1):
        before = deepcopy(parent.configuration)
        try:
            parent.add_vlan(invalid)
        except ValueError as error:
            print(f"Rejected VLAN {invalid!r}: {error}")
        else:
            raise AssertionError(f"Accepted invalid/duplicate VLAN {invalid!r}")
        assert parent.configuration == before

    invalid_constructors = [
        lambda: NetworkDevice("  ", "Office"),
        lambda: NetworkDevice("Router", None),
        lambda: ManagedSwitch("Switch", "Lab", 0, "192.0.2.1"),
        lambda: ManagedSwitch("Switch", "Lab", True, "192.0.2.1"),
        lambda: ManagedSwitch("Switch", "Lab", 24, "999.0.0.1"),
        lambda: ManagedSwitch("Switch", "Lab", 24, ""),
    ]
    for create_invalid in invalid_constructors:
        try:
            create_invalid()
        except ValueError as error:
            print("Rejected invalid device:", error)
        else:
            raise AssertionError("Accepted invalid device")
    print("All edge-case checks passed; execution continued.")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
