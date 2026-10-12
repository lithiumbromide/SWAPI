---
title: "DPartDocEvents_FileDropPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FileDropPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileDropPostNotifyEventHandler.html"
---

# DPartDocEvents_FileDropPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies user applications when a part is dropped from File Explorer into a part document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FileDropPostNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FileDropPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FileDropPostNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FileDropPostNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path and name of file dropped

## VBA Syntax

See [FileDropPostNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FileDropPostNotify_EV.html).

## Remarks

The part document may be replaced by the dropped file.

SOLIDWORKS passes the file name of the dropped part into the event handler. The event handler can use [IPartDoc::SetDroppedFileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~SetDroppedFileName.html) to replace this document with a temporary document. For example, this is useful when the file being dropped is managed by a project data management (PDM) system or otherwise not accessible directly by SOLIDWORKS. Your application (the PDM system in this example) is responsible for ensuring that the files and references are properly updated.

If developing a C++ application, use [swPartFileDropPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
