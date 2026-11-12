---
title: "GetEyePoint Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetEyePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint.html"
---

# GetEyePoint Method (IModelView)

Gets the eye position for perspective viewing.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEyePoint() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Object

value = instance.GetEyePoint()
```

### C#

```csharp
System.object GetEyePoint()
```

### C++/CLI

```cpp
System.Object^ GetEyePoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 3 doubles describing the eye position in screen space

## VBA Syntax

See [ModelView::GetEyePoint](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetEyePoint.html).

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
[IModelView::IGetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.html)
[IModelView::ISetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint.html)
[IModelView::SetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.html)
[IModelView::GetViewPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.html)
[IModelView::HasPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.html)
[IModelView::RemovePerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RemovePerspective.html)
[IModelView::Scale2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.html)
