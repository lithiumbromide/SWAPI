---
title: "DAssemblyDocEvents_FileSaveAsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FileSaveAsNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSaveAsNotifyEventHandler.html"
---

# DAssemblyDocEvents_FileSaveAsNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DAssemblyDocEvents_FileSaveAsNotify2EventHandler](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_FileSaveAsNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FileSaveAsNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FileSaveAsNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FileSaveAsNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FileSaveAsNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

### Return Value

## VBA Syntax

See [FileSaveAsNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FileSaveAsNotify_EV.html).

## Availability
