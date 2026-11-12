---
title: "DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler.html"
---

# DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when an application-level Task Pane view is deactivated.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [TaskPaneDeactivateNotify Event (TaskpaneView)](ms-its:sldworksapivb6.chm::/SldWorks~TaskpaneView~TaskPaneDeactivateNotify_EV.html).

## Remarks

If developing a C++ application, use [swAppTaskPaneDeactivateNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
