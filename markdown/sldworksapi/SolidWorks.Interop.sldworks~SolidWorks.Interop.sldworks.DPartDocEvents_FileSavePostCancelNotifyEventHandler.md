---
title: "DPartDocEvents_FileSavePostCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FileSavePostCancelNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSavePostCancelNotifyEventHandler.html"
---

# DPartDocEvents_FileSavePostCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired if [FileSavePostNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileSavePostNotifyEventHandler.html) is not fired.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FileSavePostCancelNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FileSavePostCancelNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FileSavePostCancelNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FileSavePostCancelNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FileSavePostCancelNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FileSavePostCancelNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartFileSavePostCancelNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
