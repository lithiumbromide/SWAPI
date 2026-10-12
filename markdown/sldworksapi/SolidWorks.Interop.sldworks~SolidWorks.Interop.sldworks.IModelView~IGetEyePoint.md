---
title: "IGetEyePoint Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "IGetEyePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.html"
---

# IGetEyePoint Method (IModelView)

Gets the eye position for perspective viewing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetEyePoint( _
   ByRef Eyept As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim Eyept As System.Double

instance.IGetEyePoint(Eyept)
```

### C#

```csharp
void IGetEyePoint(
   ref System.double Eyept
)
```

### C++/CLI

```cpp
void IGetEyePoint(
   System.double% Eyept
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Eyept`: Array of 3 doubles describing the eye position in screen space

## VBA Syntax

See [ModelView::IGetEyePoint](ms-its:sldworksapivb6.chm::/sldworks~ModelView~IGetEyePoint.html).

## Remarks

The values are returned in pixels and are the location of the eyepoint relative to the screen space origin (upper-left corner of window). The Z value reflects the distance from the eye point to the object center. These values are affected by the view scale.

To use these values, you should apply them after you have obtained the current view orientation matrix using ModelView::Xform.

The Z value (in pixels) will typically be close to

[( [IModelView::GetViewPlaneDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetViewPlaneDistance.html) / ("Object Sizes Away")) * ("Object Sizes Away" + 0.5) ]

The perspective view is created based on the value entered by the end-user for Object Sizes Away. If the user specifies 3 objects away, then the eye point is positioned 3 body diameters from the view plane, where the view plane is located at the front of the body as seen from this particular orientation.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::AddPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~AddPerspective.html)
[IModelView::GetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint.html)
[IModelView::GetIsoPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetIsoPlaneDistance.html)
[IModelView::GetViewPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.html)
[IModelView::HasPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.html)
[IModelView::ISetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint.html)
[IModelView::SetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.html)
[IModelView::RemovePerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RemovePerspective.html)
[IModelView::Scale2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.html)
