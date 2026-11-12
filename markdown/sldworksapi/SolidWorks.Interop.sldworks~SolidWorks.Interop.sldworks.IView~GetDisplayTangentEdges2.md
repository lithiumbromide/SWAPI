---
title: "GetDisplayTangentEdges2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDisplayTangentEdges2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayTangentEdges2.html"
---

# GetDisplayTangentEdges2 Method (IView)

Gets the current tangent edge display mode of the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayTangentEdges2() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetDisplayTangentEdges2()
```

### C#

```csharp
System.int GetDisplayTangentEdges2()
```

### C++/CLI

```cpp
System.int GetDisplayTangentEdges2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Tangent edge display mode as defined in [swDisplayTangentEdges_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayTangentEdges_e.html)

## VBA Syntax

See [View::GetDisplayTangentEdges2](ms-its:sldworksapivb6.chm::/sldworks~View~GetDisplayTangentEdges2.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayEdgesInShadedMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayEdgesInShadedMode.html)
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.html)
[IView::GetFacettedHlrDisplay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFacettedHlrDisplay.html)
[IView::GetUseParentDisplayMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUseParentDisplayMode.html)
[IView::SetDisplayMode3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.html)
[IView::UpdateViewDisplayGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
