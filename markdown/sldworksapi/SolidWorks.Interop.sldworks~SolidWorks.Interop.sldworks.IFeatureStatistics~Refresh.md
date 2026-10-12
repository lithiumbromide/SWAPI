---
title: "Refresh Method (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "Refresh"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~Refresh.html"
---

# Refresh Method (IFeatureStatistics)

Refreshes the feature statistics in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Refresh() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.Boolean

value = instance.Refresh()
```

### C#

```csharp
System.bool Refresh()
```

### C++/CLI

```cpp
System.bool Refresh();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to refresh the feature statistics, false to not

## VBA Syntax

See [FeatureStatistics::Refresh](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~Refresh.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
