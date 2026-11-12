---
title: "Thickness Property (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "Thickness"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Thickness.html"
---

# Thickness Property (IAttributeInstance)

Gets or sets the thickness of this BlockAttribute.

## Syntax

### Visual Basic

```vb
Property Thickness As System.Double
```

### C#

```csharp
System.double Thickness {get; set;}
```

### JScript

```
function get,set Thickness : System.double
```

### Managed Extensions for C++

```
__property System.double get_Thickness();
__property void set_Thickness(
   System.double value
);
```

### C++/CLI

```cpp
property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Thickness; 0 for no thickness, a positive value extrudes upward, a negative value extrudes downward (see **Remarks**)

## Remarks

Thickness is the extrusion depth along the vector normal to this entity.

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)

## Availability

DraftSight V1R1.4
