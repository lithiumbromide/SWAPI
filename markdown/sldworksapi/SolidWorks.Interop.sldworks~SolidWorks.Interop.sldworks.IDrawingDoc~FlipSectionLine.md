---
title: "FlipSectionLine Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "FlipSectionLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~FlipSectionLine.html"
---

# FlipSectionLine Method (IDrawingDoc)

Flips the cut direction of the selected section line.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FlipSectionLine()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.FlipSectionLine()
```

### C#

```csharp
void FlipSectionLine()
```

### C++/CLI

```cpp
void FlipSectionLine();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::FlipSectionLine](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~FlipSectionLine.html).

## Remarks

SOLIDWORKS creates the corresponding section view, if one exists, on the next rebuild.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.html)
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html)
[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
