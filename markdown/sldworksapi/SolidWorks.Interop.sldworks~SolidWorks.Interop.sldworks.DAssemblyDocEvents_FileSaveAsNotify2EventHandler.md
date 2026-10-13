---
title: "DAssemblyDocEvents_FileSaveAsNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FileSaveAsNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSaveAsNotify2EventHandler.html"
---

# DAssemblyDocEvents_FileSaveAsNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a file is about to be saved with a new name and passes the new document name. This event is sent before SOLIDWORKS Design displays the File Save dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FileSaveAsNotify2EventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FileSaveAsNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FileSaveAsNotify2EventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FileSaveAsNotify2EventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the saved file

## VBA Syntax

See [FileSaveAsNotify2 Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FileSaveAsNotify2_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFileSaveAsNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

In the FileSaveAsNotify2 event handler, the user can specify the filename that the file should be saved as using [IModelDoc2::SetSaveAsFileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetSaveAsFileName.html). The user should also return S_false from the event handler to indicate the notification is handled. After an appropriate filename is provided and S_false is returned from the event handler, SOLIDWORKS Design does not display the File Save dialog, but uses the filename that was provided with IModelDoc2::SetSaveAsFileName.

If you do not set an alternative filename using IModelDoc2::SetSaveAsFileName and S_false is returned, then the document is not saved. You can omit using ModelDoc2::SetSaveAsFileName to not set an alternative filename.

NOTE: Because this event is very similar to the now obsolete IAssemblyDoc event FileSaveAsNotify, do not listen for both notifications at the same time.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
