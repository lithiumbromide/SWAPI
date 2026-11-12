---
title: "DPartDocEvents_FileSaveAsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FileSaveAsNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSaveAsNotifyEventHandler.html"
---

# DPartDocEvents_FileSaveAsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DPartDocEvents_FileSaveAsNotify2EventHandler](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileSaveAsNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FileSaveAsNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FileSaveAsNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FileSaveAsNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FileSaveAsNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

### Return Value

## VBA Syntax

See [FileSaveAsNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FileSaveAsNotify_EV.html).

## Availability
