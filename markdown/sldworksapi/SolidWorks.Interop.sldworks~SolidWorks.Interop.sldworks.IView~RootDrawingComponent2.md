---
title: "RootDrawingComponent2 Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "RootDrawingComponent2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RootDrawingComponent2.html"
---

# RootDrawingComponent2 Property (IView)

Gets the root component of this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RootDrawingComponent2( _
   ByVal InChildContext As System.Boolean _
) As DrawingComponent
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim InChildContext As System.Boolean
Dim value As DrawingComponent

value = instance.RootDrawingComponent2(InChildContext)
```

### C#

```csharp
DrawingComponent RootDrawingComponent2(
   System.bool InChildContext
) {get;}
```

### C++/CLI

```cpp
property DrawingComponent^ RootDrawingComponent2 {
   DrawingComponent^ get(System.bool InChildContext);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InChildContext`: True to return the temporary root component of this section view, false to return the root drawing component of this view's parent view (see **Remarks**)

### Property Value

[Drawing component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent.html)

## VBA Syntax

See [View::RootDrawingComponent2](ms-its:sldworksapivb6.chm::/sldworks~View~RootDrawingComponent2.html).

## Remarks

For all drawing views except section views, this property returns the root drawing component of the drawing view's parent view. For section views only, this property returns the root drawing component of the temporary assembly that is created specifically for the section view. To access the real root drawing component of the section view, first call [IView::GetBaseView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBaseView.html) to get the section view's base view. Then use this property to get the root drawing drawing component.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2026 SP02, Revision Number 34.2
