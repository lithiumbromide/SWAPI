---
title: "DAssemblyDocEvents_LoadFromStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_LoadFromStorageNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LoadFromStorageNotifyEventHandler.html"
---

# DAssemblyDocEvents_LoadFromStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when it is safe to load data from third-party IStream storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_LoadFromStorageNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_LoadFromStorageNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_LoadFromStorageNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_LoadFromStorageNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [LoadFromStorageNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~LoadFromStorageNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyLoadFromStorageNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Call [IModelDoc2::IGet3rdPartyStorage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html) after receiving this notification. This notification is sent even when the third-party storage node is empty.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
