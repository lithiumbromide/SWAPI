---
title: "DDrawingDocEvents_FileSavePostCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_FileSavePostCancelNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSavePostCancelNotifyEventHandler.html"
---

# DDrawingDocEvents_FileSavePostCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired if [FileSavePostNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FileSavePostNotifyEventHandler.html) is not fired.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_FileSavePostCancelNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_FileSavePostCancelNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_FileSavePostCancelNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_FileSavePostCancelNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FileSavePostCancelNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~FileSavePostCancelNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingFileSavePostCancelNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
