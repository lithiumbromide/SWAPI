---
title: "DPartDocEvents_FileReloadPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FileReloadPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileReloadPreNotifyEventHandler.html"
---

# DPartDocEvents_FileReloadPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when an part document is reloaded

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FileReloadPreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FileReloadPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FileReloadPreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FileReloadPreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FileReloadPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FileReloadPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartFileReloadPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
