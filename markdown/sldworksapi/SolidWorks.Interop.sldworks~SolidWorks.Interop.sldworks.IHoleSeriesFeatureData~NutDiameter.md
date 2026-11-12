---
title: "NutDiameter Property (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "NutDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~NutDiameter.html"
---

# NutDiameter Property (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::NutDiameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~NutDiameter.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NutDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
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

See [HoleSeriesFeatureData::NutDiameter](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~NutDiameter.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::BoltDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltDiameter.html)
[IHoleSeriesFeatureData::BoltHeadDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltHeadDiameter.html)
[IHoleSeriesFeatureData::Material Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Material.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
