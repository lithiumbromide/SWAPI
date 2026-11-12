---
title: "CurveDegree Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "CurveDegree"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveDegree.html"
---

# CurveDegree Property (ISketchSpline)

Gets or sets the degree of curve for this Bezier curve style spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurveDegree As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Integer

instance.CurveDegree = value

value = instance.CurveDegree
```

### C#

```csharp
System.int CurveDegree {get; set;}
```

### C++/CLI

```cpp
property System.int CurveDegree {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Degree of curve or -1 if not a Bezier curve style spline

## VBA Syntax

See [SketchSpline::CurveDegree](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~CurveDegree.html).

## Remarks

This property is only valid for a style spline whose [curve type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveType.html) is [swStyleSplineCurveType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStyleSplineCurveType_e.html).BezierCurve.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::IsStyleSpline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsStyleSpline.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
