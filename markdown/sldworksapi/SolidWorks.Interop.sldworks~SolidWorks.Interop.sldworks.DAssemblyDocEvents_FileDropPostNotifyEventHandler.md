---
title: "DAssemblyDocEvents_FileDropPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FileDropPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropPostNotifyEventHandler.html"
---

# DAssemblyDocEvents_FileDropPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies user applications when a part is dropped from File Explorer into an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FileDropPostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FileDropPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FileDropPostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FileDropPostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FileDropPostNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FileDropPostNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFileDropPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

SOLIDWORKS passes the file name of the dropped part into the event handler. The event handler can use [IAssemblyDoc::SetDroppedFileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.html) to replace this document with a temporary document. For example, this is useful when the file being dropped is managed by a project data management (PDM) system or otherwise not accessible directly by SOLIDWORKS Design. Your application (the PDM system in this example) is responsible for ensuring that the files and references are properly updated.

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
