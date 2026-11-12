---
title: "GetToolbarState Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetToolbarState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState.html"
---

# GetToolbarState Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::GetToolbarState2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetToolbarState2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetToolbarState( _
   ByVal Module As System.String, _
   ByVal ToolbarId As System.Integer, _
   ByVal ToolbarState As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Module As System.String
Dim ToolbarId As System.Integer
Dim ToolbarState As System.Integer
Dim value As System.Boolean

value = instance.GetToolbarState(Module, ToolbarId, ToolbarState)
```

### C#

```csharp
System.bool GetToolbarState(
   System.string Module,
   System.int ToolbarId,
   System.int ToolbarState
)
```

### C++/CLI

```cpp
System.bool GetToolbarState(
   System.String^ Module,
   System.int ToolbarId,
   System.int ToolbarState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Module`:
- `ToolbarId`:
- `ToolbarState`:

## VBA Syntax

See [SldWorks::GetToolbarState](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetToolbarState.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
