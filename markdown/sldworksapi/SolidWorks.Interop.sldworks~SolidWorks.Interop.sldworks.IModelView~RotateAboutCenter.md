---
title: "RotateAboutCenter Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "RotateAboutCenter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutCenter.html"
---

# RotateAboutCenter Method (IModelView)

Rotates the model view about the screen X and Y axes.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RotateAboutCenter( _
   ByVal XAngle As System.Double, _
   ByVal YAngle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim XAngle As System.Double
Dim YAngle As System.Double

instance.RotateAboutCenter(XAngle, YAngle)
```

### C#

```csharp
void RotateAboutCenter(
   System.double XAngle,
   System.double YAngle
)
```

### C++/CLI

```cpp
void RotateAboutCenter(
   System.double XAngle,
   System.double YAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XAngle`: Rotation about the X axis
- `YAngle`: Rotation about the Y axis

## VBA Syntax

See [ModelView::RotateAboutCenter](ms-its:sldworksapivb6.chm::/sldworks~ModelView~RotateAboutCenter.html).

## Examples

[Change Wrap Feature Face (C#)](Change_Wrap_Feature_Face_Example_CSharp.htm)
[Change Wrap Feature Face (VB.NET)](Change_Wrap_Feature_Face_Example_VBNET.htm)
[Change Wrap Feature Face (VBA)](Change_Wrap_Feature_Face_Example_VB.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::RotateAboutAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutAxis.html)
[IModelView::RotateAboutPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.html)
[IModelView::StartDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.html)
