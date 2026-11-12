---
title: "DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler.html"
---

# DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when it is safe to save data to third-party IStorage storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_SaveToStorageStoreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SaveToStorageStoreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~SaveToStorageStoreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblySaveToStorageStoreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Call [IModelDocExtension::IGet3rdPartyStorageStore](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.html) after receiving this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
