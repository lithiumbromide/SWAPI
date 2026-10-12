---
title: "CreateCompoundNote Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateCompoundNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCompoundNote.html"
---

# CreateCompoundNote Method (IDrawingDoc)

Obsolete for documents created in SOLIDWORKS 2016 and later. Superseded by [ISketchBlockDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html) and [ISketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html). Creates and returns a compound note.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCompoundNote( _
   ByVal Height As System.Double, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Height As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.CreateCompoundNote(Height, X, Y, Z)
```

### C#

```csharp
System.object CreateCompoundNote(
   System.double Height,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ CreateCompoundNote(
   System.double Height,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Height`: Note height in meters
- `X`: x location of note in meters
- `Y`: y location of note in meters
- `Z`: z location of note in meters

### Return Value

Newly created compound note

## VBA Syntax

See [DrawingDoc::CreateCompoundNote](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateCompoundNote.html).

## Examples

[Create Compound Note (VBA)](Create_Compound_Note_Example_VB.htm)

## Remarks

A compound note is a note that can contain multiple text strings and sketch geometry.

Compound notes are equivalent to a user-defined symbol. After creating a compound note, you can use the other compound note methods to add text and sketch geometry to the object.

This object appears to the end-user as though it were one item. If the user selects the compound note and drags it, all of the entities and text move together.

Because a compound note can have multiple pieces of text, many of the compound note methods require that you specify the index value of the text. For example, the first piece of text added to the compound note using [INote::AddText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~AddText.html) has index number 1, the second text added has index number 2, and so on.

SOLIDWORKS adds the note to the view of the current selection, so you must make a selection before you call this method.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ICreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCompoundNote.html)
[IDrawingDoc::InsertRevisionSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol.html)
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.html)
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.html)
[IDrawingDoc::InsertNewNote2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.html)
[IDrawingDoc::NewNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewNote.html)
