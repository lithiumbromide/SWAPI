---
title: "DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler.html"
---

# DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when it is safe to save data to third-party IStorage storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SaveToStorageStoreNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~SaveToStorageStoreNotify_EV.html).

## Remarks

Call [IModelDocExtension::IGet3rdPartyStorageStore](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.html) after receiving this notification.

If developing a C++ application, use [swDrawingSaveToStorageStoreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
