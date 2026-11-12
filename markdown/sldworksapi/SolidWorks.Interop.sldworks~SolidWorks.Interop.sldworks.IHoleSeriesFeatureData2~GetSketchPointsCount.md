---
title: "GetSketchPointsCount Method (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "GetSketchPointsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPointsCount.html"
---

# GetSketchPointsCount Method (IHoleSeriesFeatureData2)

Gets the number of center-hole sketch points in this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPointsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
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

See [HoleSeriesFeatureData2::GetSketchPointsCount](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~GetSketchPointsCount.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## Remarks

Call this method before calling [IHoleSeriesFeatureData::IGetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData~IGetSketchPoints.html) to get the size of the array for that method.

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::GetSketchPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPoints.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
