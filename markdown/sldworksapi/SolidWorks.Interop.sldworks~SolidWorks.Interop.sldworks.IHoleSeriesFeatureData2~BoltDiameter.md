---
title: "BoltDiameter Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "BoltDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~BoltDiameter.html"
---

# BoltDiameter Property (IHoleSeriesFeatureData2)

Gets the diameter of the bolt in this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BoltDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim value As System.Double

value = instance.BoltDiameter
```

### C#

```csharp
System.double BoltDiameter {get;}
```

### C++/CLI

```cpp
property System.double BoltDiameter {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Diameter of bolt

## VBA Syntax

See [HoleSeriesFeatureData2::BoltDiameter](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~BoltDiameter.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::BoltHeadDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~BoltHeadDiameter.html)
[IHoleSeriesFeatureData2::Material Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Material.html)
[IHoleSeriesFeatureData2::NutDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~NutDiameter.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
