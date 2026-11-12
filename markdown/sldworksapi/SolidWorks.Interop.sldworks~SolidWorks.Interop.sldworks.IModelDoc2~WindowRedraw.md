---
title: "WindowRedraw Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "WindowRedraw"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.html"
---

# WindowRedraw Method (IModelDoc2)

Redraws the current window.

## Syntax

### Visual Basic (Declaration)

```vb
Sub WindowRedraw()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.WindowRedraw()
```

### C#

```csharp
void WindowRedraw()
```

### C++/CLI

```cpp
void WindowRedraw();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::WindowRedraw](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~WindowRedraw.html).

## Examples

[Insert a Note (VBA)](Insert_a_Note_Example_VB.htm)
[Running or Attaching to a SOLIDWORKS Session (VBA)](SOLIDWORKS_Visible_or_BackGround_Example_VB.htm)
[Anchor a Note (C#)](Anchor_a_Note_Example_CSharp.htm)
[Anchor a Note (VB.NET)](Anchor_a_Note_Example_VBNET.htm)
[Anchor a Note (VBA)](Anchor_a_Note_Example_VB.htm)

## Remarks

The current window includes the FeatureManager design tree view and the graphics area or graphics areas if you are using the window splitter.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GraphicsRedraw2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html)
[IModelView::DrawHighlightedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawHighlightedItems.html)
[IModelView::DrawTransparentFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawTransparentFeatureTree.html)
[IModelView::SuppressWaitCursorDuringRedraw Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SuppressWaitCursorDuringRedraw.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
