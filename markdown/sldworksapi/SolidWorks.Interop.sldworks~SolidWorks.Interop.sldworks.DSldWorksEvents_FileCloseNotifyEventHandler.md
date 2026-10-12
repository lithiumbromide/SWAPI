---
title: "DSldWorksEvents_FileCloseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_FileCloseNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileCloseNotifyEventHandler.html"
---

# DSldWorksEvents_FileCloseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when SOLIDWORKS is finished closing a file.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_FileCloseNotifyEventHandler( _
   ByVal FileName As System.String, _
   ByVal reason As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_FileCloseNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_FileCloseNotifyEventHandler(
   System.string FileName,
   System.int reason
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_FileCloseNotifyEventHandler(
   System.String^ FileName,
   System.int reason
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of closed file
- `reason`: Reason for closing as defined in [swFileCloseNotifyReason_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileCloseNotifyReason_e.html)

## VBA Syntax

See [FileCloseNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~FileCloseNotify_EV.html).

## Examples

Contact SOLIDWORKS API Support to obtain **Close and Reopen a Drawing Document (VBA, VB.NET, C#).**

## Remarks

This event occurs after a drawing document is closed using [ISldWorks::CloseAndReopen](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CloseAndReopen.html).

If developing a C++ application, use [swAppFileCloseNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
