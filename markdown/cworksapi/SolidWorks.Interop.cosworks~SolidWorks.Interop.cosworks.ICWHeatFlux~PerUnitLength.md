---
title: "PerUnitLength Property (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "PerUnitLength"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~PerUnitLength.html"
---

# PerUnitLength Property (ICWHeatFlux)

Obsolete. Superseded by [ICWHeatFlux::PerUnitLength2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~PerUnitLength2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property PerUnitLength As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Integer

instance.PerUnitLength = value

value = instance.PerUnitLength
```

### C#

```csharp
System.int PerUnitLength {get; set;}
```

### C++/CLI

```cpp
property System.int PerUnitLength {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

True if heat flux uses per unit length while selecting beam bodies, false if not

## VBA Syntax

See [CWHeatFlux::PerUnitLength](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~PerUnitLength.html).

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
