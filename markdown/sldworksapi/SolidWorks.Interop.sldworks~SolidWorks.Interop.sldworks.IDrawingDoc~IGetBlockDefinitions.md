---
title: "IGetBlockDefinitions Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IGetBlockDefinitions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetBlockDefinitions.html"
---

# IGetBlockDefinitions Method (IDrawingDoc)

Obsolete. Superseded by [SketchManager::GetSketchBlockDefinitions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBlockDefinitions( _
   ByVal Count As System.Integer _
) As BlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Count As System.Integer
Dim value As BlockDefinition

value = instance.IGetBlockDefinitions(Count)
```

### C#

```csharp
BlockDefinition IGetBlockDefinitions(
   System.int Count
)
```

### C++/CLI

```cpp
BlockDefinition^ IGetBlockDefinitions(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`:

## VBA Syntax

See [DrawingDoc::IGetBlockDefinitions](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IGetBlockDefinitions.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
