---
title: "GenerateViewPaletteViews Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GenerateViewPaletteViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GenerateViewPaletteViews.html"
---

# GenerateViewPaletteViews Method (IDrawingDoc)

Adds the specified document's predefined drawing views to the View Palette.

## Syntax

### Visual Basic (Declaration)

```vb
Function GenerateViewPaletteViews( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim FileName As System.String
Dim value As System.Boolean

value = instance.GenerateViewPaletteViews(FileName)
```

### C#

```csharp
System.bool GenerateViewPaletteViews(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool GenerateViewPaletteViews(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name of the document from which to add the predefined drawing views to the View Palette

### Return Value

True if the drawing views are added to the View Palette, false if not

## VBA Syntax

See [DrawingDoc::GenerateViewPaletteViews](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GenerateViewPaletteViews.html).

## Examples

[Get and Set Whether to Hide Cutting Line Shoulders (C#)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_CSharp.htm)
[Get and Set Whether to Hide Cutting Line Shoulders (VB.NET)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VBNET.htm)
[Get and Set Whether to Hide Cutting Line Shoulders (VBA)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::DropDrawingViewFromPalette2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette2.html)
[IDrawingDoc::GetDrawingPaletteViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetDrawingPaletteViewNames.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
