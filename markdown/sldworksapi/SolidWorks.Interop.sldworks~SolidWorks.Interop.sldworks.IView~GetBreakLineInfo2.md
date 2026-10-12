---
title: "GetBreakLineInfo2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBreakLineInfo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo2.html"
---

# GetBreakLineInfo2 Method (IView)

Gets information for all of the break lines in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBreakLineInfo2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetBreakLineInfo2()
```

### C#

```csharp
System.object GetBreakLineInfo2()
```

### C++/CLI

```cpp
System.Object^ GetBreakLineInfo2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of data for all break lines in the view (see **Remarks**)

## VBA Syntax

See [View::GetBreakLineInfo2](ms-its:sldworksapivb6.chm::/sldworks~View~GetBreakLineInfo2.html).

## Examples

[Get Break Line Data (VBA)](Get_Break_Line_Data_Example_VB.htm)
[Get Break Line Data (VB.NET)](Get_Break_Line_Data_Example_VBNET.htm)
[Get Break Line Data (C#)](Get_Break_Line_Data_Example_CSharp.htm)

## Remarks

The return value is a one-dimensional array consisting of the following data:

[ breaklineStyle, color, lineType, lineStyleIndex, lineWeight, layerId,

layerOverride, numLines, numArcs, numSplines, [break line data] ]

where:

| breaklineStyle | Break line style as defined in swBreakLineStyle_e |
| --- | --- |
| color | COLORREF returned as an integer; 0 or -1 for default color |
| lineType | Line type as defined in swLineTypes_e ; lineType is a combination of a lineStyle and lineWeight |
| lineStyleIndex | Line style as defined in swLineStyles_e |
| lineWeight | Line width as defined in swLineWeights_e |
| layerId | An integer value indicating which layer holds this entity; ILayer can be obtained by passing this integer value to ILayerMgr::GetLayerById and ILayerMgr::IGetLayerId |
| layerOverride | An integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. Valid bit values as defined in swLayerOverride_e : color = 0x1 style = 0x2 width = 0x4 Therefore, if LayerOverride is returned as 3, then the color and style are specifically set for this item and may not match the default values associated with this item's layer. |
| numLines | Number of line segments if a straight or zig zag break |
| numArcs | Number of arc lines if a curve break |
| numSplines | Number of spline lines if a jagged break |

| If the break line style is swBreakLineStyle_e... | Then [ break line data ] is packed with... |
| --- | --- |
| swBreakLine_Straight | 12 doubles (2 lines * 1 segment * 2 points * 3 coordinates) |
| swBreakLine_ZigZag | 60 doubles (2 lines * 5 segments * 2 points * 3 coordinates) |
| swBreakLine_SmallZigZag | 60 doubles (2 lines * 5 segments * 2 points * 3 coordinates) |
| swBreakLine_Curve | for each arc line in the break: arc direction (1 double) start point (3 doubles) end point (3 doubles) center point (3 doubles) |
| swBreakLine_Jagged | for each spline line in the break: n (1 integer) 3* n doubles ( n points * 3 coordinates) where: n is the number of spline points generated based on the jagged cut shape intensity selected by the user in the Break View Property Manager |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetBreakLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLineInfo2.html)
[IView::GetBreakLineCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount2.html)
[IView::GetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.html)
[IView::IGetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLines.html)
[IView::IsBroken Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsBroken.html)
[IView::BreakLineGap Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.html)
[IView::InsertBreak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
