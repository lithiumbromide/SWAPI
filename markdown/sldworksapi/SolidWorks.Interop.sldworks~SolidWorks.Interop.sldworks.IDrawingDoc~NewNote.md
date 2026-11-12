---
title: "NewNote Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "NewNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewNote.html"
---

# NewNote Method (IDrawingDoc)

Creates a new note at the selected location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub NewNote( _
   ByVal Text As System.String, _
   ByVal Height As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Text As System.String
Dim Height As System.Double

instance.NewNote(Text, Height)
```

### C#

```csharp
void NewNote(
   System.string Text,
   System.double Height
)
```

### C++/CLI

```cpp
void NewNote(
   System.String^ Text,
   System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`: Text string for the note
- `Height`: Height of the note in meters

## VBA Syntax

See [DrawingDoc::NewNote](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~NewNote.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.html)
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.html)
[IDrawingDoc::InsertNewNote2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.html)
[IDrawingDoc::InsertRevisionSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol.html)
[IDrawingDoc::ICreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCompoundNote.html)
[IDrawingDoc::CreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCompoundNote.html)
