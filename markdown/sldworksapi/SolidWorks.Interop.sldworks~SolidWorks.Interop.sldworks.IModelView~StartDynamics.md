---
title: "StartDynamics Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "StartDynamics"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.html"
---

# StartDynamics Method (IModelView)

Provides faster rotation of model views.

## Syntax

### Visual Basic (Declaration)

```vb
Sub StartDynamics()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView

instance.StartDynamics()
```

### C#

```csharp
void StartDynamics()
```

### C++/CLI

```cpp
void StartDynamics();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::StartDynamics](ms-its:sldworksapivb6.chm::/sldworks~ModelView~StartDynamics.html).

## Examples

[Dynamic View Rotation (C++)](Dynamic_View_Rotation_Example_CPlusPlus_COM.htm)

## Remarks

After setting swUserPreferenceIntegerValue_e.swLevelOfDetail high enough, this method can be used at the beginning of dynamic model view changes to:

- change HLR or HLV mode to wireframe mode, which provides you with faster view rotation because the edges are not calculated during your view re-orientation.
- turn curved-surface bodies into polyhedra for faster view manipulations when in shaded mode.

Dynamic view motion remains in effect until you call [IModelView::StopDynamics](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~StopDynamics.html).

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
