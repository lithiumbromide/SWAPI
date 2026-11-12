---
title: "DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler.html"
---

# DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when the selection is deleted.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DeleteSelectionPreNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~DeleteSelectionPreNotify_EV.html).

## Remarks

Returning S_false from your notification handler prevents deletion of the selected item.

If developing a C++ application, use [swDrawingDeleteSelectionPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
