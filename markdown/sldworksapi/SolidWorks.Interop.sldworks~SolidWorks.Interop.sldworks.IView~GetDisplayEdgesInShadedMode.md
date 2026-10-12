---
title: "GetDisplayEdgesInShadedMode Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDisplayEdgesInShadedMode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayEdgesInShadedMode.html"
---

# GetDisplayEdgesInShadedMode Method (IView)

Gets whether to display the edges in this when the drawing view is in shaded mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayEdgesInShadedMode() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.GetDisplayEdgesInShadedMode()
```

### C#

```csharp
System.bool GetDisplayEdgesInShadedMode()
```

### C++/CLI

```cpp
System.bool GetDisplayEdgesInShadedMode();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the edges are displayed when the view is in shaded mode, false if not

## VBA Syntax

See [View::GetDisplayEdgesInShadedMode](ms-its:sldworksapivb6.chm::/sldworks~View~GetDisplayEdgesInShadedMode.html).

## Remarks

| To... | Then use... |
| --- | --- |
| Determine whether this view is displayed with faceted or precise geometry | IView::GetFacettedHlrDisplay |
| Determine the display mode of a drawing view | IView::GetDisplayMode2 |
| Set the display mode of a drawing view | IView::SetDisplayMode3 |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayTangentEdges2.html)
[IView::GetUseParentDisplayMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUseParentDisplayMode.html)
[IView::SetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayTangentEdges2.html)
[IView::UpdateViewDisplayGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry.html)
