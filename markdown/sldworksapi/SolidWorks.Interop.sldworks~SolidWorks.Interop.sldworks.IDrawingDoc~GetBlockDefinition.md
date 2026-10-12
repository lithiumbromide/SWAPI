---
title: "GetBlockDefinition Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetBlockDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetBlockDefinition.html"
---

# GetBlockDefinition Method (IDrawingDoc)

Obsolete. Superseded by [SketchManager::GetSketchBlockDefinitions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBlockDefinition( _
   ByVal Name As System.String _
) As BlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Name As System.String
Dim value As BlockDefinition

value = instance.GetBlockDefinition(Name)
```

### C#

```csharp
BlockDefinition GetBlockDefinition(
   System.string Name
)
```

### C++/CLI

```cpp
BlockDefinition^ GetBlockDefinition(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:

## VBA Syntax

See [DrawingDoc::GetBlockDefinition](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetBlockDefinition.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
