---
title: "DPartDocEvents_LoadFromStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_LoadFromStorageStoreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_LoadFromStorageStoreNotifyEventHandler.html"
---

# DPartDocEvents_LoadFromStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when it is safe to load data from third-party IStorage storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_LoadFromStorageStoreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_LoadFromStorageStoreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_LoadFromStorageStoreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_LoadFromStorageStoreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [LoadFromStorageStoreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~LoadFromStorageStoreNotify_EV.html).

## Remarks

Call [IModelDocExtension::IGet3rdPartyStorageStore](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.html) after receiving this notification. This notification is sent even when the third-party storage node is empty.

If developing a C++ application, use [swPartLoadFromStorageStoreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
