---
title: "BreakView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "BreakView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView.html"
---

# BreakView Method (IDrawingDoc)

Breaks the drawing view along the existing break lines.

## Syntax

### Visual Basic (Declaration)

```vb
Sub BreakView()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.BreakView()
```

### C#

```csharp
void BreakView()
```

### C++/CLI

```cpp
void BreakView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::BreakView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~BreakView.html).

## Examples

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

## Remarks

Use [IDrawingDoc::InsertBreakHorizontal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertBreakHorizontal.html) or [IDrawingDoc::InsertBreakVertical](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertBreakVertical.html) to insert break lines to a drawing view. Customize the break by dragging and repositioning the break lines. Then, call this method to create the break view.

You can set the font of the break lines using [IBreakLine::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBreakLine~Style.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::InsertBreakHorizontal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakHorizontal.html)
[IDrawingDoc::InsertBreakVertical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakVertical.html)
[IDrawingDoc::UnBreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnBreakView.html)
