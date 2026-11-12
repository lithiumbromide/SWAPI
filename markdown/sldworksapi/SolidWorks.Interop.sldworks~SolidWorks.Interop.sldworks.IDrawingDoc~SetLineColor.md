---
title: "SetLineColor Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SetLineColor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineColor.html"
---

# SetLineColor Method (IDrawingDoc)

Sets the line color for a selected edge or sketch entity.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLineColor( _
   ByVal Color As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Color As System.Integer

instance.SetLineColor(Color)
```

### C#

```csharp
void SetLineColor(
   System.int Color
)
```

### C++/CLI

```cpp
void SetLineColor(
   System.int Color
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Color`: Color definition as a COLORREF

## VBA Syntax

See [DrawingDoc::SetLineColor](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SetLineColor.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetLineFontCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontCount2.html)
[IDrawingDoc::GetLineFontId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontId.html)
[IDrawingDoc::GetLineFontInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.html)
[IDrawingDoc::GetLineFontName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.html)
[IDrawingDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidth.html)
[IDrawingDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineStyle.html)
[IDrawingDoc::SetLineWidthCustom Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidthCustom.html)
