---
title: "StopDynamics Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "StopDynamics"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StopDynamics.html"
---

# StopDynamics Method (IModelView)

Ends dynamic model view motion.

## Syntax

### Visual Basic (Declaration)

```vb
Sub StopDynamics()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView

instance.StopDynamics()
```

### C#

```csharp
void StopDynamics()
```

### C++/CLI

```cpp
void StopDynamics();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::StopDynamics](ms-its:sldworksapivb6.chm::/sldworks~ModelView~StopDynamics.html).

## Examples

[Dynamic View Rotation (C++)](Dynamic_View_Rotation_Example_CPlusPlus_COM.htm)

## Remarks

Use this method with [IModelView::StartDynamics](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~StartDynamics.html) at the end of dynamic view motion. This method returns the view to its previous HLR, HLV, or shaded mode and recalculates the display.

After calling this method, you must call [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) or [IModelDoc2::WindowRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~WindowRedraw.html) to update the display for the end-user.

If the SOLIDWORKS file is in view-only mode and is not displaying a shaded image, then you cannot perform any view rotations. Do not call any of the view rotation functions.

To determine if the file is in view-only mode and is not displaying a shaded image, use [IModelDoc2::IsOpenedViewOnly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IsOpenedViewOnly.html) and [IModelView::GetDisplayState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetDisplayState.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::RotateAboutAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutAxis.html)
[IModelView::RotateAboutCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutCenter.html)
[IModelView::RotateAboutPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.html)
[IModelView::DynamicMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DynamicMode.html)
[IModelView::HlrQuality Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HlrQuality.html)
