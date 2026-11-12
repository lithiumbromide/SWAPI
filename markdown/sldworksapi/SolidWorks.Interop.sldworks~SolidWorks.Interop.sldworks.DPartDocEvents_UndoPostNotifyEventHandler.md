---
title: "DPartDocEvents_UndoPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_UndoPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UndoPostNotifyEventHandler.html"
---

# DPartDocEvents_UndoPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after an Undo action occurs in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_UndoPostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_UndoPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_UndoPostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_UndoPostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [UndoPostNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~UndoPostNotify_EV.html).

## Examples

[Undo Feature and Fire Undo Post-Notify Event (VBA)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)
[Undo Feature and Fire Undo Post-Notify Event (VB.NET)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)
[Undo Feature and Fire Undo Post-Notify Event (C#)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swPartUndoPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
