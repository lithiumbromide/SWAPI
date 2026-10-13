---
title: "FeatureStatistics Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureStatistics"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureStatistics.html"
---

# FeatureStatistics Property (IFeatureManager)

Gets statistics about the features in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureStatistics As FeatureStatistics
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As FeatureStatistics

value = instance.FeatureStatistics
```

### C#

```csharp
FeatureStatistics FeatureStatistics {get;}
```

### C++/CLI

```cpp
property FeatureStatistics^ FeatureStatistics {
   FeatureStatistics^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Feature statistics](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureStatistics.html)

## VBA Syntax

See [FeatureManager::FeatureStatistics](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureStatistics.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
