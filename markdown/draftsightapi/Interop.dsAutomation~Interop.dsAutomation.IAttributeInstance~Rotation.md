---
title: "Rotation Property (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "Rotation"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Rotation.html"
---

# Rotation Property (IAttributeInstance)

Gets or sets the insertion angle of the BlockAttribute instance.

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

Value between 0° and 360° for the angle at which to insert the BlockAttribute instance (see **Remarks**)

## Remarks

| This type of value... | Results in this type of rotation.... |
| --- | --- |
| Positive | Counter-clockwise |
| Negative | Clockwise |

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)

## Availability

DraftSight V1R2.0
