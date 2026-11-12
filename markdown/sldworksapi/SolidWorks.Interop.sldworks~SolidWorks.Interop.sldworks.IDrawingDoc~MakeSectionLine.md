---
title: "MakeSectionLine Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "MakeSectionLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~MakeSectionLine.html"
---

# MakeSectionLine Method (IDrawingDoc)

Makes a section line from a set of connected sketch lines.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MakeSectionLine()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.MakeSectionLine()
```

### C#

```csharp
void MakeSectionLine()
```

### C++/CLI

```cpp
void MakeSectionLine();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::MakeSectionLine](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~MakeSectionLine.html).

## Remarks

You must create the sketch lines in the drawing view, not on the drawing sheet.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrawingDoc::FlipSectionLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~FlipSectionLine.html)
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.html)
