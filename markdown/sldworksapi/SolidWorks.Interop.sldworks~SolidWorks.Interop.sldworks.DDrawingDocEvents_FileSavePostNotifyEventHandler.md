---
title: "DDrawingDocEvents_FileSavePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_FileSavePostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSavePostNotifyEventHandler.html"
---

# DDrawingDocEvents_FileSavePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a drawing is saved in SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_FileSavePostNotifyEventHandler( _
   ByVal saveType As System.Integer, _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_FileSavePostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_FileSavePostNotifyEventHandler(
   System.int saveType,
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_FileSavePostNotifyEventHandler(
   System.int saveType,
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `saveType`: Type of save as defined in [swFileSaveTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveTypes_e.html)
- `FileName`: Saved file name

## VBA Syntax

See [FileSavePostNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~FileSavePostNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingFileSavePostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
