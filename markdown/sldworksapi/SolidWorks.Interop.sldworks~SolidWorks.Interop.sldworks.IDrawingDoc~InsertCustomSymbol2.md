---
title: "InsertCustomSymbol2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertCustomSymbol2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCustomSymbol2.html"
---

# InsertCustomSymbol2 Method (IDrawingDoc)

Obsolete. Superseded by [ISketchManager::InsertSketchBlockInstance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCustomSymbol2( _
   ByVal FileName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim FileName As System.String
Dim value As System.Object

value = instance.InsertCustomSymbol2(FileName)
```

### C#

```csharp
System.object InsertCustomSymbol2(
   System.string FileName
)
```

### C++/CLI

```cpp
System.Object^ InsertCustomSymbol2(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [DrawingDoc::InsertCustomSymbol2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertCustomSymbol2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
