---
title: "RemoveToolbar Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveToolbar"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar.html"
---

# RemoveToolbar Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::RemoveToobar2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveToolbar2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveToolbar( _
   ByVal Module As System.String, _
   ByVal ToolbarId As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Module As System.String
Dim ToolbarId As System.Integer
Dim value As System.Boolean

value = instance.RemoveToolbar(Module, ToolbarId)
```

### C#

```csharp
System.bool RemoveToolbar(
   System.string Module,
   System.int ToolbarId
)
```

### C++/CLI

```cpp
System.bool RemoveToolbar(
   System.String^ Module,
   System.int ToolbarId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Module`:
- `ToolbarId`:

## VBA Syntax

See [SldWorks::RemoveToolbar](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveToolbar.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
