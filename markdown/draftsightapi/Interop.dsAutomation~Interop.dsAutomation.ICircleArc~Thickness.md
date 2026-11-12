---
title: "Thickness Property (ICircleArc)"
project: ""
interface: "ICircleArc"
member: "Thickness"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircleArc~Thickness.html"
---

# Thickness Property (ICircleArc)

Gets or sets the thickness of this circle Arc.

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

Thickness is the extrusion depth along the [vector normal](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetNormal.html) to this entity.

## See Also

[ICircleArc Interface](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
[ICircleArc Members](Interop.dsAutomation~Interop.dsAutomation.ICircleArc_members.html)
[ICircleArc::SetNormal Method ()](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~SetNormal.html)

## Availability

DraftSight V1R1.4
