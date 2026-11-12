---
title: "GetViewPlaneDistance Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetViewPlaneDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.html"
---

# GetViewPlaneDistance Method (IModelView)

Gets the model view plane distance for perspective viewing.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViewPlaneDistance() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Double

value = instance.GetViewPlaneDistance()
```

### C#

```csharp
System.double GetViewPlaneDistance()
```

### C++/CLI

```cpp
System.double GetViewPlaneDistance();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Distance from the eye point to the view plane

## VBA Syntax

See [ModelView::GetViewPlaneDistance](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetViewPlaneDistance.html).

## Remarks

The value returned is in pixels and represents the distance from the eye point to the view plane (the front of the object). The view plane distance is affected by the view scale.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::AddPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~AddPerspective.html)
[IModelView::GetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint.html)
[IModelView::GetIsoPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetIsoPlaneDistance.html)
[IModelView::HasPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.html)
[IModelView::IGetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.html)
[IModelView::ISetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint.html)
[IModelView::SetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.html)
[IModelView::RemovePerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RemovePerspective.html)
[IModelView::Scale2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.html)
