---
title: "IGetSketchPoints Method (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "IGetSketchPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetSketchPoints.html"
---

# IGetSketchPoints Method (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::IGetSketchPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~IGetSketchPoints.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchPoints( _
   ByVal NCount As System.Integer _
) As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
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

Before calling this method, call [IHoleSeriesFeatureData::GetSketchPointsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData~GetSketchPointsCount.html) to get the value for NCount.

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::GetSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetSketchPoints.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
