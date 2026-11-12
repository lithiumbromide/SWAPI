---
title: "GraphicsRedraw Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GraphicsRedraw"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.html"
---

# GraphicsRedraw Method (IModelView)

Redraws the specified region of or the entire SOLIDWORKS graphics window.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GraphicsRedraw( _
   ByVal Rect As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim Rect As System.Object

instance.GraphicsRedraw(Rect)
```

### C#

```csharp
void GraphicsRedraw(
   System.object Rect
)
```

### C++/CLI

```cpp
void GraphicsRedraw(
   System.Object^ Rect
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Rect`: Array of four integers or longs indicating the boundary of the region in the SOLIDWORKS graphics window to redraw; if the array is empty, then the entire graphics window is redrawn

## VBA Syntax

See [ModelView::GraphicsRedraw](ms-its:sldworksapivb6.chm::/Sldworks~ModelView~GraphicsRedraw.html).

## Examples

[Exclude Faces Before Flattening (C#)](Exclude_Faces_Before_Flattening_Example_CSharp.htm)
[Exclude Faces Before Flattening (VB.NET)](Exclude_Faces_Before_Flattening_Example_VBNET.htm)
[Exclude Faces Before Flattening (VBA)](Exclude_Faces_Before_Flattening_Example_VB.htm)

## Remarks

This method forces the specified region or the entire SOLIDWORKS graphics window to be updated immediately when called.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelDoc2::WindowRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.html)
[IModelView::DrawHighlightedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawHighlightedItems.html)
[IModelView::DrawTransparentFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawTransparentFeatureTree.html)
[IModelView::SuppressWaitCursorDuringRedraw Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SuppressWaitCursorDuringRedraw.html)
[IModelView::IGraphicsRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
