---
title: "DDrawingDocEvents_UserSelectionPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_UserSelectionPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UserSelectionPostNotifyEventHandler.html"
---

# DDrawingDocEvents_UserSelectionPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after an entity is selected in a drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_UserSelectionPostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_UserSelectionPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_UserSelectionPostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_UserSelectionPostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [UserSelectionPostNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~UserSelectionPostNotify_EV.html).

## Examples

[Fire Event After Selection Made (C#)](Fire_Event_After_Selection_Made_Example_CSharp.htm)
[Fire Event After Selection Made (VB.NET)](Fire_Event_After_Selection_Made_Example_VBNET.htm)
[Fire Event After Selection Made (VBA)](Fire_Event_After_Selection_Made_Example_VB.htm)

## Remarks

Only selections made interactively fire this event; selections made programmatically are ignored by this event.

If developing a C++ application, use [swDrawingUserSelectionPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
