---
title: "DDrawingDocEvents_ClearSelectionsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_ClearSelectionsNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ClearSelectionsNotifyEventHandler.html"
---

# DDrawingDocEvents_ClearSelectionsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when selections are cleared using Clear Selections.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_ClearSelectionsNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_ClearSelectionsNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_ClearSelectionsNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_ClearSelectionsNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ClearSelectionsNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~ClearSelectionsNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingClearNotificationsNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
