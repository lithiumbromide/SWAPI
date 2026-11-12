---
title: "GetDisplayMode2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDisplayMode2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.html"
---

# GetDisplayMode2 Method (IView)

Gets the current display mode of the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayMode2() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetDisplayMode2()
```

### C#

```csharp
System.int GetDisplayMode2()
```

### C++/CLI

```cpp
System.int GetDisplayMode2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Current display mode of the drawing view as defined in [swDisplayMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayMode_e.html)

## VBA Syntax

See [View::GetDisplayMode2](ms-its:sldworksapivb6.chm::/sldworks~View~GetDisplayMode2.html).

## Examples

[Set View Display Mode (C++)](Set_View_Display_Mode_Example_CPlusPlus_COM.htm)
[Change Display Mode to Draft Quality (VBA)](Change_Display_Mode_to_Draft_Quality_Example_VB.htm)
[Get Number of Polylines in Shaded Mode Drawing View (VBA)](Get_Number_of_Polylines_in_Shaded_Mode_Drawing_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayEdgesInShadedMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayEdgesInShadedMode.html)
[IView::GetFacettedHlrDisplay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFacettedHlrDisplay.html)
[IView::SetDisplayMode3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.html)
[IView::UpdateViewDisplayGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry.html)
[IView::SetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayTangentEdges2.html)
[IView::GetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayTangentEdges2.html)
[IView::GetUseParentDisplayMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUseParentDisplayMode.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
