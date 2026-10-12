---
title: "FastenerHoleCount Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "FastenerHoleCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerHoleCount.html"
---

# FastenerHoleCount Property (IHoleSeriesFeatureData2)

Gets the number of fastener holes in this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FastenerHoleCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim value As System.Integer

value = instance.FastenerHoleCount
```

### C#

```csharp
System.int FastenerHoleCount {get;}
```

### C++/CLI

```cpp
property System.int FastenerHoleCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of fastener holes

## VBA Syntax

See [HoleSeriesFeatureData2::FastenerHoleCount](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~FastenerHoleCount.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::FastenerBottomHoleType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerBottomHoleType.html)
[IHoleSeriesFeatureData2::FastenerDefaultUnits Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerDefaultUnits.html)
[IHoleSeriesFeatureData2::FastenerTopHoleType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerTopHoleType.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
