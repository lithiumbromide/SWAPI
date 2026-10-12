---
title: "BoltHeadDiameter Property (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "BoltHeadDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltHeadDiameter.html"
---

# BoltHeadDiameter Property (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::BoltHeadDiameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~BoltHeadDiameter.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BoltHeadDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim value As System.Double

value = instance.BoltHeadDiameter
```

### C#

```csharp
System.double BoltHeadDiameter {get;}
```

### C++/CLI

```cpp
property System.double BoltHeadDiameter {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Diameter of head of the bolt

## VBA Syntax

See [HoleSeriesFeatureData::BoltHeadDiameter](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~BoltHeadDiameter.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::BoltDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltDiameter.html)
[IHoleSeriesFeatureData::NutDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~NutDiameter.html)
[IHoleSeriesFeatureData::Material Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Material.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
