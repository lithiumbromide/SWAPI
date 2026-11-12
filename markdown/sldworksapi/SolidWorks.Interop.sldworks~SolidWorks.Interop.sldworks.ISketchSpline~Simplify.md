---
title: "Simplify Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "Simplify"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~Simplify.html"
---

# Simplify Method (ISketchSpline)

Reduces the number of points in a spline to increase system performance in models with complex spline curves.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Simplify( _
   ByVal ToleranceIn As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim ToleranceIn As System.Double

instance.Simplify(ToleranceIn)
```

### C#

```csharp
void Simplify(
   System.double ToleranceIn
)
```

### C++/CLI

```cpp
void Simplify(
   System.double ToleranceIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToleranceIn`: Smoothing factor, in meters, to use to simplify sketch

## VBA Syntax

See [SketchSpline::Simplify](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~Simplify.html).

## Examples

[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)

## Remarks

The sketch must be in edit mode and a spline must be preselected.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
