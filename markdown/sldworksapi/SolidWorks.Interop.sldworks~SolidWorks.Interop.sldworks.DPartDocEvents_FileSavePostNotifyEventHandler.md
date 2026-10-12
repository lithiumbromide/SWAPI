---
title: "DPartDocEvents_FileSavePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FileSavePostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSavePostNotifyEventHandler.html"
---

# DPartDocEvents_FileSavePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a part document is saved.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FileSavePostNotifyEventHandler( _
   ByVal saveType As System.Integer, _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FileSavePostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FileSavePostNotifyEventHandler(
   System.int saveType,
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FileSavePostNotifyEventHandler(
   System.int saveType,
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `saveType`: Type of save as defined in [swFileSaveTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveTypes_e.html)
- `FileName`: Saved file name

## VBA Syntax

See [FileSavePostNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FileSavePostNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartFileSavePostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
