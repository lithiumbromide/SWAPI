---
title: "RotateAboutPoint Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "RotateAboutPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.html"
---

# RotateAboutPoint Method (IModelView)

Rotates the model view about the specified point by the specified angles in the directions of the screen X and Y axes.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RotateAboutPoint( _
   ByVal XAngle As System.Double, _
   ByVal YAngle As System.Double, _
   ByVal Ptx As System.Double, _
   ByVal Pty As System.Double, _
   ByVal Ptz As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim XAngle As System.Double
Dim YAngle As System.Double
Dim Ptx As System.Double
Dim Pty As System.Double
Dim Ptz As System.Double

instance.RotateAboutPoint(XAngle, YAngle, Ptx, Pty, Ptz)
```

### C#

```csharp
void RotateAboutPoint(
   System.double XAngle,
   System.double YAngle,
   System.double Ptx,
   System.double Pty,
   System.double Ptz
)
```

### C++/CLI

```cpp
void RotateAboutPoint(
   System.double XAngle,
   System.double YAngle,
   System.double Ptx,
   System.double Pty,
   System.double Ptz
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XAngle`: Rotation about the screen X axis
- `YAngle`: Rotation about the screen Y axis
- `Ptx`: Center of rotation
- `Pty`: Center of rotation
- `Ptz`: Center of rotation

## VBA Syntax

See [ModelView::RotateAboutPoint](ms-its:sldworksapivb6.chm::/sldworks~ModelView~RotateAboutPoint.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::RotateAboutAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutAxis.html)
[IModelView::RotateAboutCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutCenter.html)
[IModelView::RotateAboutPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.html)
