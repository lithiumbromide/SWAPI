---
title: "FeatureUpdateTimes Property (IFeatureStatistics)"
project: "SOLIDWORKS API Help"
interface: "IFeatureStatistics"
member: "FeatureUpdateTimes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureUpdateTimes.html"
---

# FeatureUpdateTimes Property (IFeatureStatistics)

Gets the times, in seconds, it takes to update (rebuild) each feature in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureUpdateTimes As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureStatistics
Dim value As System.Object

value = instance.FeatureUpdateTimes
```

### C#

```csharp
System.object FeatureUpdateTimes {get;}
```

### C++/CLI

```cpp
property System.Object^ FeatureUpdateTimes {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of times, in seconds, it takes to udpate (rebuild) each feature in a part document

## VBA Syntax

See [FeatureStatistics::FeatureUpdateTimes](ms-its:sldworksapivb6.chm::/sldworks~FeatureStatistics~FeatureUpdateTimes.html).

## Examples

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

## See Also

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.html)
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html)
[IFeatureStatistics::FeatureUpdatePercentageTimes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureUpdatePercentageTimes.html)
[IFeatureStatistics::TotalRebuildTime Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~TotalRebuildTime.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
