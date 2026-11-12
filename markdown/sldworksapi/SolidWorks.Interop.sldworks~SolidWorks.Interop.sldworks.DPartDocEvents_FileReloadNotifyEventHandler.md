---
title: "DPartDocEvents_FileReloadNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FileReloadNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileReloadNotifyEventHandler.html"
---

# DPartDocEvents_FileReloadNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a part document is reloaded.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FileReloadNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FileReloadNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FileReloadNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FileReloadNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FileReloadNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FileReloadNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartFileReloadNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
