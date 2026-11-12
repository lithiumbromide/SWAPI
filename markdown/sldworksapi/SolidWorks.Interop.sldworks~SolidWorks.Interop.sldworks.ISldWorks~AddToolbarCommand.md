---
title: "AddToolbarCommand Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddToolbarCommand"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand.html"
---

# AddToolbarCommand Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddToolbarCommand2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddToolbarCommand2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddToolbarCommand( _
   ByVal ModuleName As System.String, _
   ByVal ToolbarId As System.Integer, _
   ByVal ToolbarIndex As System.Integer, _
   ByVal CommandString As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim ModuleName As System.String
Dim ToolbarId As System.Integer
Dim ToolbarIndex As System.Integer
Dim CommandString As System.String
Dim value As System.Boolean

value = instance.AddToolbarCommand(ModuleName, ToolbarId, ToolbarIndex, CommandString)
```

### C#

```csharp
System.bool AddToolbarCommand(
   System.string ModuleName,
   System.int ToolbarId,
   System.int ToolbarIndex,
   System.string CommandString
)
```

### C++/CLI

```cpp
System.bool AddToolbarCommand(
   System.String^ ModuleName,
   System.int ToolbarId,
   System.int ToolbarIndex,
   System.String^ CommandString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModuleName`:
- `ToolbarId`:
- `ToolbarIndex`:
- `CommandString`:

## VBA Syntax

See [SldWorks::AddToolbarCommand](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddToolbarCommand.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
