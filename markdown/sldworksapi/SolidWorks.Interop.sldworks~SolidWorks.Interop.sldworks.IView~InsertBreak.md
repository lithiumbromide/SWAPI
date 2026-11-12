---
title: "InsertBreak Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertBreak"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.html"
---

# InsertBreak Method (IView)

Obsolete. Superseded by [IView::InsertBreak2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBreak( _
   ByVal Orientation As System.Integer, _
   ByVal Position1 As System.Double, _
   ByVal Position2 As System.Double, _
   ByVal Style As System.Integer _
) As BreakLine
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Orientation As System.Integer
Dim Position1 As System.Double
Dim Position2 As System.Double
Dim Style As System.Integer
Dim value As BreakLine

value = instance.InsertBreak(Orientation, Position1, Position2, Style)
```

### C#

```csharp
BreakLine InsertBreak(
   System.int Orientation,
   System.double Position1,
   System.double Position2,
   System.int Style
)
```

### C++/CLI

```cpp
BreakLine^ InsertBreak(
   System.int Orientation,
   System.double Position1,
   System.double Position2,
   System.int Style
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Orientation`: Horizontal or vertical cut as defined in [swBreakLineOrientation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineOrientation_e.html)
- `Position1`: Location of the first line in the break (see Remarks)
- `Position2`: Location of the second line in the break (see Remarks)
- `Style`: Cut style as defined in [swBreakLineStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineStyle_e.html)

### Return Value

[Break line](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBreakLine.html)

## VBA Syntax

See [View::InsertBreak](ms-its:sldworksapivb6.chm::/sldworks~View~InsertBreak.html).

## Remarks

A break in a drawing view consists of a pair of lines. This method inserts the break lines at the locations indicated by Position1 and Position2.

| If the orientation of the break is... | Then Position1 and Position2 are... |
| --- | --- |
| Horizontal | Y values, relative to the drawing view origin, indicating where along the Y axis to place the breaks |
| Vertical | X values, relative to the drawing view origin, indicating where along the X axis to place the breaks |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBreakLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount.html)
[IView::GetBreakLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo.html)
[IView::GetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.html)
[IView::IGetBreakLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLineInfo.html)
[IView::IGetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLines.html)
[IView::BreakLineGap Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.html)
[IView::IsBroken Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsBroken.html)
[IDrawingDoc::BreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView.html)
[IBreakLine::Style Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Style.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
