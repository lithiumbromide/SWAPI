---
title: "DPartDocEvents_FileSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FileSaveNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSaveNotifyEventHandler.html"
---

# DPartDocEvents_FileSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a file is about to be saved and passes the current document name.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FileSaveNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FileSaveNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FileSaveNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FileSaveNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the saved file

## VBA Syntax

See [FileSaveNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FileSaveNotify_EV.html).

## Remarks

When a user selects File, Save on a document that has never been saved, you receive a [FileSaveAsNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileSaveAsNotify2EventHandler.html) instead of FileSaveNotify.

If developing a C++ application, use [swPartFileSaveNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
