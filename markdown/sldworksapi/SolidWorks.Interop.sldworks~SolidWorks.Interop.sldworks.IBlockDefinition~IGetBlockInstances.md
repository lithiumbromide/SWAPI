---
title: "IGetBlockInstances Method (IBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "IBlockDefinition"
member: "IGetBlockInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~IGetBlockInstances.html"
---

# IGetBlockInstances Method (IBlockDefinition)

Obsolete. Superseded by [ISketchBlockDefinition::GetInstances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetInstances.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBlockInstances( _
   ByVal Count As System.Integer _
) As BlockInstance
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockDefinition
Dim Count As System.Integer
Dim value As BlockInstance

value = instance.IGetBlockInstances(Count)
```

### C#

```csharp
BlockInstance IGetBlockInstances(
   System.int Count
)
```

### C++/CLI

```cpp
BlockInstance^ IGetBlockInstances(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`:

## VBA Syntax

See [BlockDefinition::IGetBlockInstances](ms-its:sldworksapivb6.chm::/sldworks~BlockDefinition~IGetBlockInstances.html).

## See Also

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.html)
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.html)
