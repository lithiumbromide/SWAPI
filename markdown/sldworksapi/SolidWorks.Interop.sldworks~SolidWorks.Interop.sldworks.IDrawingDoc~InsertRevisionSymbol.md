---
title: "InsertRevisionSymbol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertRevisionSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol.html"
---

# InsertRevisionSymbol Method (IDrawingDoc)

Inserts a revision symbol note in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertRevisionSymbol( _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim value As Note

value = instance.InsertRevisionSymbol(X, Y)
```

### C#

```csharp
Note InsertRevisionSymbol(
   System.double X,
   System.double Y
)
```

### C++/CLI

```cpp
Note^ InsertRevisionSymbol(
   System.double X,
   System.double Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate at which to insert revision symbol note
- `Y`: Y coordinate at which to insert revision symbol note

### Return Value

Pointer to the newly created [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) object

## VBA Syntax

See [DrawingDoc::InsertRevisionSymbol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertRevisionSymbol.html).

## Remarks

To attach the revision symbol to entities in the drawing, the end-user must interactively preselect those entities. The revision symbol is then inserted with leaders to those selected entities. If there are no preselected entities, the symbol is free-standing.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCompoundNote.html)
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.html)
[IDrawingDoc::ICreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCompoundNote.html)
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.html)
[IDrawingDoc::InsertNewNote2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
