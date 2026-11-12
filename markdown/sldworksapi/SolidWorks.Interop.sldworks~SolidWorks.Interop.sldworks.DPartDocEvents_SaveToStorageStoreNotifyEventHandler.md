---
title: "DPartDocEvents_SaveToStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_SaveToStorageStoreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SaveToStorageStoreNotifyEventHandler.html"
---

# DPartDocEvents_SaveToStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when it is safe to save data to third-party IStorage storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_SaveToStorageStoreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_SaveToStorageStoreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_SaveToStorageStoreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_SaveToStorageStoreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SaveToStorageStoreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~SaveToStorageStoreNotify_EV.html).

## Remarks

Call [IModelDocExtension::IGet3rdPartyStorageStore](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGet3rdPartyStorageStore.html) after receiving this notification.

If developing a C++ application, use [swPartSaveToStorageStoreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
