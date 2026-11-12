---
title: "SetBasePoint Method (IBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "IBlockDefinition"
member: "SetBasePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~SetBasePoint.html"
---

# SetBasePoint Method (IBlockDefinition)

Obsolete. Superseded by [ISketchBlockDefinition::InsertionPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBasePoint( _
   ByVal BasePoint As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockDefinition
Dim BasePoint As System.Object
Dim value As System.Boolean

value = instance.SetBasePoint(BasePoint)
```

### C#

```csharp
System.bool SetBasePoint(
   System.object BasePoint
)
```

### C++/CLI

```cpp
System.bool SetBasePoint(
   System.Object^ BasePoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BasePoint`:

## VBA Syntax

See [BlockDefinition::SetBasePoint](ms-its:sldworksapivb6.chm::/sldworks~BlockDefinition~SetBasePoint.html).

## See Also

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.html)
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.html)
