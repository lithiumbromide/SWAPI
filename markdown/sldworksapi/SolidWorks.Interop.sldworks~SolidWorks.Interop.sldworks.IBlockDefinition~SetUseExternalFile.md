---
title: "SetUseExternalFile Method (IBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "IBlockDefinition"
member: "SetUseExternalFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~SetUseExternalFile.html"
---

# SetUseExternalFile Method (IBlockDefinition)

Obsolete. Superseded by [ISketchBlockDefinition::LinkToFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~LinkToFile.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUseExternalFile( _
   ByVal UseFile As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockDefinition
Dim UseFile As System.Boolean
Dim value As System.Integer

value = instance.SetUseExternalFile(UseFile)
```

### C#

```csharp
System.int SetUseExternalFile(
   System.bool UseFile
)
```

### C++/CLI

```cpp
System.int SetUseExternalFile(
   System.bool UseFile
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseFile`:

## VBA Syntax

See [BlockDefinition::SetUseExternalFile](ms-its:sldworksapivb6.chm::/sldworks~BlockDefinition~SetUseExternalFile.html).

## See Also

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.html)
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.html)
