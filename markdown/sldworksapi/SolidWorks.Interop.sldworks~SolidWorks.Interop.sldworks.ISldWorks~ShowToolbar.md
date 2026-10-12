---
title: "ShowToolbar Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ShowToolbar"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowToolbar.html"
---

# ShowToolbar Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::ShowToolbar2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowToolbar2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowToolbar( _
   ByVal ModuleName As System.String, _
   ByVal ToolbarId As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim ModuleName As System.String
Dim ToolbarId As System.Integer
Dim value As System.Boolean

value = instance.ShowToolbar(ModuleName, ToolbarId)
```

### C#

```csharp
System.bool ShowToolbar(
   System.string ModuleName,
   System.int ToolbarId
)
```

### C++/CLI

```cpp
System.bool ShowToolbar(
   System.String^ ModuleName,
   System.int ToolbarId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleName`:
- `ToolbarId`:

## VBA Syntax

See [SldWorks::ShowToolbar](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ShowToolbar.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
