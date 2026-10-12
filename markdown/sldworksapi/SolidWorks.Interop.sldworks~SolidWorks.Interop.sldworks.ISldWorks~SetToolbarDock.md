---
title: "SetToolbarDock Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetToolbarDock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock.html"
---

# SetToolbarDock Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::SetToolbarDock2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetToolbarDock2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetToolbarDock( _
   ByVal ModuleIn As System.String, _
   ByVal ToolbarIDIn As System.Integer, _
   ByVal DocStatePosIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim ModuleIn As System.String
Dim ToolbarIDIn As System.Integer
Dim DocStatePosIn As System.Integer

instance.SetToolbarDock(ModuleIn, ToolbarIDIn, DocStatePosIn)
```

### C#

```csharp
void SetToolbarDock(
   System.string ModuleIn,
   System.int ToolbarIDIn,
   System.int DocStatePosIn
)
```

### C++/CLI

```cpp
void SetToolbarDock(
   System.String^ ModuleIn,
   System.int ToolbarIDIn,
   System.int DocStatePosIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleIn`:
- `ToolbarIDIn`:
- `DocStatePosIn`:

## VBA Syntax

See [SldWorks::SetToolbarDock](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetToolbarDock.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
