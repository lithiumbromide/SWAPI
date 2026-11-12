---
title: "Material Property (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "Material"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Material.html"
---

# Material Property (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::Material](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~Material.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Material As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim value As System.String

value = instance.Material
```

### C#

```csharp
System.string Material {get;}
```

### C++/CLI

```cpp
property System.String^ Material {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bolt material name

## VBA Syntax

See [HoleSeriesFeatureData::Material](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~Material.html).

## Remarks

The material value is not available in the SOLIDWORKS Toolbox database.

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::BoltDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltDiameter.html)
[IHoleSeriesFeatureData::BoltHeadDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltHeadDiameter.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
