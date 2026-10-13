---
title: "IMakeCustomSymbol2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IMakeCustomSymbol2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IMakeCustomSymbol2.html"
---

# IMakeCustomSymbol2 Method (IDrawingDoc)

Obsolete. Superseded by [ISkethcManager::MakeSketchBlockFromFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.html), [ISketchManager::MakeSketchBlockSelected](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.html), and [ISketchManager::MakeSketchBlockFromSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IMakeCustomSymbol2() As CustomSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As CustomSymbol

value = instance.IMakeCustomSymbol2()
```

### C#

```csharp
CustomSymbol IMakeCustomSymbol2()
```

### C++/CLI

```cpp
CustomSymbol^ IMakeCustomSymbol2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::IMakeCustomSymbol2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IMakeCustomSymbol2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
