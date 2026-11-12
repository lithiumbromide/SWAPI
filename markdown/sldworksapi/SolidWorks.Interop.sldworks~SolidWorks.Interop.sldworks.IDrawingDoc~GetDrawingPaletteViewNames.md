---
title: "GetDrawingPaletteViewNames Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetDrawingPaletteViewNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetDrawingPaletteViewNames.html"
---

# GetDrawingPaletteViewNames Method (IDrawingDoc)

Gets the names of drawing views in the View Palette for the active drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDrawingPaletteViewNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Object

value = instance.GetDrawingPaletteViewNames()
```

### C#

```csharp
System.object GetDrawingPaletteViewNames()
```

### C++/CLI

```cpp
System.Object^ GetDrawingPaletteViewNames();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the names of the drawing views in the View Palette for the active drawing sheet

## VBA Syntax

See [DrawingDoc::GetDrawingPaletteViewNames](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetDrawingPaletteViewNames.html).

## Examples

[Drop Drawing Views from View Palette (VBA)](Drop_Drawing_Views_from_View_Palette_Example_VB.htm)
[Drop First Drawing View from View Palette (VBA)](Drop_Drawing_Views_from_View_Palette_Example_VB.htm)
[Get Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (C#)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm)
[Get Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm)
[Get Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VBA)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VB.htm)

## Remarks

| If... | Then this method... |
| --- | --- |
| a part or assembly was not pre-selected for the View Palette (i.e., the View Palette is empty) | returns an empty array. |
| an end-user moves a drawing view from the View Palette to the drawing sheet (either through the user-interface or via an API) | does not include that drawing name the next time this method is called. |

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::DropDrawingViewFromPalette2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette2.html)
[IDrawingDoc::GenerateViewPaletteViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GenerateViewPaletteViews.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
