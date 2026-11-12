---
title: "InsertCustomSymbol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertCustomSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCustomSymbol.html"
---

# InsertCustomSymbol Method (IDrawingDoc)

Obsolete. Superseded by [ISketchManager::InsertSketchBlockInstance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertCustomSymbol( _
   ByVal SymbolPath As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim SymbolPath As System.String

instance.InsertCustomSymbol(SymbolPath)
```

### C#

```csharp
void InsertCustomSymbol(
   System.string SymbolPath
)
```

### C++/CLI

```cpp
void InsertCustomSymbol(
   System.String^ SymbolPath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymbolPath`:

## VBA Syntax

See [DrawingDoc::InsertCustomSymbol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertCustomSymbol.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
