---
title: "ReverseDirection Property (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "ReverseDirection"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~ReverseDirection.html"
---

# ReverseDirection Property (ICWHeatFlux)

Obsolete. Superseded by [ICWHeatFlux::ReverseDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~ReverseDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Integer

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.int ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.int ReverseDirection {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse direction, 0 to not

## VBA Syntax

See [CWHeatFlux::ReverseDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~ReverseDirection.html).

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::HFValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~HFValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
