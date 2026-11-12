---
title: "RotateAboutAxis Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "RotateAboutAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutAxis.html"
---

# RotateAboutAxis Method (IModelView)

Rotates the model view about a point, by an angle in the specified direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RotateAboutAxis( _
   ByVal Angle As System.Double, _
   ByVal Ptx As System.Double, _
   ByVal Pty As System.Double, _
   ByVal Ptz As System.Double, _
   ByVal AxisVecX As System.Double, _
   ByVal AxisVecY As System.Double, _
   ByVal AxisVecZ As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim Angle As System.Double
Dim Ptx As System.Double
Dim Pty As System.Double
Dim Ptz As System.Double
Dim AxisVecX As System.Double
Dim AxisVecY As System.Double
Dim AxisVecZ As System.Double

instance.RotateAboutAxis(Angle, Ptx, Pty, Ptz, AxisVecX, AxisVecY, AxisVecZ)
```

### C#

```csharp
void RotateAboutAxis(
   System.double Angle,
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.double AxisVecX,
   System.double AxisVecY,
   System.double AxisVecZ
)
```

### C++/CLI

```cpp
void RotateAboutAxis(
   System.double Angle,
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.double AxisVecX,
   System.double AxisVecY,
   System.double AxisVecZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle of rotation
- `Ptx`: Center of rotation
- `Pty`: Center of rotation
- `Ptz`: Center of rotation
- `AxisVecX`: Direction of axis of rotation
- `AxisVecY`: Direction of axis of rotation
- `AxisVecZ`: Direction of axis of rotation

## VBA Syntax

See [ModelView::RotateAboutAxis](ms-its:sldworksapivb6.chm::/sldworks~ModelView~RotateAboutAxis.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::RotateAboutCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutCenter.html)
[IModelView::RotateAboutPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.html)
[IModelView::StartDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.html)
