---
title: "DDrawingDocEvents_RegenNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_RegenNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RegenNotifyEventHandler.html"
---

# DDrawingDocEvents_RegenNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a drawing document is about to be regenerated.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_RegenNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_RegenNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_RegenNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_RegenNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RegenNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~RegenNotify_EV.html).

## Remarks

You can also use [IModelDoc2::GetUpdateStamp](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUpdateStamp.html) to determine when changes have taken place in this document.

If developing a C++ application, use [swDrawingRegenNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
