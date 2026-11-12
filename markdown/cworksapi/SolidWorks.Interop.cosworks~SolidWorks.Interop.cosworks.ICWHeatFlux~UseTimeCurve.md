---
title: "UseTimeCurve Property (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "UseTimeCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~UseTimeCurve.html"
---

# UseTimeCurve Property (ICWHeatFlux)

Obsolete. Superseded by [ICWHeatFlux::UseTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~UseTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTimeCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Integer

instance.UseTimeCurve = value

value = instance.UseTimeCurve
```

### C#

```csharp
System.int UseTimeCurve {get; set;}
```

### C++/CLI

```cpp
property System.int UseTimeCurve {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use time curve, 0 to not

## VBA Syntax

See [CWHeatFlux::UseTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~UseTimeCurve.html).

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[ICWHeatFlux::GetTimeCurve Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~GetTimeCurve.html)
[ICWHeatFlux::SetTimeCurve Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
