---
title: "DPartDocEvents_UndoPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_UndoPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UndoPreNotifyEventHandler.html"
---

# DPartDocEvents_UndoPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before an Undo operation occurs in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_UndoPreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_UndoPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_UndoPreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_UndoPreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [UndoPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~UndoPreNotify_EV.html).

## Examples

[Fire Undo and Redo Pre- and Post-notifications in Part Document (C#)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Part_Document_Example_CSharp.htm)
[Fire Undo and Redo Pre- and Post-notifications in Part Document (VB.NET)](Fire_Undo_and_Redo_Pre_and_Post-notifications_in_Part_Document_Example_VBNET.htm)
[Fire Undo and Redo Pre- and Post-notifications in Part Document (VBA)](Fire_Undo_and_Redo_Pre_and_Post-notifications_in_Part_Document_Example_VB6.htm)

## Remarks

If developing a C++ application, use [swPartUndoPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
