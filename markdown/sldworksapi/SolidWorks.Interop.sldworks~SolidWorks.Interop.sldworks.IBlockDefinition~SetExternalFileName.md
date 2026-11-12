---
title: "SetExternalFileName Method (IBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "IBlockDefinition"
member: "SetExternalFileName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~SetExternalFileName.html"
---

# SetExternalFileName Method (IBlockDefinition)

Obsolete. Superseded by [ISketchBlockDefinition::FileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~FileName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetExternalFileName( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockDefinition
Dim FileName As System.String
Dim value As System.Integer

value = instance.SetExternalFileName(FileName)
```

### C#

```csharp
System.int SetExternalFileName(
   System.string FileName
)
```

### C++/CLI

```cpp
System.int SetExternalFileName(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [BlockDefinition::SetExternalFileName](ms-its:sldworksapivb6.chm::/sldworks~BlockDefinition~SetExternalFileName.html).

## See Also

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.html)
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.html)
