---
title: "ICreateBlockDefinition Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateBlockDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateBlockDefinition.html"
---

# ICreateBlockDefinition Method (IDrawingDoc)

Obsolete. Superseded by [ISketchManager::MakeSketchBlockFromFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.html), [ISketchManager::MakeSketchBlockSelected](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.html), and [ISketchManager::MakeSketchBlockFromSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBlockDefinition( _
   ByVal Name As System.String, _
   ByVal XRefFileName As System.String, _
   ByVal Instance As System.Boolean, _
   ByVal SegmentCount As System.Integer, _
   ByRef Segments As SketchSegment, _
   ByVal PointCount As System.Integer, _
   ByRef Points As SketchPoint, _
   ByVal NoteCount As System.Integer, _
   ByRef Notes As Note, _
   ByVal DimensionCount As System.Integer, _
   ByRef Dimensions As DisplayDimension, _
   ByVal BlockCount As System.Integer, _
   ByRef Blocks As BlockInstance _
) As BlockDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Name As System.String
Dim XRefFileName As System.String
Dim Instance As System.Boolean
Dim SegmentCount As System.Integer
Dim Segments As SketchSegment
Dim PointCount As System.Integer
Dim Points As SketchPoint
Dim NoteCount As System.Integer
Dim Notes As Note
Dim DimensionCount As System.Integer
Dim Dimensions As DisplayDimension
Dim BlockCount As System.Integer
Dim Blocks As BlockInstance
Dim value As BlockDefinition

value = instance.ICreateBlockDefinition(Name, XRefFileName, Instance, SegmentCount, Segments, PointCount, Points, NoteCount, Notes, DimensionCount, Dimensions, BlockCount, Blocks)
```

### C#

```csharp
BlockDefinition ICreateBlockDefinition(
   System.string Name,
   System.string XRefFileName,
   System.bool Instance,
   System.int SegmentCount,
   ref SketchSegment Segments,
   System.int PointCount,
   ref SketchPoint Points,
   System.int NoteCount,
   ref Note Notes,
   System.int DimensionCount,
   ref DisplayDimension Dimensions,
   System.int BlockCount,
   ref BlockInstance Blocks
)
```

### C++/CLI

```cpp
BlockDefinition^ ICreateBlockDefinition(
   System.String^ Name,
   System.String^ XRefFileName,
   System.bool Instance,
   System.int SegmentCount,
   SketchSegment^% Segments,
   System.int PointCount,
   SketchPoint^% Points,
   System.int NoteCount,
   Note^% Notes,
   System.int DimensionCount,
   DisplayDimension^% Dimensions,
   System.int BlockCount,
   BlockInstance^% Blocks
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `XRefFileName`:
- `Instance`:
- `SegmentCount`:
- `Segments`:
- `PointCount`:
- `Points`:
- `NoteCount`:
- `Notes`:
- `DimensionCount`:
- `Dimensions`:
- `BlockCount`:
- `Blocks`:

## VBA Syntax

See [DrawingDoc::ICreateBlockDefinition](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateBlockDefinition.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
