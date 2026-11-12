---
title: "DAssemblyDocEvents_FileSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FileSaveNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSaveNotifyEventHandler.html"
---

# DAssemblyDocEvents_FileSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a file is about to be saved and passes the current document name.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FileSaveNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FileSaveNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FileSaveNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FileSaveNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the saved file

## VBA Syntax

See [FileSaveNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FileSaveNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFileSaveNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

When a user saves a document for the first time, SOLIDWORKS generates a [FileSaveAsNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_FileSaveAsNotify2EventHandler.html) event instead of a FileSaveNotify event.

If the user attempts to close the document and S_false is returned, then the document does not close; it remains open and is not saved.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
