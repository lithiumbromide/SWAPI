---
title: "IsStyleSpline Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "IsStyleSpline"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsStyleSpline.html"
---

# IsStyleSpline Property (ISketchSpline)

Gets whether this spline is a style spline.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsStyleSpline As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Boolean

value = instance.IsStyleSpline
```

### C#

```csharp
System.bool IsStyleSpline {get;}
```

### C++/CLI

```cpp
property System.bool IsStyleSpline {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if a style spline, false if not

## VBA Syntax

See [SketchSpline::IsStyleSpline](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~IsStyleSpline.html).

## Examples

[Get Style Spline Curve Type (C#)](Get_Style_Spline_Curve_Type_Example_CSharp.htm)
[Get Style Spline Curve Type (VB.NET)](Get_Style_Spline_Curve_Type_Example_VBNET.htm)
[Get Style Spline Curve Type (VBA)](Get_Style_Spline_Curve_Type_Example_VB.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::CurveDegree Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveDegree.html)
[ISketchSpline::CurveType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveType.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
