---
title: "DAssemblyDocEvents_FileSavePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FileSavePostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSavePostNotifyEventHandler.html"
---

# DAssemblyDocEvents_FileSavePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a file is saved in SOLIDWORKS Design.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FileSavePostNotifyEventHandler( _
   ByVal saveType As System.Integer, _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FileSavePostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FileSavePostNotifyEventHandler(
   System.int saveType,
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FileSavePostNotifyEventHandler(
   System.int saveType,
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `saveType`: Type of save as defined in [swFileSaveTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveTypes_e.html)
- `FileName`: Saved file name

## VBA Syntax

See [FileSavePostNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FileSavePostNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFileSavePostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
