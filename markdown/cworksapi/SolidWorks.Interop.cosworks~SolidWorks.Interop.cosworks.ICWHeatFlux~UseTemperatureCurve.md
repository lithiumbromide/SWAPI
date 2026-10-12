---
title: "UseTemperatureCurve Property (ICWHeatFlux)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: "UseTemperatureCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~UseTemperatureCurve.html"
---

# UseTemperatureCurve Property (ICWHeatFlux)

Obsolete. Superseded by [ICWHeatFlux::UseTemperatureCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux~UseTemperatureCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTemperatureCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
Dim value As System.Integer

instance.UseTemperatureCurve = value

value = instance.UseTemperatureCurve
```

### C#

```csharp
System.int UseTemperatureCurve {get; set;}
```

### C++/CLI

```cpp
property System.int UseTemperatureCurve {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use temperature curve, 0 to not

## VBA Syntax

See [CWHeatFlux::UseTemperatureCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux~UseTemperatureCurve.html).

## See Also

[ICWHeatFlux Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html)
[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
