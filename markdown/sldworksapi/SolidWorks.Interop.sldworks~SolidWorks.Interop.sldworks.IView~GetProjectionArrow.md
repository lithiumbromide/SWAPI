---
title: "GetProjectionArrow Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetProjectionArrow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionArrow.html"
---

# GetProjectionArrow Method (IView)

Gets the projection arrow for this projected view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProjectionArrow() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetProjectionArrow()
```

### C#

```csharp
System.object GetProjectionArrow()
```

### C++/CLI

```cpp
System.Object^ GetProjectionArrow();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Projection arrow](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionArrow.html)

## VBA Syntax

See [View::GetProjectionArrow](ms-its:sldworksapivb6.chm::/sldworks~View~GetProjectionArrow.html).

## Examples

[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionArrow.html)
[IView::GetProjectionLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLineCount.html)
[IView::GetProjectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLines.html)
[IProjectionArrow::GetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetProjectedView.html)
[IProjectionArrow::IGetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetProjectedView.html)
[IView::IGetProjectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionLines.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
