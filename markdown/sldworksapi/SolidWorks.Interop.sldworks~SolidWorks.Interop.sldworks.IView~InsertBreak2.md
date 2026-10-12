---
title: "InsertBreak2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertBreak2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak2.html"
---

# InsertBreak2 Method (IView)

Obsolete. Superseded by [IView::InsertBreak3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBreak2( _
   ByVal Orientation As System.Integer, _
   ByVal Position1 As System.Double, _
   ByVal Position2 As System.Double, _
   ByVal Style As System.Integer, _
   ByVal ShapeIntensity As System.Integer _
) As BreakLine
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Orientation As System.Integer
Dim Position1 As System.Double
Dim Position2 As System.Double
Dim Style As System.Integer
Dim ShapeIntensity As System.Integer
Dim value As BreakLine

value = instance.InsertBreak2(Orientation, Position1, Position2, Style, ShapeIntensity)
```

### C#

```csharp
BreakLine InsertBreak2(
   System.int Orientation,
   System.double Position1,
   System.double Position2,
   System.int Style,
   System.int ShapeIntensity
)
```

### C++/CLI

```cpp
BreakLine^ InsertBreak2(
   System.int Orientation,
   System.double Position1,
   System.double Position2,
   System.int Style,
   System.int ShapeIntensity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Orientation`: Horizontal or vertical cut as defined in [swBreakLineOrientation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineOrientation_e.html)
- `Position1`: Location of the first line in the break (see Remarks)
- `Position2`: Location of the second line in the break (see Remarks)
- `Style`: Break line style as defined in [swBreakLineStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineStyle_e.html)
- `ShapeIntensity`: Shape intensity for jagged cut break lines only; valid range is 1 (most) through 5 (least)

### Return Value

[Break line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)

## VBA Syntax

See [View::InsertBreak2](ms-its:sldworksapivb6.chm::/sldworks~View~InsertBreak2.html).

## Remarks

A break in a drawing view consists of a pair of break lines. This method inserts the break lines at the locations indicated by Position1 and Position2.

| If the orientation of the break is... | Then Position1 and Position2 are... |
| --- | --- |
| Horizontal | Y values relative to the drawing view origin, indicating where along the Y axis to place the breaks |
| Vertical | X values relative to the drawing view origin, indicating where along the X axis to place the breaks |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBreakLineCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount2.html)
[IView::GetBreakLineInfo2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo2.html)
[IView::GetBreakLines Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.html)
[IView::IsBroken Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsBroken.html)
[IView::BreakLineGap Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.html)
[IDrawingDoc::BreakView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
