---
title: "GetProjectionLines Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetProjectionLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLines.html"
---

# GetProjectionLines Method (IView)

Gets the projection lines (arrows) in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProjectionLines() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetProjectionLines()
```

### C#

```csharp
System.object GetProjectionLines()
```

### C++/CLI

```cpp
System.Object^ GetProjectionLines();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [projection lines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionArrow.html)

## VBA Syntax

See [View::GetProjectionLines](ms-its:sldworksapivb6.chm::/sldworks~View~GetProjectionLines.html).

## Remarks

This method only works for base drawing views; it does not work for projected or auxiliary views.

Multiple projection lines can exist in a view. This method returns the interface for each projection line so that an application such as DXF/DWG translation can create the projection lines with the base drawing view rather than creating those lines when cycling through the views and finding a projected or auxiliary view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetProjectionLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLineCount.html)
[IView::IGetProjectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionLines.html)
[IView::IGetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionArrow.html)
[IView::GetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionArrow.html)
[IView::GetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBaseView.html)
[IView::IGetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBaseView.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
