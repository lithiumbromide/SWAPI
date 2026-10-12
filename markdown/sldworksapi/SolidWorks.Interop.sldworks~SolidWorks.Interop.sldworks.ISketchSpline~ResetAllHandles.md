---
title: "ResetAllHandles Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "ResetAllHandles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.html"
---

# ResetAllHandles Method (ISketchSpline)

Resets all [handles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle.html) to their initial state.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ResetAllHandles()
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline

instance.ResetAllHandles()
```

### C#

```csharp
void ResetAllHandles()
```

### C++/CLI

```cpp
void ResetAllHandles();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Use [SplineHandle::Reset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle~Reset.html) to reset one handle to its initial state.

## VBA Syntax

See [SketchSpline::ResetAllHandles](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~ResetAllHandles.html).

## Examples

[Set Spline Tangency and Curvature Controls (VBA)](Set_Spline_Tangency_and_Curvature_Controls_Example_VB.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::GetSplineHandleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.html)
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.html)
[ISketchSpline::IGetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.html)
[ISketchSpline::ShowSplineHandles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
