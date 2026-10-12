---
title: "IGetSplines Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "IGetSplines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines.html"
---

# IGetSplines Method (ISketchBlockDefinition)

Obsolete. Superseded by [ISketchBlockDefinition::GetSplines2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetSplines2.html) and [ISketchBlockDefinition::IGetSplines2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSplines( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim ArraySize As System.Integer
Dim value As System.Double

value = instance.IGetSplines(ArraySize)
```

### C#

```csharp
System.double IGetSplines(
   System.int ArraySize
)
```

### C++/CLI

```cpp
System.double IGetSplines(
   System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`:

## VBA Syntax

See [SketchBlockDefinition::IGetSplines](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~IGetSplines.html).

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
