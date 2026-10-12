---
title: "BoltDiameter Property (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "BoltDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltDiameter.html"
---

# BoltDiameter Property (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::BoltDiameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~BoltDiameter.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BoltDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
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

See [HoleSeriesFeatureData::BoltDiameter](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~BoltDiameter.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::BoltHeadDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltHeadDiameter.html)
[IHoleSeriesFeatureData::NutDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~NutDiameter.html)
[IHoleSeriesFeatureData::Material Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Material.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
