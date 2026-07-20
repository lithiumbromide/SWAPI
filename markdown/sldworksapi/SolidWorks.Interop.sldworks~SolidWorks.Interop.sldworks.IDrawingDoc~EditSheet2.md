---
title: "EditSheet2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "EditSheet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet2.html"
---

# EditSheet2 Method (IDrawingDoc)

Puts the current drawing sheet in edit mode.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditSheet2()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.EditSheet2()
```

### C#

```csharp
void EditSheet2()
```

### C++/CLI

```cpp
void EditSheet2();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[DrawingDoc::EditSheet2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~EditSheet2.html)

.

## Examples

[Place Note Behind Drawing Sheet (VBA)](Place_Note_Behind_Drawing_Sheet_Example_VB.htm)

[Place Note Behind Drawing Sheet (VB.NET)](Place_Note_Behind_Drawing_Sheet_Example_VBNET.htm)

[Place Note Behind Drawing Sheet (C#)](Place_Note_Behind_Drawing_Sheet_Example_CSharp.htm)

## Remarks

The drawing sheet in edit mode ensures graphics updates and contains all subsequently created geometry.

You can use this method with[IDrawingDoc::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditSketch.html)or[IDrawingDoc::EditTemplate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditTemplate.html). Use[IDrawingDoc::GetEditSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetEditSheet.html)to determine the current state.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)

[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)

## Availability

SOLIDWORKS 2024 SP02, Revision Number 32.2
