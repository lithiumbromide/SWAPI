---
title: "DDrawingDocEvents_FileReloadPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_FileReloadPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileReloadPreNotifyEventHandler.html"
---

# DDrawingDocEvents_FileReloadPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user application when a drawing document is reloaded.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_FileReloadPreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_FileReloadPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_FileReloadPreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_FileReloadPreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FileReloadPreNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~FileReloadPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingFileReloadPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
