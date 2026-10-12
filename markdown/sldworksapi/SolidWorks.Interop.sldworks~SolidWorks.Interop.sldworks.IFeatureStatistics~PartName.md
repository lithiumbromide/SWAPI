---
title: "PartName Property (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "PartName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~PartName.html"
---

# PartName Property (IFeatureStatistics)

Gets the name of the part document whose feature statistics you want.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PartName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.String

value = instance.PartName
```

### C#

```csharp
System.string PartName {get;}
```

### C++/CLI

```cpp
property System.String^ PartName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of part document

## VBA Syntax

See [FeatureStatistics::PartName](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~PartName.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
