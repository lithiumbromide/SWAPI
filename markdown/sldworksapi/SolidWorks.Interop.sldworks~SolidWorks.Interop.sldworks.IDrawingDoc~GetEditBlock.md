---
title: "GetEditBlock Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetEditBlock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditBlock.html"
---

# GetEditBlock Method (IDrawingDoc)

Obsolete. Superseded by [ISketchManager::EditSketchBlock](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~EditSketchBlock.html) and [ISketchManager::EndEditSketchBlock](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~EndEditSketchBlock.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEditBlock() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Boolean

value = instance.GetEditBlock()
```

### C#

```csharp
System.bool GetEditBlock()
```

### C++/CLI

```cpp
System.bool GetEditBlock();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::GetEditBlock](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetEditBlock.html).

## Remarks

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
