---
title: "Elevation Property (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "Elevation"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Elevation.html"
---

# Elevation Property (IPolyLine)

Gets or sets the elevation of this 2D PolyLine.

## Syntax

### Visual Basic

```vb
Property Elevation As System.Double
```

### C#

```csharp
System.double Elevation {get; set;}
```

### JScript

```
function get,set Elevation : System.double
```

### Managed Extensions for C++

```
__property System.double get_Elevation();
__property void set_Elevation(
   System.double value
);
```

### C++/CLI

```cpp
property System.double Elevation {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Elevation (see **Remarks**)

## Remarks

Elevation is the distance between the World Coordinate System origin and the plane of this 2D PolyLine.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)

## Availability

DraftSight V1R1.4
