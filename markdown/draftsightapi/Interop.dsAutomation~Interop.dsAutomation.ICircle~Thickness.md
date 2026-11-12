---
title: "Thickness Property (ICircle)"
project: ""
interface: "ICircle"
member: "Thickness"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircle~Thickness.html"
---

# Thickness Property (ICircle)

Gets or sets the thickness of this Circle.

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

Thickness is the extrusion depth along the [vector normal](Interop.dsAutomation~Interop.dsAutomation.ICircle~GetNormal.html) to this entity.

## See Also

[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[ICircle Members](Interop.dsAutomation~Interop.dsAutomation.ICircle_members.html)
[ICircle::SetNormal Method ()](Interop.dsAutomation~Interop.dsAutomation.ICircle~SetNormal.html)

## Availability

DraftSight V1R1.4
