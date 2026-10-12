---
title: "FastenerDefaultUnits Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "FastenerDefaultUnits"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerDefaultUnits.html"
---

# FastenerDefaultUnits Property (IHoleSeriesFeatureData2)

Gets the fastener default units for this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FastenerDefaultUnits As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim value As System.String

value = instance.FastenerDefaultUnits
```

### C#

```csharp
System.string FastenerDefaultUnits {get;}
```

### C++/CLI

```cpp
property System.String^ FastenerDefaultUnits {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fastener default units

## VBA Syntax

See [HoleSeriesFeatureData2::FastenerDefaultUnits](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~FastenerDefaultUnits.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::FastenerBottomHoleType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerBottomHoleType.html)
[IHoleSeriesFeatureData2::FastenerHoleCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerHoleCount.html)
[IHoleSeriesFeatureData2::FastenerTopHoleType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerTopHoleType.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
