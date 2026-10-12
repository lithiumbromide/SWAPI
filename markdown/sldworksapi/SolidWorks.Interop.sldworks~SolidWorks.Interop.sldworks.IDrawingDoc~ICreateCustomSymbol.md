---
title: "ICreateCustomSymbol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ICreateCustomSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCustomSymbol.html"
---

# ICreateCustomSymbol Method (IDrawingDoc)

Obsolete. Superseded by [ISkethcManager::MakeSketchBlockFromFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.html), [ISketchManager::MakeSketchBlockSelected](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.html), and [ISketchManager::MakeSketchBlockFromSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateCustomSymbol( _
   ByVal SegmentCount As System.Integer, _
   ByRef Segments As SketchSegment, _
   ByVal PointCount As System.Integer, _
   ByRef Points As SketchPoint, _
   ByVal NoteCount As System.Integer, _
   ByRef Notes As Note _
) As CustomSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim SegmentCount As System.Integer
Dim Segments As SketchSegment
Dim PointCount As System.Integer
Dim Points As SketchPoint
Dim NoteCount As System.Integer
Dim Notes As Note
Dim value As CustomSymbol

value = instance.ICreateCustomSymbol(SegmentCount, Segments, PointCount, Points, NoteCount, Notes)
```

### C#

```csharp
CustomSymbol ICreateCustomSymbol(
   System.int SegmentCount,
   ref SketchSegment Segments,
   System.int PointCount,
   ref SketchPoint Points,
   System.int NoteCount,
   ref Note Notes
)
```

### C++/CLI

```cpp
CustomSymbol^ ICreateCustomSymbol(
   System.int SegmentCount,
   SketchSegment^% Segments,
   System.int PointCount,
   SketchPoint^% Points,
   System.int NoteCount,
   Note^% Notes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SegmentCount`:
- `Segments`:
- `PointCount`:
- `Points`:
- `NoteCount`:
- `Notes`:

## VBA Syntax

See [DrawingDoc::ICreateCustomSymbol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ICreateCustomSymbol.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
