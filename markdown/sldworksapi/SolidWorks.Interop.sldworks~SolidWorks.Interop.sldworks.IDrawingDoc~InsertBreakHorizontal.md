---
title: "InsertBreakHorizontal Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertBreakHorizontal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakHorizontal.html"
---

# InsertBreakHorizontal Method (IDrawingDoc)

Inserts a horizontal break in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertBreakHorizontal()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.InsertBreakHorizontal()
```

### C#

```csharp
void InsertBreakHorizontal()
```

### C++/CLI

```cpp
void InsertBreakHorizontal();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::InsertBreakHorizontal](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertBreakHorizontal.html).

## Remarks

To create the break view, use [IDrawingDoc::BreakView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~BreakView.html).

You can:

- Customize the break by dragging and repositioning the break lines.
- Set the font of the break lines using [IBreakLine::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBreakLine~Style.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::UnInsertBreakVertical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakVertical.html)
[IDrawingDoc::UnBreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnBreakView.html)
[IDrawingDoc::BreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView.html)
