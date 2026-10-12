---
title: "GetProjectionLineCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetProjectionLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLineCount.html"
---

# GetProjectionLineCount Method (IView)

Gets the number of projection lines (arrows) in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProjectionLineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetProjectionLineCount()
```

### C#

```csharp
System.int GetProjectionLineCount()
```

### C++/CLI

```cpp
System.int GetProjectionLineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of projection lines in this drawing view

## VBA Syntax

See [View::GetProjectionLineCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetProjectionLineCount.html).

## Remarks

This method only works for base drawing views; it does not work for projected or auxiliary views.

Call this method before [IView::IGetProjectionLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetProjectionLines.html) to get the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetProjectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionLines.html)
[IView::GetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetProjectionArrow.html)
[IView::IGetProjectionArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetProjectionArrow.html)
[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
