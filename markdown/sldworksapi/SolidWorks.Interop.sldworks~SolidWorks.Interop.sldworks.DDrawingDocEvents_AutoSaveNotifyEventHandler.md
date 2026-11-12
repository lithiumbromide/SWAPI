---
title: "DDrawingDocEvents_AutoSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_AutoSaveNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AutoSaveNotifyEventHandler.html"
---

# DDrawingDocEvents_AutoSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the drawing document is automatically saved.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_AutoSaveNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_AutoSaveNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_AutoSaveNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_AutoSaveNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Filename to which to save the drawing document

## VBA Syntax

See [AutoSaveNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~AutoSaveNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingAutoSaveNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
