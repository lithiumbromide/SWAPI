---
title: "CreateCustomSymbol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateCustomSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCustomSymbol.html"
---

# CreateCustomSymbol Method (IDrawingDoc)

Obsolete. Superseded by [ISkethcManager::MakeSketchBlockFromFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.html), [ISketchManager::MakeSketchBlockSelected](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.html), and [ISketchManager::MakeSketchBlockFromSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCustomSymbol( _
   ByVal Segments As System.Object, _
   ByVal Points As System.Object, _
   ByVal Notes As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Segments As System.Object
Dim Points As System.Object
Dim Notes As System.Object
Dim value As System.Object

value = instance.CreateCustomSymbol(Segments, Points, Notes)
```

### C#

```csharp
System.object CreateCustomSymbol(
   System.object Segments,
   System.object Points,
   System.object Notes
)
```

### C++/CLI

```cpp
System.Object^ CreateCustomSymbol(
   System.Object^ Segments,
   System.Object^ Points,
   System.Object^ Notes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Segments`:
- `Points`:
- `Notes`:

## VBA Syntax

See [DrawingDoc::CreateCustomSymbol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateCustomSymbol.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
