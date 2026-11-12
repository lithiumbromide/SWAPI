---
title: "FeatureTypes Property (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "FeatureTypes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureTypes.html"
---

# FeatureTypes Property (IFeatureStatistics)

Gets the types of features in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureTypes As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.Object

value = instance.FeatureTypes
```

### C#

```csharp
System.object FeatureTypes {get;}
```

### C++/CLI

```cpp
property System.Object^ FeatureTypes {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of the types of features as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [FeatureStatistics::FeatureTypes](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~FeatureTypes.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
