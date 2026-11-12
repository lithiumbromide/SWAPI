---
title: "GraphicsRedraw2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GraphicsRedraw2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html"
---

# GraphicsRedraw2 Method (IModelDoc2)

Obsolete. Superseded by [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) and [IModelView::IGraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGraphicsRedraw.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GraphicsRedraw2()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.GraphicsRedraw2()
```

### C#

```csharp
void GraphicsRedraw2()
```

### C++/CLI

```cpp
void GraphicsRedraw2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::GraphicsRedraw2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GraphicsRedraw2.html).

## Examples

[Dynamic View Rotation (C++)](Dynamic_View_Rotation_Example_CPlusPlus_COM.htm)
[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)
[Autodimension a Sketch (VBA)](Autodimension_a_Sketch_Example_VB.htm)
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Redraw Graphics (VBA)](Redraw_Graphics_Example_VB.htm)

## Remarks

This method forces the display to be updated immediately when called.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::WindowRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.html)
[IModelView::DrawHighlightedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawHighlightedItems.html)
[IModelView::DrawTransparentFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawTransparentFeatureTree.html)
[IModelView::SuppressWaitCursorDuringRedraw Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SuppressWaitCursorDuringRedraw.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
