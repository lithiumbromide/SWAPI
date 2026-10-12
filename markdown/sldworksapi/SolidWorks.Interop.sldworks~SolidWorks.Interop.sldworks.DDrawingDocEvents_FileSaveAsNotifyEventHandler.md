---
title: "DDrawingDocEvents_FileSaveAsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_FileSaveAsNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotifyEventHandler.html"
---

# DDrawingDocEvents_FileSaveAsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DDrawingDocEvents_FileSaveAsNotify2EventHandler](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_FileSaveAsNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_FileSaveAsNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_FileSaveAsNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_FileSaveAsNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the current document

## VBA Syntax

See [FileSaveAsNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~FileSaveAsNotify_EV.html).
