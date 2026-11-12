---
title: "Transform Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "Transform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Transform.html"
---

# Transform Property (IModelView)

Gets the model space to the model view plane transform.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Transform As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As MathTransform

instance.Transform = value

value = instance.Transform
```

### C#

```csharp
MathTransform Transform {get; set;}
```

### C++/CLI

```cpp
property MathTransform^ Transform {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[View plane transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [ModelView::Transform](ms-its:sldworksapivb6.chm::/sldworks~ModelView~Transform.html).

## Remarks

This method is typically used when you are grabbing the view handle using [IModelView::GetViewHWnd](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetViewHWnd.html) or [IModelView::GetViewHWndx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetViewHWndx64.html) and drawing to the view. For example, if you had a point located at 2,2,2 in model space coordinates, then you could multiply it by this return value to determine where to draw in screen space coordinates. The result will be pixel values for the current view.

The screen space coordinate system has its origin in the upper-left corner of the current view with the X vector pointing to the right and the Y vector pointing down.

If the SOLIDWORKS file is in view-only mode and is not displaying a shaded image, then you cannot perform any view rotations. In this situation, you should not call any of the view rotation APIs.

To determine if the file is in view-only mode and whether it is shaded or not, see [IModelDoc2::IsOpenedViewOnly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IsOpenedViewOnly.html) and [IModelView::GetDisplayState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetDisplayState.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
