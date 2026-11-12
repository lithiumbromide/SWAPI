---
title: "InsertBlock Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertBlock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBlock.html"
---

# InsertBlock Method (IDrawingDoc)

Obsolete. Superseded by [ISketchManager::InsertSketchBlockInstance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBlock( _
   ByVal FileName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Scale As System.Double _
) As BlockInstance
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim FileName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Angle As System.Double
Dim Scale As System.Double
Dim value As BlockInstance

value = instance.InsertBlock(FileName, X, Y, Angle, Scale)
```

### C#

```csharp
BlockInstance InsertBlock(
   System.string FileName,
   System.double X,
   System.double Y,
   System.double Angle,
   System.double Scale
)
```

### C++/CLI

```cpp
BlockInstance^ InsertBlock(
   System.String^ FileName,
   System.double X,
   System.double Y,
   System.double Angle,
   System.double Scale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:
- `X`:
- `Y`:
- `Angle`:
- `Scale`:

## VBA Syntax

See [DrawingDoc::InsertBlock](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertBlock.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
