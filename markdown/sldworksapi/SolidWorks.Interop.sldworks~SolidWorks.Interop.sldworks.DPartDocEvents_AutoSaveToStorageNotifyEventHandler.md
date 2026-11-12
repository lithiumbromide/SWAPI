---
title: "DPartDocEvents_AutoSaveToStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_AutoSaveToStorageNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AutoSaveToStorageNotifyEventHandler.html"
---

# DPartDocEvents_AutoSaveToStorageNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the part document is automatically saved to third-party IStream storage.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_AutoSaveToStorageNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_AutoSaveToStorageNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_AutoSaveToStorageNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_AutoSaveToStorageNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [AutoSaveToStorageNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~AutoSaveToStorageNotify_EV.html).

## Remarks

If developing a C++ application, use [swAutoSaveToStorageNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
