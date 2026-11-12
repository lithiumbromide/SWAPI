---
title: "SurfaceBodiesCount Property (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "SurfaceBodiesCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~SurfaceBodiesCount.html"
---

# SurfaceBodiesCount Property (IFeatureStatistics)

Gets the number of surface bodies in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SurfaceBodiesCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.Integer

value = instance.SurfaceBodiesCount
```

### C#

```csharp
System.int SurfaceBodiesCount {get;}
```

### C++/CLI

```cpp
property System.int SurfaceBodiesCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of surface bodies

## VBA Syntax

See [FeatureStatistics::SurfaceBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~SurfaceBodiesCount.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)
[IFeatureStatistics::SolidBodiesCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~SolidBodiesCount.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
