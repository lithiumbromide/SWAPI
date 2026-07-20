---
title: "DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler.html"
---

# DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a display pane is collapsed in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[DisplayPaneCollapseNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~DisplayPaneCollapseNotify_EV.html)

.

## Examples

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

## Remarks

If developing a C++ application, use

[swDrawingDisplayPaneCollapseNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html)

to register for this notification.

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
