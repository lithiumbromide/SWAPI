---
title: "PerUnitLength2 Property (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "PerUnitLength2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~PerUnitLength2.html"
---

# PerUnitLength2 Property (ICWHeatFlux)

Gets or sets whether heat flux uses per unit length while selecting beam bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property PerUnitLength2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Boolean

instance.PerUnitLength2 = value

value = instance.PerUnitLength2
```

### C#

```csharp
System.bool PerUnitLength2 {get; set;}
```

### C++/CLI

```cpp
property System.bool PerUnitLength2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true if heat flux uses per unit length while selecting beam bodies, 0 or false if not

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
