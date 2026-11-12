---
title: "NutDiameter Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "NutDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~NutDiameter.html"
---

# NutDiameter Property (IHoleSeriesFeatureData2)

Gets the diameter of the nut in this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NutDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim value As System.Double

value = instance.NutDiameter
```

### C#

```csharp
System.double NutDiameter {get;}
```

### C++/CLI

```cpp
property System.double NutDiameter {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Diameter of nut

## VBA Syntax

See [HoleSeriesFeatureData2::NutDiameter](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~NutDiameter.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::BoltDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~BoltDiameter.html)
[IHoleSeriesFeatureData2::BoltHeadDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~BoltHeadDiameter.html)
[IHoleSeriesFeatureData2::Material Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Material.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
