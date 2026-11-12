---
title: "HasPerspective Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "HasPerspective"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.html"
---

# HasPerspective Method (IModelView)

Determines if the model view currently has perspective.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasPerspective() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Boolean

value = instance.HasPerspective()
```

### C#

```csharp
System.bool HasPerspective()
```

### C++/CLI

```cpp
System.bool HasPerspective();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the view currently has perspective viewing turned on, false otherwise

## VBA Syntax

See [ModelView::HasPerspective](ms-its:sldworksapivb6.chm::/sldworks~ModelView~HasPerspective.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::AddPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~AddPerspective.html)
[IModelView::GetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint.html)
[IModelView::GetIsoPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetIsoPlaneDistance.html)
[IModelView::GetViewPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.html)
[IModelView::IGetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.html)
[IModelView::ISetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint.html)
[IModelView::SetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.html)
[IModelView::RemovePerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RemovePerspective.html)
