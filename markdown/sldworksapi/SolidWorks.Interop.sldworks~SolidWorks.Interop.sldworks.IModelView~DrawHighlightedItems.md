---
title: "DrawHighlightedItems Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "DrawHighlightedItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawHighlightedItems.html"
---

# DrawHighlightedItems Method (IModelView)

Draws or redraws the highlighted items.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DrawHighlightedItems()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView

instance.DrawHighlightedItems()
```

### C#

```csharp
void DrawHighlightedItems()
```

### C++/CLI

```cpp
void DrawHighlightedItems();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::DrawHighlightedItems](ms-its:sldworksapivb6.chm::/sldworks~ModelView~DrawHighlightedItems.html).

## Remarks

This method is useful in applications that handle repainting if you want highlighting
to be visible. When called, the currently highlighted items are painted.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
