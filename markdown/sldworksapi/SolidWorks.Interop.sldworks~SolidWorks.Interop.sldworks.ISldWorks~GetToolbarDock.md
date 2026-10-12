---
title: "GetToolbarDock Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetToolbarDock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock.html"
---

# GetToolbarDock Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::GetToolbarDock2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetToolbarDock2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetToolbarDock( _
   ByVal ModuleIn As System.String, _
   ByVal ToolbarIDIn As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim ModuleIn As System.String
Dim ToolbarIDIn As System.Integer
Dim value As System.Integer

value = instance.GetToolbarDock(ModuleIn, ToolbarIDIn)
```

### C#

```csharp
System.int GetToolbarDock(
   System.string ModuleIn,
   System.int ToolbarIDIn
)
```

### C++/CLI

```cpp
System.int GetToolbarDock(
   System.String^ ModuleIn,
   System.int ToolbarIDIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleIn`:
- `ToolbarIDIn`:

## VBA Syntax

See [SldWorks::GetToolbarDock](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetToolbarDock.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
