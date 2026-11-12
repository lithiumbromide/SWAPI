---
title: "IGetSketchPoints Method (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "IGetSketchPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~IGetSketchPoints.html"
---

# IGetSketchPoints Method (IHoleSeriesFeatureData2)

Gets the center-hole sketch points in this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchPoints( _
   ByVal NCount As System.Integer _
) As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim NCount As System.Integer
Dim value As SketchPoint

value = instance.IGetSketchPoints(NCount)
```

### C#

```csharp
SketchPoint IGetSketchPoints(
   System.int NCount
)
```

### C++/CLI

```cpp
SketchPoint^ IGetSketchPoints(
   System.int NCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of center-hole sketch points

### Return Value

- in-process, unmanaged C++: Pointer to an array of center-hole [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IHoleSeriesFeatureData2::GetSketchPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPointsCount.html) to get the value for NCount.

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::GetSketchPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetSketchPoints.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
