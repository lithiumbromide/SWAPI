---
title: "EditSheet Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "EditSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html"
---

# EditSheet Method (IDrawingDoc)

Obsolete. Superseded by

[IDrawingDoc::EditSheet2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet2.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditSheet()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.EditSheet()
```

### C#

```csharp
void EditSheet()
```

### C++/CLI

```cpp
void EditSheet();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[DrawingDoc::EditSheet](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~EditSheet.html)

.

## Remarks

Subsequently created geometry resides on this drawing sheet.

You can use this method with[IDrawingDoc::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditSketch.html)or[IDrawingDoc::EditTemplate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditTemplate.html). Use[IDrawingDoc::GetEditSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetEditSheet.html)to determine the current state.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)

[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
