---
title: "AddCurvatureControl Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "AddCurvatureControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddCurvatureControl.html"
---

# AddCurvatureControl Method (ISketchSpline)

Adds a curvature control pointer to this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCurvatureControl( _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ZPos As System.Double _
) As SplineHandle
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double
Dim value As SplineHandle

value = instance.AddCurvatureControl(XPos, YPos, ZPos)
```

### C#

```csharp
SplineHandle AddCurvatureControl(
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

### C++/CLI

```cpp
SplineHandle^ AddCurvatureControl(
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XPos`: x coordinate for the pointer
- `YPos`: y coordinate for the pointer
- `ZPos`: z coordinate for the pointer

### Return Value

[Spline handle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle.html)

## VBA Syntax

See [SketchSpline::AddCurvatureControl](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~AddCurvatureControl.html).

## Examples

[Set Spline Tangency and Curvature Controls (VBA)](Set_Spline_Tangency_and_Curvature_Controls_Example_VB.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::AddTangencyControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddTangencyControl.html)
[ISketchSpline::GetSplineHandleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.html)
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.html)
[ISketchSpline::IGetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.html)
[ISketchSpline::ResetAllHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.html)
[ISketchSpline::ShowCurvatureCombs Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowCurvatureCombs.html)
[ISketchSpline::ShowSplineHandles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.html)
[ISplineHandle::Curvature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Curvature.html)
[ISplineHandle::CurvatureControlled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~CurvatureControlled.html)
[ISplineHandle::RadiusOfCurvature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~RadiusOfCurvature.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
