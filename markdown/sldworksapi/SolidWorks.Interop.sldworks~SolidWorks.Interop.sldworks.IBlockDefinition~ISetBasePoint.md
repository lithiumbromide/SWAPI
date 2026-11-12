---
title: "ISetBasePoint Method (IBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "IBlockDefinition"
member: "ISetBasePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~ISetBasePoint.html"
---

# ISetBasePoint Method (IBlockDefinition)

Obsolete. Superseded by [ISketchBlockDefinition::InsertionPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetBasePoint( _
   ByRef BasePoint As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockDefinition
Dim BasePoint As System.Double
Dim value As System.Boolean

value = instance.ISetBasePoint(BasePoint)
```

### C#

```csharp
System.bool ISetBasePoint(
   ref System.double BasePoint
)
```

### C++/CLI

```cpp
System.bool ISetBasePoint(
   System.double% BasePoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BasePoint`:

## VBA Syntax

See [BlockDefinition::ISetBasePoint](ms-its:sldworksapivb6.chm::/sldworks~BlockDefinition~ISetBasePoint.html).

## See Also

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.html)
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.html)
