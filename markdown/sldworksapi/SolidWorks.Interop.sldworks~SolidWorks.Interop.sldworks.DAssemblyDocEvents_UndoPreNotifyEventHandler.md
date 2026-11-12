---
title: "DAssemblyDocEvents_UndoPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_UndoPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UndoPreNotifyEventHandler.html"
---

# DAssemblyDocEvents_UndoPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before an Undo operation occurs in an assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_UndoPreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_UndoPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_UndoPreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_UndoPreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [UndoPreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~UndoPreNotify_EV.html).

## Examples

[Fire Undo and Redo Pre- and Post-notifications in Assembly Document (C#)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_CSharp.htm)
[Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VB.NET)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_VBNET.htm)
[Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VBA)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_VB6.htm)

## Remarks

If developing a C++ application, use [swAssemblyUndoPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
