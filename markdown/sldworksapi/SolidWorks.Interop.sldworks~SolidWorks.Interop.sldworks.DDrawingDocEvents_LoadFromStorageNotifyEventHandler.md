---
title: "DDrawingDocEvents_LoadFromStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_LoadFromStorageNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_LoadFromStorageNotifyEventHandler.html"
---

# DDrawingDocEvents_LoadFromStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when it is safe to load data from third-party IStream storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_LoadFromStorageNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_LoadFromStorageNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_LoadFromStorageNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_LoadFromStorageNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [LoadFromStorageNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~LoadFromStorageNotify_EV.html).

## Remarks

Call [IModelDoc2::IGet3rdPartyStorage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html) after receiving this notification. This notification is sent even when the third-party storage node is empty.

If developing a C++ application, use [swDrawingLoadFromStorageNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
