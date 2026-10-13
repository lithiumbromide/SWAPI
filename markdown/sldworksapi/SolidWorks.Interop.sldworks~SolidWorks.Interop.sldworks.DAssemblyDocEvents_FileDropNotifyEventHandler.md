---
title: "DAssemblyDocEvents_FileDropNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FileDropNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropNotifyEventHandler.html"
---

# DAssemblyDocEvents_FileDropNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a part is dropped from File Explorer into an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FileDropNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FileDropNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FileDropNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FileDropNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: File name of the part

## VBA Syntax

See [FileDropNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FileDropNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFileDropNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

[IAssemblyDoc::SetDroppedFileConfigName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~SetDroppedFileConfigName.html) allows you to set the configuration name for the recently dropped part, thereby avoiding the configuration name selection dialog.

SOLIDWORKS passes the file name of the dropped part into the event handler. The event handler can use [IAssemblyDoc::SetDroppedFileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.html) to replace this document with a temporary document. For example, this is useful when the file being dropped is managed by a project data management (PDM) system or otherwise not accessible directly by SOLIDWORKS Design. Your application (the PDM system in this example) is responsible for ensuring that the files and references are properly updated.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
