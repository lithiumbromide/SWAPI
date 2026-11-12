---
title: "DAssemblyDocEvents_FileReloadCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FileReloadCancelNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileReloadCancelNotifyEventHandler.html"
---

# DAssemblyDocEvents_FileReloadCancelNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired if the IAssembly event [FileReloadNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_FileReloadNotifyEventHandler.html) is canceled.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FileReloadCancelNotifyEventHandler( _
   ByVal ErrorCode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FileReloadCancelNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FileReloadCancelNotifyEventHandler(
   System.int ErrorCode
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FileReloadCancelNotifyEventHandler(
   System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ErrorCode`: Error as defined in [swComponentReloadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentReloadError_e.html)

## VBA Syntax

See [FileReloadCancelNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FileReloadCancelNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFileReloadCancelNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
