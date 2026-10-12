---
title: "ISetEyePoint Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "ISetEyePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint.html"
---

# ISetEyePoint Method (IModelView)

Sets the eye position for perspective viewing.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetEyePoint( _
   ByRef Eyept As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim Eyept As System.Double
Dim value As System.Boolean

value = instance.ISetEyePoint(Eyept)
```

### C#

```csharp
System.bool ISetEyePoint(
   ref System.double Eyept
)
```

### C++/CLI

```cpp
System.bool ISetEyePoint(
   System.double% Eyept
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Eyept`: Array of 3 doubles describing the eye position in screen space

### Return Value

True if the eye point is set successfully, false if not

## VBA Syntax

See [ModelView::ISetEyePoint](ms-its:sldworksapivb6.chm::/sldworks~ModelView~ISetEyePoint.html).

## Remarks

The values are returned in pixels and are the location of the eye point relative to the screen-space origin (upper-left corner of window). The Z value, in pixels, reflects the distance from the eye point to the object center. These values will be affected by the view scale.

To use these values, you should apply them after you have obtained the current view orientation matrix using [IModelView::Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Transform.html).

The Z value typically are close to

[( [IModelView::GetViewPlaneDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetViewPlaneDistance.html) / ("Object Sizes Away")) * ("Object Sizes Away" + 0.5) ]

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::AddPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~AddPerspective.html)
[IModelView::GetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint.html)
[IModelView::GetIsoPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetIsoPlaneDistance.html)
[IModelView::GetViewPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.html)
[IModelView::HasPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.html)
[IModelView::IGetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.html)
[IModelView::SetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.html)
[IModelView::RemovePerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RemovePerspective.html)
[IModelView::Scale2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.html)
