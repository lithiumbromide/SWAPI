---
title: "IGetProjectionArrow Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetProjectionArrow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionArrow.html"
---

# IGetProjectionArrow Method (IView)

Gets the projection arrow for this projected view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProjectionArrow() As ProjectionArrow
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As ProjectionArrow

value = instance.IGetProjectionArrow()
```

### C#

```csharp
ProjectionArrow IGetProjectionArrow()
```

### C++/CLI

```cpp
ProjectionArrow^ IGetProjectionArrow();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Projection arrow](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionArrow.html)

## VBA Syntax

See [View::IGetProjectionArrow](ms-its:sldworksapivb6.chm::/sldworks~View~IGetProjectionArrow.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[GetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionArrow.html)
[IView::GetProjectionLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLineCount.html)
[IView::GetProjectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLines.html)
[IView::IGetProjectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionLines.html)
[IProjectionArrow::IGetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetProjectedView.html)
[IProjectionArrow::GetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetProjectedView.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
