---
title: "DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler.html"
---

# DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the part document is automatically saved to third-party IStorage storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [AutoSaveToStorageStoreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~AutoSaveToStorageStoreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAutoSaveToStorageStoreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
