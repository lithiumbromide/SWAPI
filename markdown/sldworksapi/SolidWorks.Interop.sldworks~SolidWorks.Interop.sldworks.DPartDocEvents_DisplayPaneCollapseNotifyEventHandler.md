---
title: "DPartDocEvents_DisplayPaneCollapseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_DisplayPaneCollapseNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DisplayPaneCollapseNotifyEventHandler.html"
---

# DPartDocEvents_DisplayPaneCollapseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the Display Pane collapses in this part.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_DisplayPaneCollapseNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_DisplayPaneCollapseNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_DisplayPaneCollapseNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_DisplayPaneCollapseNotifyEventHandler();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[DisplayPaneCollapseNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~DisplayPaneCollapseNotify_EV.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## Remarks

If developing a C++ application, use

[swPartDisplayPaneCollapseNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html)

to register for this notification.

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
