---
title: "DPartDocEvents_RedoPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_RedoPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RedoPostNotifyEventHandler.html"
---

# DPartDocEvents_RedoPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after a Redo operation occurs in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_RedoPostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_RedoPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_RedoPostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_RedoPostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RedoPostNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~RedoPostNotify_EV.html).

## Examples

[Fire Undo and Redo Pre- and Post-notifications in a Part Document (C#)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Part_Document_Example_CSharp.htm)
[Fire Undo and Redo Pre- and Post-notifications in a Part Document (VB.NET)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VBNET.htm)
[Fire Undo and Redo Pre- and Post-notifications in a Part Document (VBA)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VB6.htm)

## Remarks

If developing a C++ application, use [swPartRedoPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
