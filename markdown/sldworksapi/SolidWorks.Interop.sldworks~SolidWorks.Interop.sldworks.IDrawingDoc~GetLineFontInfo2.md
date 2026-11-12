---
title: "GetLineFontInfo2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetLineFontInfo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.html"
---

# GetLineFontInfo2 Method (IDrawingDoc)

Gets the detailed information about the specified line font.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineFontInfo2( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetLineFontInfo2(Index)
```

### C#

```csharp
System.object GetLineFontInfo2(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetLineFontInfo2(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index position of the line font which is within the index range returned by [IDrawingDoc::GetLineFontCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetLineFontCount2.html)

### Return Value

Array containing the line font information (see **Remarks**)

## VBA Syntax

See [DrawingDoc::GetLineFontInfo2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetLineFontInfo2.html).

## Remarks

This method breaks down the line font into its individual segment lengths.

Lines are repeating patterns of space and solid segments. The segCount argument returns the number of segments that define the pattern, and segLengths[] specifies the length of each segment. A negative length value indicates space.

For example:

Solid line: segCount = 1, segLenghts[] = {0.5}

Dashed line: segCount = 2, segLengths[] = {0.25, -0.25}

VARIANT format:

double segCount - Number of segments in the pattern

double segLengths[segCount] - Length of each segment

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetLineFontId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontId.html)
[IDrawingDoc::GetLineFontName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.html)
[GetLineFontCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontCount2.html)
[IDrawingDoc::SetLineColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineColor.html)
[IDrawingDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineStyle.html)
[IDrawingDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidth.html)
