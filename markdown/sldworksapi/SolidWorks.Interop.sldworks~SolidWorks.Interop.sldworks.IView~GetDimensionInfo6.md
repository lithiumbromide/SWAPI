---
title: "GetDimensionInfo6 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDimensionInfo6"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.html"
---

# GetDimensionInfo6 Method (IView)

Obsolete. Superseded by [IView::GetDimensionInfo7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo7.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimensionInfo6() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDimensionInfo6()
```

### C#

```csharp
System.object GetDimensionInfo6()
```

### C++/CLI

```cpp
System.Object^ GetDimensionInfo6();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::GetDimensionInfo6](ms-its:sldworksapivb6.chm::/sldworks~View~GetDimensionInfo6.html).

## Remarks

The data returned is an array of doubles as follows:

[ dimensionCount, [ dimensionType, LineStyleIndex, LineWidth, Color, LayerID, LayerOverride, refPoint1a[3], refPoint1b[3], refPoint2a[3], refPoint2b[3], refPoint3[3], textPoint[3], textDirection[3], dimNormal[3], angularDimInfo[9], precision, arrowLength, arrowHeadWidth, arrowHeadHeight, arrowHeadStyle, witnessGap, witnessExt, dimValue, textHeight, arrowsOut, isDiameter, RadialDimensionflags ] ]

where:

dimensionCount = number of dimensions found in the drawing view

For each dimension, you have a repeating set of the following data:

dimensionType = returns 0 = Linear, 1 = Angular, 2 = Radial, 3 = Ordinate

LineStyleIndex = line style; valid line styles as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

LineWidth = integer value defining the line width; valid width values as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

Color = COLORREF returned as an integer; return value could be 0 or -1 for default color

LayerID = integer value indicating which layer holds this entity; this integer value is the array index value into the layerList array; obtain the layerList array using [ILayerMgr::GetLayerList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerList.html) or [ILayerMgr::IGetLayerList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerList.html); a value of 1 indicates that this item is not on a layer

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) default properties; if the bit value is set, then the specific property or properties have been overridden; the bit indicators are: color = 0x1, style = 0x2, and width = 0x4; therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer

refPoint1a[3] = array of three doubles

refPoint1b[3] = array of three doubles

refPoint2a[3] = array of three doubles

refPoint2b[3] = array of three doubles

refPoint3[3] = array of three doubles

textPoint[3] = array of three doubles; this is the upper-left corner of the dimension bounding box

textDirection[3] = array of three doubles

dimNormal[3] = array of three doubles

angularDimInfo[9] This data is only returned for angular dimensions; the array of 9 values is as follows:

quadrant = as defined in [swQuadant_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swQuadant_e.html)

directionLine1[3] = array of three doubles

directionLine2[3] = array of three doubles

isInteriorAngle = BOOLEAN returned as a double; true if it is an interior angle

isFlipped = BOOLEAN returned as a double; true if it is flipped

precision = number of decimal places

arrowLength = arrow length

arrowHeadWidth = arrowhead width

arrowHeadHeight = arrowhead height

arrowHeadStyle = arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

witnessGap = extension gap

witnessExt = extension's extension

dimValue = dimension value

textHeight = dimension text height

arrowsOut = BOOLEAN returned as a double and is true if the arrows are outside

isDiameter = BOOLEAN returned as a double and is used by radial dimensions; if this value is true, then the dimValue returned is the diameter value, if false, then the dimValue returned is the radial value

RadialDimensionflags = bit code defining properties for radial dimensions or 0 if the dimension is not radial. This element contains a bitwise OR of the following values:

RADIAL_INSIDE - Specifies that the arrows of the radial dimension are displayed inside the arc/circle.

RADIAL_2ND_ARROW - Specifies that there should be two outside arrows displayed with the radial dimension.

RADIAL_SOLID_LEADER - Specifies that the leader line should be drawn in solid.

RADIAL_CALLOUT - Specifies that there should be text displayed with the dimension.

RADIAL_IS_RADIAL - Specifies that the leader line should remain radial.

RADIAL_IS_BENT - Specifies that the leader line should be bent at the end.

RADIAL_IS_LINEAR - Specifies that the leader line should be straight at the end.

RADIAL_DOC_2ND_ARROW - Specifies that there should be two outside document arrows displayed with the radial dimension.

RADIAL_HAS_SNAPPED_DIR - Specifies that the arrow should snap to the grid.

The maximum number of doubles contained in the array will be (1 + dimensionCount * 51).

This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDimensionCount4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionCount4.html)
[IView::GetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfo5.html)
[IView::GetDimensionDisplayInfoSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.html)
[IView::GetDimensionDisplayString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString4.html)
[IView::GetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.html)
[IView::GetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.html)
[IView::GetFirstDisplayDimension5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.html)
[IView::IGetDimensionDisplayInfo5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayInfo5.html)
[IView::IGetDimensionDisplayString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionDisplayString4.html)
[IView::IGetDimensionIds4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionIds4.html)
[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.html)
[IView::IGetDimensionString4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionString4.html)
[IView::ProjectedDimensions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.html)
