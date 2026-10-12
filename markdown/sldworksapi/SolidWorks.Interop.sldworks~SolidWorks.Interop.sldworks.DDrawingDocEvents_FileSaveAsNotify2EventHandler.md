---
title: "DDrawingDocEvents_FileSaveAsNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_FileSaveAsNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler.html"
---

# DDrawingDocEvents_FileSaveAsNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Sends pre-notification before displaying the File, Save dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_FileSaveAsNotify2EventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_FileSaveAsNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_FileSaveAsNotify2EventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_FileSaveAsNotify2EventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the saved file

## VBA Syntax

See [FileSaveAsNotify2 Event (DrawingDoc).](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~FileSaveAsNotify2_EV.html)

## Remarks

SOLIDWORKS sends this notification before it displays the Save dialog.

In the FileSaveAsNotify2 event handler, you can specify an alternate file name using [IModelDoc2::SetSaveAsFileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetSaveAsFileName.html) and return S_false from the event handler to indicate that the notification is handled. If you do not set an alternative filename using IModelDoc2::SetSaveAsFileName and S_false is returned, then the document is not saved. You can omit using IModelDoc2::SetSaveAsFileName to not set an alternative filename.

You can return S_false to stop SOLIDWORKS from proceeding with the action that caused the notification. In .NET, you can return 1 instead of S_false.

NOTE: Because this event is very similar to the now obsolete Drawing Doc event [FileSaveAsNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotifyEventHandler.html), do not listen for both notifications at the same time.

If developing a C++ application, use [swDrawingFileSaveAsNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
