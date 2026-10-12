---
title: "FeatureNames Property (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "FeatureNames"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureNames.html"
---

# FeatureNames Property (IFeatureStatistics)

Gets the names of the features in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureNames As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.Object

value = instance.FeatureNames
```

### C#

```csharp
System.object FeatureNames {get;}
```

### C++/CLI

```cpp
property System.Object^ FeatureNames {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of the names of the features

## VBA Syntax

See [FeatureStatistics::FeatureNames](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~FeatureNames.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
