---
title: "DeletePoint Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "DeletePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DeletePoint.html"
---

# DeletePoint Method (ISketchSpline)

Deletes a point on this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeletePoint( _
   ByVal Point As SketchPoint _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim Point As SketchPoint
Dim value As System.Boolean

value = instance.DeletePoint(Point)
```

### C#

```csharp
System.bool DeletePoint(
   SketchPoint Point
)
```

### C++/CLI

```cpp
System.bool DeletePoint(
   SketchPoint^ Point
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: [Sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) to delete (see **Remarks**)

### Return Value

True if the point is deleted, false if not

## VBA Syntax

See [SketchSpline::DeletePoint](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~DeletePoint.html).

## Remarks

This method does not work if Point specifies the start or end point of this spline.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::GetPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPointCount.html)
[ISketchSpline::GetPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints2.html)
[ISketchSpline::InsertPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~InsertPoint.html)
[ISketchSpline::IGetPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetPoints.html)
[ISketchSpline::IEnumPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IEnumPoints.html)
[ISplineHandle::SplinePointNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~SplinePointNumber.html)
[ISketchSpline::ShowInflectionPoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowInflectionPoints.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
