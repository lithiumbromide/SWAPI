---
title: "InsertBreakVertical Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertBreakVertical"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakVertical.html"
---

# InsertBreakVertical Method (IDrawingDoc)

Inserts a vertical break in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertBreakVertical()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.InsertBreakVertical()
```

### C#

```csharp
void InsertBreakVertical()
```

### C++/CLI

```cpp
void InsertBreakVertical();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::InsertBreakVertical](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertBreakVertical.html).

## Remarks

To create the break view, use [IDrawingDoc::BreakView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~BreakView.html).

You can:

- Customize the break by dragging and repositioning the break lines.
- Set the font of the break lines using [IBreakLine::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBreakLine~Style.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::UnBreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnBreakView.html)
[IDrawingDoc::InsertBreakHorizontal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBreakHorizontal.html)
[IDrawingDoc::BreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView.html)
