---
title: "FeatureUpdatePercentageTimes Property (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "FeatureUpdatePercentageTimes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureUpdatePercentageTimes.html"
---

# FeatureUpdatePercentageTimes Property (IFeatureStatistics)

Gets the percentages of time it takes to update (rebuild) each feature in a part document relative to the total time it takes to update all features in that part document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureUpdatePercentageTimes As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.Object

value = instance.FeatureUpdatePercentageTimes
```

### C#

```csharp
System.object FeatureUpdatePercentageTimes {get;}
```

### C++/CLI

```cpp
property System.Object^ FeatureUpdatePercentageTimes {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of percentages of time it takes to update (rebuild) each feature in a part document relative to the total time it takes to update all features in that part document

## VBA Syntax

See [FeatureStatistics::FeatureUpdatePercentageTimes](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~FeatureUpdatePercentageTimes.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)
[IFeatureStatistics::FeatureUpdateTimes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureUpdateTimes.html)
[IFeatureStatistics::TotalRebuildTime Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~TotalRebuildTime.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
