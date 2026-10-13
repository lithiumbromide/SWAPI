---
title: "IInsertMultiJogLeader2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IInsertMultiJogLeader2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertMultiJogLeader2.html"
---

# IInsertMultiJogLeader2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::InsertMultiJogLeader3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IInsertMultiJogLeader3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertMultiJogLeader2( _
   ByVal PointsCount As System.Integer, _
   ByRef Points As MathPoint _
) As MultiJogLeader
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim PointsCount As System.Integer
Dim Points As MathPoint
Dim value As MultiJogLeader

value = instance.IInsertMultiJogLeader2(PointsCount, Points)
```

### C#

```csharp
MultiJogLeader IInsertMultiJogLeader2(
   System.int PointsCount,
   ref MathPoint Points
)
```

### C++/CLI

```cpp
MultiJogLeader^ IInsertMultiJogLeader2(
   System.int PointsCount,
   MathPoint^% Points
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointsCount`:
- `Points`:

## VBA Syntax

See [DrawingDoc::IInsertMultiJogLeader2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IInsertMultiJogLeader2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
