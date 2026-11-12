---
title: "DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler.html"
---

# DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the user has switched to a different configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveConfigChangePostNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~ActiveConfigChangePostNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingConfigChangePostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
