---
title: "IGetCurve Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "IGetCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetCurve.html"
---

# IGetCurve Method (ISketchSegment)

Gets the underlying curve for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCurve() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As Curve

value = instance.IGetCurve()
```

### C#

```csharp
Curve IGetCurve()
```

### C++/CLI

```cpp
Curve^ IGetCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Underlying [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [SketchSegment::IGetCurve](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~IGetCurve.html).

## Examples

[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)

## Remarks

This operation only supports for [ellipse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchEllipse.html), [line](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchLine.html), [arc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc.html), [spline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline.html), and [parabola](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager.html) sketch items. All other sketch segment types will return NULL, and S_false for COM applications.

NOTE: Support for ellipse, line, and arc segments was introduced in SOLIDWORKS 2004.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetCurve.html)

## Availability

SOLIDWORKS 99, datecode 1999207
