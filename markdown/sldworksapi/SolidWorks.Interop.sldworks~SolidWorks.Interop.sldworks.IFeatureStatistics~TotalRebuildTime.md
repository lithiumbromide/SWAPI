---
title: "TotalRebuildTime Property (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "TotalRebuildTime"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~TotalRebuildTime.html"
---

# TotalRebuildTime Property (IFeatureStatistics)

Gets the time, in seconds, it takes to rebuild (update) all features in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TotalRebuildTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.Double

value = instance.TotalRebuildTime
```

### C#

```csharp
System.double TotalRebuildTime {get;}
```

### C++/CLI

```cpp
property System.double TotalRebuildTime {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Time, in seconds, it takes to rebuild (update) all features

## VBA Syntax

See [FeatureStatistics::TotalRebuildTime](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~TotalRebuildTime.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)
[IFeatureStatistics::FeatureUpdatePercentageTimes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureUpdatePercentageTimes.html)
[IFeatureStatistics::FeatureUpdateTimes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureUpdateTimes.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
