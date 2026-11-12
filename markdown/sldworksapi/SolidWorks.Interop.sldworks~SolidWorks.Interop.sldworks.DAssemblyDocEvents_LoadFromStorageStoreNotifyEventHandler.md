---
title: "DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler.html"
---

# DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when it is safe to load data from third-party IStorage storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_LoadFromStorageStoreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [LoadFromStorageStoreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~LoadFromStorageStoreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyLoadFromStorageStoreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Call [IModelDocExtension::IGet3rdPartyStorageStore](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.html) after receiving this notification. This notification is sent even when the third-party storage node is empty.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
