---
title: "Material Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "Material"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Material.html"
---

# Material Property (IHoleSeriesFeatureData2)

Gets the name of the bolt material in this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Material As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
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

See [HoleSeriesFeatureData2::Material](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~Material.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## Remarks

The material value is not available in the SOLIDWORKS Toolbox database.

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::BoltDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~BoltDiameter.html)
[IHoleSeriesFeatureData2::BoltHeadDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~BoltHeadDiameter.html)
[IHoleSeriesFeatureData2::NutDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~NutDiameter.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
