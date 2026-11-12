---
title: "DDrawingDocEvents_SaveToStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_SaveToStorageNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_SaveToStorageNotifyEventHandler.html"
---

# DDrawingDocEvents_SaveToStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when it is safe to save data to third-party IStream storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_SaveToStorageNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_SaveToStorageNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_SaveToStorageNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_SaveToStorageNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SaveToStorageNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~SaveToStorageNotify_EV.html).

## Remarks

Call [IModelDoc2::IGet3rdPartyStorage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html) after receiving this notification.

If developing a C++ application, use [swDrawingSaveToStorageNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
