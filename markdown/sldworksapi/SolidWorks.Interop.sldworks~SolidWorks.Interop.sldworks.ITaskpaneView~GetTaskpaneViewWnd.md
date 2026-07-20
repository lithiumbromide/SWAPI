---
title: "GetTaskpaneViewWnd Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "GetTaskpaneViewWnd"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetTaskpaneViewWnd.html"
---

# GetTaskpaneViewWnd Method (ITaskpaneView)

Obsolete. Superseded by

[ITaskpaneView::GetTaskpaneViewWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetTaskpaneViewWndx64.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTaskpaneViewWnd() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim value As System.Integer

value = instance.GetTaskpaneViewWnd()
```

### C#

```csharp
System.int GetTaskpaneViewWnd()
```

### C++/CLI

```cpp
System.int GetTaskpaneViewWnd();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

CWnd object pointer

EndOLEArgumentsRow

## VBA Syntax

See

[TaskpaneView::GetTaskpaneViewWnd](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~GetTaskpaneViewWnd.html)

.

## Remarks

This method gets a Task Pane view window object pointer for 32-bit MFC applications only.

Because this method is valid only for 32-bit applications, it is now obsolete.

To insert a Task Pane view window, create your Task Pane view window and pass its handle to SOLIDWORKS using[ITaskpaneView::DisplayWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandlex64.html).

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)

[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
