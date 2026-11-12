---
title: "Rotation Property (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "Rotation"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~Rotation.html"
---

# Rotation Property (IBlockInstance)

Gets or sets the angle by which to rotate the Block instance.

## Syntax

### Visual Basic

```vb
Property Rotation As System.Double
```

### C#

```csharp
System.double Rotation {get; set;}
```

### JScript

```
function get,set Rotation : System.double
```

### Managed Extensions for C++

```
__property System.double get_Rotation();
__property void set_Rotation(
   System.double value
);
```

### C++/CLI

```cpp
property System.double Rotation {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Angle by which to rotate the Block instance (see **Remarks**)

## Remarks

Use a positive value to rotate the Block instance counterclockwise and a negative value to rotate the Block instance clockwise.

## See Also

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)

## Availability

DraftSight V1R1.1
