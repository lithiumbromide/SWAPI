---
title: "InsertMultiJogLeader3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertMultiJogLeader3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertMultiJogLeader3.html"
---

# InsertMultiJogLeader3 Method (IDrawingDoc)

Inserts a multi-jog leader.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMultiJogLeader3( _
   ByVal Points As System.Object, _
   ByVal StartPointArrowStyle As System.Integer, _
   ByVal EndPointArrowStyle As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Points As System.Object
Dim StartPointArrowStyle As System.Integer
Dim EndPointArrowStyle As System.Integer
Dim value As System.Object

value = instance.InsertMultiJogLeader3(Points, StartPointArrowStyle, EndPointArrowStyle)
```

### C#

```csharp
System.object InsertMultiJogLeader3(
   System.object Points,
   System.int StartPointArrowStyle,
   System.int EndPointArrowStyle
)
```

### C++/CLI

```cpp
System.Object^ InsertMultiJogLeader3(
   System.Object^ Points,
   System.int StartPointArrowStyle,
   System.int EndPointArrowStyle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Points`: Array of [points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of size PointsCount
- `StartPointArrowStyle`: Starting point's arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)
- `EndPointArrowStyle`: Ending point's arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

### Return Value

Newly created multi-jog leader

## VBA Syntax

See [DrawingDoc::InsertMultiJogLeader3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertMultiJogLeader3.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::IInsertMultiJogLeader3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertMultiJogLeader3.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
