---
title: "DAssemblyDocEvents_RedoPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_RedoPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RedoPostNotifyEventHandler.html"
---

# DAssemblyDocEvents_RedoPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after a Redo operation occurs in an assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_RedoPostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_RedoPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_RedoPostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_RedoPostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RedoPostNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~RedoPostNotify_EV.html).

## Examples

[Fire Undo and Redo Pre- and Post-notifications in Assembly Document (C#)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_CSharp.htm)
[Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VB.NET)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_VBNET.htm)
[Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VBA)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_VB6.htm)

## Remarks

If developing a C++ application, use [swAssemblyRedoPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
