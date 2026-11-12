---
title: "DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler.html"
---

# DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when an application-level Task Pane view is activated.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [TaskPaneActivateNotify Event (TaskpaneView)](ms-its:sldworksapivb6.chm::/SldWorks~TaskpaneView~TaskPaneActivateNotify_EV.html).

## Examples

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swAppTaskPaneActivateNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
