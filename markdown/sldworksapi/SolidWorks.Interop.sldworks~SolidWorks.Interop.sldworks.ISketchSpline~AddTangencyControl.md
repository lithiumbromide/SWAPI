---
title: "AddTangencyControl Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "AddTangencyControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddTangencyControl.html"
---

# AddTangencyControl Method (ISketchSpline)

Adds a new handle to help control the tangency of this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddTangencyControl( _
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

value = instance.AddTangencyControl(XPos, YPos, ZPos)
```

### C#

```csharp
SplineHandle AddTangencyControl(
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

### C++/CLI

```cpp
SplineHandle^ AddTangencyControl(
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XPos`: x coordinate of the new handle
- `YPos`: y coordinate of the new handle
- `ZPos`: z coordinate of the new handle

### Return Value

[Spline handle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle.html)

## VBA Syntax

See [SketchSpline::AddTangencyControl](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~AddTangencyControl.html).

## Examples

[Set Spline Tangency and Curvature Controls (VBA)](Set_Spline_Tangency_and_Curvature_Controls_Example_VB.htm)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::AddCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~AddCurvatureControl.html)
[ISketchSpline::GetSplineHandleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.html)
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.html)
[ISketchSpline::IGetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.html)
[ISketchSpline::ResetAllHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.html)
[ISketchSpline::ShowSplineHandles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.html)
[ISplineHandle::TangentDriving Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentDriving.html)
[ISplineHandle::TangentMagnitude Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentMagnitude.html)
[ISplineHandle::TangentPolarDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentPolarDirection.html)
[ISplineHandle::TangentRadialDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~TangentRadialDirection.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
