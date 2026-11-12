---
title: "DAssemblyDocEvents_SaveToStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_SaveToStorageNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SaveToStorageNotifyEventHandler.html"
---

# DAssemblyDocEvents_SaveToStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when it is safe to save data to third-party IStream storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_SaveToStorageNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_SaveToStorageNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_SaveToStorageNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_SaveToStorageNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SaveToStorageNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~SaveToStorageNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblySaveToStorageNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Call [IModelDoc2::IGet3rdPartyStorage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html) after receiving this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
