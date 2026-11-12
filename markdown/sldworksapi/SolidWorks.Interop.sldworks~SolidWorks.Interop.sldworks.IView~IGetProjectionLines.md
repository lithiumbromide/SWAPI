---
title: "IGetProjectionLines Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetProjectionLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionLines.html"
---

# IGetProjectionLines Method (IView)

Gets the projection lines (arrows) in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProjectionLines( _
   ByVal Count As System.Integer _
) As ProjectionArrow
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Count As System.Integer
Dim value As ProjectionArrow

value = instance.IGetProjectionLines(Count)
```

### C#

```csharp
ProjectionArrow IGetProjectionLines(
   System.int Count
)
```

### C++/CLI

```cpp
ProjectionArrow^ IGetProjectionLines(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of projection lines

### Return Value

- in-process, unmanaged C++: Pointer to an array of [projection lines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionArrow.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

This method only works for base drawing views; it does not work for projected or auxiliary views.

Multiple projection lines can exist in a view. This method returns the interface for each projection line so that an application such as DXF/DWG translation can create the projection lines with the base drawing view rather than creating those lines when cycling through the views and finding a projected or auxiliary view.

Before calling this method, call [IView::GetProjectionLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetProjectionLineCount.html) to get the value for Count.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetProjectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLines.html)
[IView::GetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionArrow.html)
[IView::GetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBaseView.html)
[IView::IGetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBaseView.html)
[IView::IGetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionArrow.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
