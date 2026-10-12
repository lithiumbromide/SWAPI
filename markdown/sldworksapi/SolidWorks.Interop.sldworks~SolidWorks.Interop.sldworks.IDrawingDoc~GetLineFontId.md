---
title: "GetLineFontId Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetLineFontId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontId.html"
---

# GetLineFontId Method (IDrawingDoc)

Gets the associated line font ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineFontId( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetLineFontId(Index)
```

### C#

```csharp
System.int GetLineFontId(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetLineFontId(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index position of the line font which is within the index range returned by [IDrawingDoc::GetLineFontCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetLineFontCount2.html)

### Return Value

Line font ID

## VBA Syntax

See [DrawingDoc::GetLineFontId](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetLineFontId.html).

## Remarks

SOLIDWORKS uses the line font ID to represent specific line fonts whose names are, for example, Visible, Hidden, Sketch, and so on.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetLineFontName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.html)
[IDrawingDoc::GetLineFontInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.html)
[IDrawingDoc::SetLineColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineColor.html)
[IDrawingDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineStyle.html)
[IDrawingDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidth.html)
[IDrawingDoc::GetLineFontCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontCount2.html)
