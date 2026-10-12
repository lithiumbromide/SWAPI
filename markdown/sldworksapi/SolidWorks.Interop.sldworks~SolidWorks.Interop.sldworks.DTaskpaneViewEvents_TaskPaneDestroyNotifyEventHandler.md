---
title: "DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler.html"
---

# DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when an application-level Task Pane view is about to be destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DTaskpaneViewEvents_TaskPaneDestroyNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [TaskPaneDestroyNotify Event (TaskpaneView)](ms-its:sldworksapivb6.chm::/SldWorks~TaskpaneView~TaskPaneDestroyNotify_EV.html).

## Examples

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swAppTaskPaneDestroyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
