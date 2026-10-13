---
title: "IInsertMultiJogLeader3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IInsertMultiJogLeader3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertMultiJogLeader3.html"
---

# IInsertMultiJogLeader3 Method (IDrawingDoc)

Inserts a multi-jog leader.

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertMultiJogLeader3( _
   ByVal PointsCount As System.Integer, _
   ByRef Points As MathPoint, _
   ByVal StartPointArrowStyle As System.Integer, _
   ByVal EndPointArrowStyle As System.Integer _
) As MultiJogLeader
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim PointsCount As System.Integer
Dim Points As MathPoint
Dim StartPointArrowStyle As System.Integer
Dim EndPointArrowStyle As System.Integer
Dim value As MultiJogLeader

value = instance.IInsertMultiJogLeader3(PointsCount, Points, StartPointArrowStyle, EndPointArrowStyle)
```

### C#

```csharp
MultiJogLeader IInsertMultiJogLeader3(
   System.int PointsCount,
   ref MathPoint Points,
   System.int StartPointArrowStyle,
   System.int EndPointArrowStyle
)
```

### C++/CLI

```cpp
MultiJogLeader^ IInsertMultiJogLeader3(
   System.int PointsCount,
   MathPoint^% Points,
   System.int StartPointArrowStyle,
   System.int EndPointArrowStyle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointsCount`: Number of points
- `Points`: Array of [points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of size PointsCount
- `StartPointArrowStyle`: Starting point's arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)
- `EndPointArrowStyle`: Ending point's arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

### Return Value

Pointer to the newly created [multi-jog leader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader.html)

## VBA Syntax

See [DrawingDoc::IInsertMultiJogLeader3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IInsertMultiJogLeader3.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::InsertMultiJogLeader3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertMultiJogLeader3.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
