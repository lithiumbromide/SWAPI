---
title: "IsRationalCurve Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "IsRationalCurve"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsRationalCurve.html"
---

# IsRationalCurve Property (ISketchSpline)

Gets whether this spline is rational or non-rational.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsRationalCurve As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Boolean

value = instance.IsRationalCurve
```

### C#

```csharp
System.bool IsRationalCurve {get;}
```

### C++/CLI

```cpp
property System.bool IsRationalCurve {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if rational, false if non-rational

## VBA Syntax

See [SketchSpline::IsRationalCurve](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~IsRationalCurve.html).

## Examples

[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::MakeRational Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~MakeRational.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
