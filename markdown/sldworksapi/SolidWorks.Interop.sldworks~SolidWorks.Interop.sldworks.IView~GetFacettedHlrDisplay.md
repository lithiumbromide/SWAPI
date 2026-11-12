---
title: "GetFacettedHlrDisplay Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFacettedHlrDisplay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFacettedHlrDisplay.html"
---

# GetFacettedHlrDisplay Method (IView)

Gets whether HLR/HLV (Hidden Lines Removed/Hidden Lines Visible) edges should be displayed faceted in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacettedHlrDisplay() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.GetFacettedHlrDisplay()
```

### C#

```csharp
System.bool GetFacettedHlrDisplay()
```

### C++/CLI

```cpp
System.bool GetFacettedHlrDisplay();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the edges should be displayed faceted, false if not

## VBA Syntax

See [View::GetFacettedHlrDisplay](ms-its:sldworksapivb6.chm::/sldworks~View~GetFacettedHlrDisplay.html).

## Examples

[Get Whether HLR/HLV Edges are Displayed Faceted (VBA)](Get_Whether_HLR_HLV_Edges_Are_Displayed_Faceted_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayEdgesInShadedMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayEdgesInShadedMode.html)
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.html)
[IView::GetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayTangentEdges2.html)
[IView::SetDisplayMode3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.html)
[IView::SetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayTangentEdges2.html)
[IView::UpdateViewDisplayGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
