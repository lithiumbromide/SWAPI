---
title: "DSldWorksEvents_TaskPaneUnpinnedNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_TaskPaneUnpinnedNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_TaskPaneUnpinnedNotifyEventHandler.html"
---

# DSldWorksEvents_TaskPaneUnpinnedNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the Task Pane is unpinned.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_TaskPaneUnpinnedNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_TaskPaneUnpinnedNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_TaskPaneUnpinnedNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_TaskPaneUnpinnedNotifyEventHandler();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[TaskPaneUnpinnedNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~TaskPaneUnpinnedNotify_EV.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## Remarks

If developing a C++ application, use[swAppTaskPaneUnpinnedNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html)to register for this notification.

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
