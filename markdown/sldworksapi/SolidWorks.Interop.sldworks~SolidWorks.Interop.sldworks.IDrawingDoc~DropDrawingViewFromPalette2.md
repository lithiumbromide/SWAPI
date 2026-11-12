---
title: "DropDrawingViewFromPalette2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "DropDrawingViewFromPalette2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette2.html"
---

# DropDrawingViewFromPalette2 Method (IDrawingDoc)

Moves the specified drawing view from the View Palette to the current drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function DropDrawingViewFromPalette2( _
   ByVal PaletteViewName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim PaletteViewName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As View

value = instance.DropDrawingViewFromPalette2(PaletteViewName, X, Y, Z)
```

### C#

```csharp
View DropDrawingViewFromPalette2(
   System.string PaletteViewName,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
View^ DropDrawingViewFromPalette2(
   System.String^ PaletteViewName,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PaletteViewName`: Name of the drawing view to move to the drawing sheet
- `X`: x coordinate where to drop the drawing view
- `Y`: y coordinate where to drop the drawing view
- `Z`: z coordinate where to drop the drawing view; this coordinate is always 0

### Return Value

[View](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [DrawingDoc::DropDrawingViewFromPalette2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~DropDrawingViewFromPalette2.html).

## Examples

[Drop Drawing Views from View Palette (VBA)](Drop_Drawing_Views_from_View_Palette_Example_VB.htm)
[Drop First Drawing View from View Palette (VBA)](Drop_First_Drawing_View_from_View_Palette_Example_VB.htm)
[Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (C#)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm)
[Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm)
[Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VBA)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VB.htm)

## Remarks

The x, y, and z coordinates are in paper space. Thus, the drawing sheet scale is irrelevant.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GenerateViewPaletteViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GenerateViewPaletteViews.html)
[IDrawingDoc::GetDrawingPaletteViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetDrawingPaletteViewNames.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
