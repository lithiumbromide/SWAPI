---
title: "Elevation Property (IHatch)"
project: ""
interface: "IHatch"
member: "Elevation"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatch~Elevation.html"
---

# Elevation Property (IHatch)

Gets or sets the elevation of this Hatch.

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

Elevation is the distance between the World Coordinate System origin and the plane of this Hatch.

## See Also

[IHatch Interface](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)
[IHatch Members](Interop.dsAutomation~Interop.dsAutomation.IHatch_members.html)

## Availability

DraftSight V1R1.4
