---
title: "IGetNotes Method (IBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "IBlockDefinition"
member: "IGetNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~IGetNotes.html"
---

# IGetNotes Method (IBlockDefinition)

Obsolete. Superseded by [ISketchBlockDefinition::GetNotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetNotes.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNotes( _
   ByVal NumNotes As System.Integer _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockDefinition
Dim NumNotes As System.Integer
Dim value As Note

value = instance.IGetNotes(NumNotes)
```

### C#

```csharp
Note IGetNotes(
   System.int NumNotes
)
```

### C++/CLI

```cpp
Note^ IGetNotes(
   System.int NumNotes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumNotes`:

## VBA Syntax

See [BlockDefinition::IGetNotes](ms-its:sldworksapivb6.chm::/sldworks~BlockDefinition~IGetNotes.html).

## See Also

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.html)
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.html)
