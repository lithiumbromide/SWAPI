---
title: "FeatureCount Property (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "FeatureCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureCount.html"
---

# FeatureCount Property (IFeatureStatistics)

Gets the number of features in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.Integer

value = instance.FeatureCount
```

### C#

```csharp
System.int FeatureCount {get;}
```

### C++/CLI

```cpp
property System.int FeatureCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of features

## VBA Syntax

See [FeatureStatistics::FeatureCount](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~FeatureCount.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
