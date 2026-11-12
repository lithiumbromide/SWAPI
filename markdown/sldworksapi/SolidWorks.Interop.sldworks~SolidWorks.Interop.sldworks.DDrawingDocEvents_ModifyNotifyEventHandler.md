---
title: "DDrawingDocEvents_ModifyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_ModifyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ModifyNotifyEventHandler.html"
---

# DDrawingDocEvents_ModifyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a document is marked as dirty for the first time.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_ModifyNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_ModifyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_ModifyNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_ModifyNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModifyNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~ModifyNotify_EV.html).

## Remarks

If the user saves the document in the current SOLIDWORKS Design session, then the event is fired when the document is marked dirty again.

If developing a C++ application, use [swDrawingModifyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
