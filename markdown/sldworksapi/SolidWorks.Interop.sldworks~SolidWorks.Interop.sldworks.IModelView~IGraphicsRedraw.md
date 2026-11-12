---
title: "IGraphicsRedraw Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "IGraphicsRedraw"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.html"
---

# IGraphicsRedraw Method (IModelView)

Redraws the specified region of or the entire SOLIDWORKS graphics window.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGraphicsRedraw( _
   ByRef Rect As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim Rect As System.Integer

instance.IGraphicsRedraw(Rect)
```

### C#

```csharp
void IGraphicsRedraw(
   ref System.int Rect
)
```

### C++/CLI

```cpp
void IGraphicsRedraw(
   System.int% Rect
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Rect`: Array of four integers or longs indicating the boundary of the region in the SOLIDWORKS graphics window to redraw; if the array is empty, then the entire graphics window is redrawn

## VBA Syntax

See [ModelView::IGraphicsRedraw](ms-its:sldworksapivb6.chm::/sldworks~ModelView~IGraphicsRedraw.html).

## Remarks

This method forces the specified region or the entire SOLIDWORKS graphics window to be updated immediately when called.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelDoc2::WindowRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.html)
[IModelView::DrawHighlightedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawHighlightedItems.html)
[IModelView::DrawTransparentFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawTransparentFeatureTree.html)
[IModelView::GraphicsRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.html)
[IModelView::SuppressWaitCursorDuringRedraw Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SuppressWaitCursorDuringRedraw.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
