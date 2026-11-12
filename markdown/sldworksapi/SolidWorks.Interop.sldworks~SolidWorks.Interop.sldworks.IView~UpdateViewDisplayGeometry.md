---
title: "UpdateViewDisplayGeometry Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "UpdateViewDisplayGeometry"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry.html"
---

# UpdateViewDisplayGeometry Method (IView)

Updates the displayed geometry for a drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UpdateViewDisplayGeometry()
```

### Visual Basic (Usage)

```vb
Dim instance As IView

instance.UpdateViewDisplayGeometry()
```

### C#

```csharp
void UpdateViewDisplayGeometry()
```

### C++/CLI

```cpp
void UpdateViewDisplayGeometry();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [View::UpdateViewDisplayGeometry](ms-its:sldworksapivb6.chm::/sldworks~View~UpdateViewDisplayGeometry.html).

## Remarks

This method accesses new view geometry before Microsoft has repainted the window. For example, this can occur if you were changing the display mode of the drawing view from HLR to HLV and wanted immediate access to the polylines in that drawing view.

Because Microsoft controls repainting the window, you do not have access to your drawing view changes until control is returned. However, using this method immediately updates the view geometry for your purposes.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.html)
[IView::SetDisplayMode3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.html)
