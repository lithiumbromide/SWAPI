---
title: "HideToolbar Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "HideToolbar"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar.html"
---

# HideToolbar Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::HideToolbar2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~HideToolbar2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function HideToolbar( _
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

value = instance.HideToolbar(ModuleName, ToolbarId)
```

### C#

```csharp
System.bool HideToolbar(
   System.string ModuleName,
   System.int ToolbarId
)
```

### C++/CLI

```cpp
System.bool HideToolbar(
   System.String^ ModuleName,
   System.int ToolbarId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleName`:
- `ToolbarId`:

## VBA Syntax

See [SldWorks::HideToolbar](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~HideToolbar.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
