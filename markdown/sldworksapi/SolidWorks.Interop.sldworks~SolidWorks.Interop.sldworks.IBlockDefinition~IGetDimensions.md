---
title: "IGetDimensions Method (IBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "IBlockDefinition"
member: "IGetDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~IGetDimensions.html"
---

# IGetDimensions Method (IBlockDefinition)

Obsolete. Superseded by [ISketchBlockDefinition::GetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDimensions( _
   ByVal NumDimensions As System.Integer _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockDefinition
Dim NumDimensions As System.Integer
Dim value As DisplayDimension

value = instance.IGetDimensions(NumDimensions)
```

### C#

```csharp
DisplayDimension IGetDimensions(
   System.int NumDimensions
)
```

### C++/CLI

```cpp
DisplayDimension^ IGetDimensions(
   System.int NumDimensions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumDimensions`:

## VBA Syntax

See [BlockDefinition::IGetDimensions](ms-its:sldworksapivb6.chm::/sldworks~BlockDefinition~IGetDimensions.html).

## See Also

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.html)
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.html)
