---
title: "EditSketch Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "EditSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSketch.html"
---

# EditSketch Method (IDrawingDoc)

Allows editing of a sketch in the selected drawing view or sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditSketch()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.EditSketch()
```

### C#

```csharp
void EditSketch()
```

### C++/CLI

```cpp
void EditSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::EditSketch](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~EditSketch.html).

## Remarks

Creating subsequent geometry resides in this drawing view or sheet.

If you selected a drawing view and called IDrawingDoc::EditSketch, then you can resume editing the drawing sheet by calling [IDrawingDoc::EditSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditSheet.html) or by selecting the sheet and calling IDrawingDoc::EditSketch again.

To determine the current state, use [IDrawingDoc::GetEditSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetEditSheet.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
