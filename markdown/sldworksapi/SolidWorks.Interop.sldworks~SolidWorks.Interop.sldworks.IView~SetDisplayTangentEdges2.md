---
title: "SetDisplayTangentEdges2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetDisplayTangentEdges2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayTangentEdges2.html"
---

# SetDisplayTangentEdges2 Method (IView)

Sets the tangent edge display mode of the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDisplayTangentEdges2( _
   ByVal DisplayIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim DisplayIn As System.Integer

instance.SetDisplayTangentEdges2(DisplayIn)
```

### C#

```csharp
void SetDisplayTangentEdges2(
   System.int DisplayIn
)
```

### C++/CLI

```cpp
void SetDisplayTangentEdges2(
   System.int DisplayIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayIn`: Tangent edge display mode as defined in [swDisplayTangentEdges_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayTangentEdges_e.html)

## VBA Syntax

See [View::SetDisplayTangentEdges2](ms-its:sldworksapivb6.chm::/sldworks~View~SetDisplayTangentEdges2.html).

## Remarks

Tangent edges are the transition lines between, for example, a blend and a face.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayTangentEdges2.html)
[IView::GetDisplayEdgesInShadedMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayEdgesInShadedMode.html)
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.html)
[IView::GetUseParentDisplayMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUseParentDisplayMode.html)
[IView::UpdateViewDisplayGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
