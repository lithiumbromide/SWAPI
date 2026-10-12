---
title: "FastenerTopHoleType Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "FastenerTopHoleType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerTopHoleType.html"
---

# FastenerTopHoleType Property (IHoleSeriesFeatureData2)

Gets the fastener top hole type for this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FastenerTopHoleType As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim value As System.Short

value = instance.FastenerTopHoleType
```

### C#

```csharp
System.short FastenerTopHoleType {get;}
```

### C++/CLI

```cpp
property System.short FastenerTopHoleType {
   System.short get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fastener top hole type as defined in [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

## VBA Syntax

See [HoleSeriesFeatureData2::FastenerTopHoleType](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~FastenerTopHoleType.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::FastenerBottomHoleType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerBottomHoleType.html)
[IHoleSeriesFeatureData2::FastenerDefaultUnits Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerDefaultUnits.html)
[IHoleSeriesFeatureData2::FastenerHoleCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~FastenerHoleCount.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
