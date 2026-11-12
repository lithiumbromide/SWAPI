---
title: "IInsertCustomSymbol2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IInsertCustomSymbol2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertCustomSymbol2.html"
---

# IInsertCustomSymbol2 Method (IDrawingDoc)

Obsolete. Superseded by [ISketchManager::InsertSketchBlockInstance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertCustomSymbol2( _
   ByVal FileName As System.String _
) As CustomSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim FileName As System.String
Dim value As CustomSymbol

value = instance.IInsertCustomSymbol2(FileName)
```

### C#

```csharp
CustomSymbol IInsertCustomSymbol2(
   System.string FileName
)
```

### C++/CLI

```cpp
CustomSymbol^ IInsertCustomSymbol2(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [DrawingDoc::IInsertCustomSymbol2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IInsertCustomSymbol2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
