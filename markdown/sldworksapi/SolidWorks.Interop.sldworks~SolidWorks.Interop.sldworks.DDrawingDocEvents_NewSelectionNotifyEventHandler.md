---
title: "DDrawingDocEvents_NewSelectionNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_NewSelectionNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_NewSelectionNotifyEventHandler.html"
---

# DDrawingDocEvents_NewSelectionNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the selection list has changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_NewSelectionNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_NewSelectionNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_NewSelectionNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_NewSelectionNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [NewSelectionNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~NewSelectionNotify_EV.html).

## Remarks

This notification is generated when items are added, removed, or reordered in the selection list.

If developing a C++ application, use [swDrawingNewSelectionNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
