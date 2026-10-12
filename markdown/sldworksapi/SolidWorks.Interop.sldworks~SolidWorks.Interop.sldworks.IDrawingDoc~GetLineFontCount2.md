---
title: "GetLineFontCount2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetLineFontCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontCount2.html"
---

# GetLineFontCount2 Method (IDrawingDoc)

Gets the a number line fonts supported by this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineFontCount2() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Integer

value = instance.GetLineFontCount2()
```

### C#

```csharp
System.int GetLineFontCount2()
```

### C++/CLI

```cpp
System.int GetLineFontCount2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of line fonts supported by this drawing

## VBA Syntax

See [DrawingDoc::GetLineFontCount2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetLineFontCount2.html).

## Remarks

Each line font is identified by an index in the range [0, (retval -1) ].

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetLineFontId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontId.html)
[IDrawingDoc::GetLineFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo.html)
[IDrawingDoc::GetLineFontName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.html)
[IDrawingDoc::SetLineColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineColor.html)
[IDrawingDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineStyle.html)
[IDrawingDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidth.html)
