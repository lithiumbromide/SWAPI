---
title: "DPartDocEvents_FileSaveAsNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FileSaveAsNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSaveAsNotify2EventHandler.html"
---

# DPartDocEvents_FileSaveAsNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Sends pre-notification before displaying the File, Save dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FileSaveAsNotify2EventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FileSaveAsNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FileSaveAsNotify2EventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FileSaveAsNotify2EventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the saved file

## VBA Syntax

See [FileSaveAsNotify2 Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FileSaveAsNotify2_EV.html).

## Remarks

In this event handler, the user can specify the filename that the file should be saved to by using [IModelDoc2::SetSaveAsFileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetSaveAsFileName.html) and also returning S_false from the event handler. After providing an appropriate filename and after S_false is returned from the event handler, the File, Save dialog is not displayed; instead, the filename that was provided with IModelDoc2::SetSaveAsFileName is used.

If developing a C++ application, use [swPartFileSaveAsNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
