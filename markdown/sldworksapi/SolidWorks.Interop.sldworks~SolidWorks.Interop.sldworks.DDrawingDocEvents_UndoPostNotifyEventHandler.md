---
title: "DDrawingDocEvents_UndoPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_UndoPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UndoPostNotifyEventHandler.html"
---

# DDrawingDocEvents_UndoPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after an Undo action occurs in a drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_UndoPostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_UndoPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_UndoPostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_UndoPostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [UndoPostNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~UndoPostNotify_EV.html).

## Examples

[Undo Deleted Note and Fire Undo Pre- and Post-notify Events (VBA)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)
[Undo Deleted Note and Fire Undo Pre- and Post-notify Events (VB.NET)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)
[Undo Deleted Note and Fire Undo Pre- and Post-notify Events (C#)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swDrawingUndoPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
