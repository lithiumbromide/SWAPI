---
title: "Sheet Property (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "Sheet"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Sheet.html"
---

# Sheet Property (IDrawingDoc)

Gets the specified sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Sheet( _
   ByVal Name As System.String _
) As Sheet
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Name As System.String
Dim value As Sheet

value = instance.Sheet(Name)
```

### C#

```csharp
Sheet Sheet(
   System.string Name
) {get;}
```

### C++/CLI

```cpp
property Sheet^ Sheet {
   Sheet^ get(System.String^ Name);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of sheet

### Property Value

[Sheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html)

## VBA Syntax

See [DrawingDoc::Sheet](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~Sheet.html).

## Examples

[Get Sheet in Multi-sheet Drawing (C#)](Get_Sheet_in_Multi-sheet_Drawing_Example_CSharp.htm)
[Get Sheet in Multi-Sheet Drawing (VB.NET)](Get_Sheet_in_Multi-Sheet_Drawing_Example_VBNET.htm)
[Get Sheet in Multi-sheet Drawing (VBA)](Get_Sheet_in_Multi-sheet_Drawing_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
