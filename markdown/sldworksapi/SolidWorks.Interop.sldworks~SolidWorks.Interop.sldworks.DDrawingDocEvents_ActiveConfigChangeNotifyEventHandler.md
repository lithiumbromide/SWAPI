---
title: "DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler.html"
---

# DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when the user is about to switch to a different configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveConfigChangeNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~ActiveConfigChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingConfigChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
