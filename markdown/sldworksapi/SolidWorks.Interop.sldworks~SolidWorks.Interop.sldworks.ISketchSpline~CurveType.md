---
title: "CurveType Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "CurveType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveType.html"
---

# CurveType Property (ISketchSpline)

Gets or sets the type of curve for this style spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurveType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Integer

instance.CurveType = value

value = instance.CurveType
```

### C#

```csharp
System.int CurveType {get; set;}
```

### C++/CLI

```cpp
property System.int CurveType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of curve as defined in [swStyleSplineCurveType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStyleSplineCurveType_e.html)

## VBA Syntax

See [SketchSpline::CurveType](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~CurveType.html).

## Examples

[Get Style Spline Curve Type (C#)](Get_Style_Spline_Curve_Type_Example_CSharp.htm)
[Get Style Spline Curve Type (VB.NET)](Get_Style_Spline_Curve_Type_Example_VBNET.htm)
[Get Style Spline Curve Type (VBA)](Get_Style_Spline_Curve_Type_Example_VB.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::CurveDegree Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveDegree.html)
[ISketchSpline::IsStyleSpline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsStyleSpline.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
