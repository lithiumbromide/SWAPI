---
title: "GetTaskpaneViewWndx64 Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "GetTaskpaneViewWndx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetTaskpaneViewWndx64.html"
---

# GetTaskpaneViewWndx64 Method (ITaskpaneView)

Gets the Taskpane view window handle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTaskpaneViewWndx64() As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim value As System.Long

value = instance.GetTaskpaneViewWndx64()
```

### C#

```csharp
System.long GetTaskpaneViewWndx64()
```

### C++/CLI

```cpp
System.int64 GetTaskpaneViewWndx64();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Window handle

## VBA Syntax

See

[TaskpaneView::GetTaskpaneViewWndx64](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~GetTaskpaneViewWndx64.html)

.

## Remarks

To insert a Task Pane view window, create your Task Pane view window and pass its handle to SOLIDWORKS using[ITaskpaneView::DisplayWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandlex64.html).

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)

[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
