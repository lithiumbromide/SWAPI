---
title: "DDrawingDocEvents_FileSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_FileSaveNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveNotifyEventHandler.html"
---

# DDrawingDocEvents_FileSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a file is about to be saved and passes the current document name.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_FileSaveNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_FileSaveNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_FileSaveNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_FileSaveNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the file to save

## VBA Syntax

See [FileSaveNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~FileSaveNotify_EV.html).

## Remarks

When a user selects File, Save for a document that has never been saved, SOLIDWORKS generates [FileSaveAsNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler.html) instead of FileSaveNotify. You can return S_false to stop SOLIDWORKS from proceeding with the action that generated the notification.

If the user attempts to close the document and S_false is returned, then the document does not close; it remains open and is not saved.

If developing a C++ application, use [swDrawingFileSaveAsNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
