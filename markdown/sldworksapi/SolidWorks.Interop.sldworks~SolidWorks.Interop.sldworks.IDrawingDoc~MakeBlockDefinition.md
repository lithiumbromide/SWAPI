---
title: "MakeBlockDefinition Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "MakeBlockDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~MakeBlockDefinition.html"
---

# MakeBlockDefinition Method (IDrawingDoc)

Obsolete. Superseded by [ISkethcManager::MakeSketchBlockFromFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.html), [ISketchManager::MakeSketchBlockSelected](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.html), and [ISketchManager::MakeSketchBlockFromSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeBlockDefinition( _
   ByVal Name As System.String, _
   ByVal XRefFileName As System.String, _
   ByVal Instance As System.Boolean _
) As BlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Name As System.String
Dim XRefFileName As System.String
Dim Instance As System.Boolean
Dim value As BlockDefinition

value = instance.MakeBlockDefinition(Name, XRefFileName, Instance)
```

### C#

```csharp
BlockDefinition MakeBlockDefinition(
   System.string Name,
   System.string XRefFileName,
   System.bool Instance
)
```

### C++/CLI

```cpp
BlockDefinition^ MakeBlockDefinition(
   System.String^ Name,
   System.String^ XRefFileName,
   System.bool Instance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `XRefFileName`:
- `Instance`:

## VBA Syntax

See [DrawingDoc::MakeBlockDefinition](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~MakeBlockDefinition.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
