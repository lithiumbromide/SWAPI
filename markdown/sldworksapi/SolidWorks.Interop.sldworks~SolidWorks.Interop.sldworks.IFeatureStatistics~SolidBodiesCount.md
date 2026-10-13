---
title: "SolidBodiesCount Property (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "SolidBodiesCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~SolidBodiesCount.html"
---

# SolidBodiesCount Property (IFeatureStatistics)

Gets the number of solid bodies in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SolidBodiesCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.Integer

value = instance.SolidBodiesCount
```

### C#

```csharp
System.int SolidBodiesCount {get;}
```

### C++/CLI

```cpp
property System.int SolidBodiesCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of solid bodies

## VBA Syntax

See [FeatureStatistics::SolidBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~SolidBodiesCount.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)
[IFeatureStatistics::SurfaceBodiesCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~SurfaceBodiesCount.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
