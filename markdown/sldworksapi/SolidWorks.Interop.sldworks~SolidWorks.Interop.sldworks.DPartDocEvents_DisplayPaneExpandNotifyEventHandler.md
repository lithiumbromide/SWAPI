---
title: "DPartDocEvents_DisplayPaneExpandNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_DisplayPaneExpandNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DisplayPaneExpandNotifyEventHandler.html"
---

# DPartDocEvents_DisplayPaneExpandNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the Display Pane expands in this part.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_DisplayPaneExpandNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_DisplayPaneExpandNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_DisplayPaneExpandNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_DisplayPaneExpandNotifyEventHandler();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[DisplayPaneExpandNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~DisplayPaneExpandNotify_EV.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## Remarks

If developing a C++ application, use

[swPartDisplayPaneExpandNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html)

to register for this notification.

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
