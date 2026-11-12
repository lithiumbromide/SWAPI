---
title: "GetSketchPointsCount Method (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "GetSketchPointsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetSketchPointsCount.html"
---

# GetSketchPointsCount Method (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::GetSketchPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPointsCount.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPointsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim value As System.Integer

value = instance.GetSketchPointsCount()
```

### C#

```csharp
System.int GetSketchPointsCount()
```

### C++/CLI

```cpp
System.int GetSketchPointsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of center-hole sketch points in this hole series

## VBA Syntax

See [HoleSeriesFeatureData::GetSketchPointsCount](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~GetSketchPointsCount.html).

## Remarks

Call this method before calling [IHoleSeriesFeatureData::IGetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData~IGetSketchPoints.html) to get the size of the array for that method.

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::GetSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetSketchPoints.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
