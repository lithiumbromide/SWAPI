---
title: "Thickness Property (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "Thickness"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Thickness.html"
---

# Thickness Property (IPolyLine)

Gets or sets the thickness of this 2D PolyLine.

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

Thickness is the extrusion depth along the [vector normal](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetNormal.html) to this entity.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::SetNormal Method ()](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetNormal.html)

## Availability

DraftSight V1R1.4
