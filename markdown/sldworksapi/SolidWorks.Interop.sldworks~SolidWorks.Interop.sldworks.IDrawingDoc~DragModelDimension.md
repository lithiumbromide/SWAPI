---
title: "DragModelDimension Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "DragModelDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DragModelDimension.html"
---

# DragModelDimension Method (IDrawingDoc)

Copies or moves dimensions to a different drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DragModelDimension( _
   ByVal ViewName As System.String, _
   ByVal DropEffect As System.Short, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ViewName As System.String
Dim DropEffect As System.Short
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.DragModelDimension(ViewName, DropEffect, X, Y, Z)
```

### C#

```csharp
void DragModelDimension(
   System.string ViewName,
   System.short DropEffect,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void DragModelDimension(
   System.String^ ViewName,
   System.short DropEffect,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`: Name of the drawing view to which you want to copy or move the selected model dimension
- `DropEffect`: - Copy = 1
  - Move = 2
- `X`: X location in sheet space for the newly copied or moved dimension
- `Y`: Y location in sheet space for the newly copied or moved dimension
- `Z`: Z location in sheet space for the newly copied or moved dimension; set to 0

### Return Value

The ViewName argument cannot be the current view for the dimension.

## VBA Syntax

See [DrawingDoc::DragModelDimension](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~DragModelDimension.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.html)
