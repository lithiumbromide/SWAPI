---
title: "TranslateDrawing Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "TranslateDrawing"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~TranslateDrawing.html"
---

# TranslateDrawing Method (IDrawingDoc)

Translates the entire drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub TranslateDrawing( _
   ByVal DeltaX As System.Double, _
   ByVal DeltaY As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim DeltaX As System.Double
Dim DeltaY As System.Double

instance.TranslateDrawing(DeltaX, DeltaY)
```

### C#

```csharp
void TranslateDrawing(
   System.double DeltaX,
   System.double DeltaY
)
```

### C++/CLI

```cpp
void TranslateDrawing(
   System.double DeltaX,
   System.double DeltaY
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DeltaX`: Delta X value for the translation operation
- `DeltaY`: Delta Y value for the translation operation

## VBA Syntax

See [DrawingDoc::TranslateDrawing](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~TranslateDrawing.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
