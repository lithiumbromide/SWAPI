---
title: "DSldWorksEvents_TaskPanePinnedNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_TaskPanePinnedNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_TaskPanePinnedNotifyEventHandler.html"
---

# DSldWorksEvents_TaskPanePinnedNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the Task Pane is pinned.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_TaskPanePinnedNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_TaskPanePinnedNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_TaskPanePinnedNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_TaskPanePinnedNotifyEventHandler();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[TaskPanePinnedNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~TaskPanePinnedNotify_EV.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## Remarks

If developing a C++ application, use[swAppTaskPanePinnedNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html)to register for this notification.

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
