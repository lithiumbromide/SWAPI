---
title: "DPartDocEvents_FileReloadCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FileReloadCancelNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileReloadCancelNotifyEventHandler.html"
---

# DPartDocEvents_FileReloadCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired if [FileReloadNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileReloadNotifyEventHandler.html) is canceled.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FileReloadCancelNotifyEventHandler( _
   ByVal ErrorCode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FileReloadCancelNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FileReloadCancelNotifyEventHandler(
   System.int ErrorCode
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FileReloadCancelNotifyEventHandler(
   System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ErrorCode`: Error as defined in [swComponentReloadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentReloadError_e.html)

## VBA Syntax

See [FileReloadCancelNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FileReloadCancelNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartFileReloadCancelNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
