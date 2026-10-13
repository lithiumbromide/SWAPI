---
title: "SaveBlock Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SaveBlock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveBlock.html"
---

# SaveBlock Method (IDrawingDoc)

Obsolete. Superseded by [ISketchBlockDefinition::Save](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~Save.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveBlock( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SaveBlock(FileName)
```

### C#

```csharp
System.bool SaveBlock(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SaveBlock(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [DrawingDoc::SaveBlock](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SaveBlock.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
