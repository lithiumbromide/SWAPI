---
title: "InsertInstance Method (IBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "IBlockDefinition"
member: "InsertInstance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~InsertInstance.html"
---

# InsertInstance Method (IBlockDefinition)

Obsolete. Superseded by [ISketchManager::InsertSketchBlockInstance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertInstance( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Scale As System.Double _
) As BlockInstance
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockDefinition
Dim X As System.Double
Dim Y As System.Double
Dim Angle As System.Double
Dim Scale As System.Double
Dim value As BlockInstance

value = instance.InsertInstance(X, Y, Angle, Scale)
```

### C#

```csharp
BlockInstance InsertInstance(
   System.double X,
   System.double Y,
   System.double Angle,
   System.double Scale
)
```

### C++/CLI

```cpp
BlockInstance^ InsertInstance(
   System.double X,
   System.double Y,
   System.double Angle,
   System.double Scale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Angle`:
- `Scale`:

## VBA Syntax

See [BlockDefinition::InsertInstance](ms-its:sldworksapivb6.chm::/sldworks~BlockDefinition~InsertInstance.html).

## See Also

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.html)
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.html)
