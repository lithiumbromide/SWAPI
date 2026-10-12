---
title: "DrawTransparentFeatureTree Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "DrawTransparentFeatureTree"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawTransparentFeatureTree.html"
---

# DrawTransparentFeatureTree Method (IModelView)

Draws a transparent FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DrawTransparentFeatureTree()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView

instance.DrawTransparentFeatureTree()
```

### C#

```csharp
void DrawTransparentFeatureTree()
```

### C++/CLI

```cpp
void DrawTransparentFeatureTree();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::DrawTransparentFeatureTree](ms-its:sldworksapivb6.chm::/sldworks~ModelView~DrawTransparentFeatureTree.html).

## Remarks

You can use this method to redraw the flyout FeatureManager design tree after rendering a model.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelDoc2::GraphicsRedraw2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html)
[IModelDoc2::WindowRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
