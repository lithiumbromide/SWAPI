---
title: "InsertPoint Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "InsertPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~InsertPoint.html"
---

# InsertPoint Method (ISketchSpline)

Inserts a point at the specified coordinates of this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertPoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.InsertPoint(X, Y, Z)
```

### C#

```csharp
System.bool InsertPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool InsertPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate on this spline
- `Y`: Y coordinate on this spline
- `Z`: Z coordinate on this spline

### Return Value

True if a point is added to the spline, false if not

## VBA Syntax

See [SketchSpline::InsertPoint](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~InsertPoint.html).

## Remarks

This method works only if X, Y, and Z specify a location on this spline. You cannot add a new point that is not on this spline.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::DeletePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~DeletePoint.html)
[ISketchSpline::GetPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPointCount.html)
[ISketchSpline::GetPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetPoints2.html)
[ISketchSpline::IEnumPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IEnumPoints.html)
[ISplineHandle::SplinePointNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~SplinePointNumber.html)
[ISketchSpline::ShowInflectionPoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowInflectionPoints.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
