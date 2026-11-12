---
title: "View::GetDimensionInfo5"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionInfo5.htm"
---

# View::GetDimensionInfo5

This method is obsolete and has been superseded by [View::GetDimensionInfo6](sldworksAPI.chm::/View/View__GetDimensionInfo6.htm).

Description

This method gets all of the dimension information in the view. All values returned are in meters.

Syntax (OLE Automation)

retval = View.GetDimensionInfo5 ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the dimension information |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionInfo5 ( retval )

| Output: | (double*) retval | Pointer to an array of doubles containing the dimension information |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For COM implementation, use View::GetDimensionCount4 to determine the overall size of the array needed. The maximum number of doubles contained in the array will be (1 + dimensionCount * 51).

The data returned is an array of doubles as follows:

[ dimensionCount, [ dimensionType, LineStyleIndex, LineWidth, Color, LayerID, LayerOverride, refPoint1a[3], refPoint1b[3], refPoint2a[3], refPoint2b[3], refPoint3[3], textPoint[3], textDirection[3], dimNormal[3], angularDimInfo[9], precision, arrowLength, arrowHeadWidth, arrowHeadHeight, arrowHeadStyle, witnessGap, witnessExt, dimValue, textHeight, arrowsOut, isDiameter, RadialDimensionflags ] ]

where:

dimensionCount = the number of dimensions found in the drawing view

For each dimension, you have a repeating set of the following data:

dimensionType = returns 0 = Linear, 1 = Angular, 2 = Radial, 3 = Ordinate.

LineStyleIndex = line style. Valid line styles as defined in swLineStyles_e.

LineWidth = integer value defining the line width. Valid width values as defined in swLineWeights_e.

Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

LayerID = integer value indicating which layer holds this entity. This integer value is the array index value into the layerList array. Obtain the layerList array using LayerMgr::GetLayerList. A value of –1 indicates that this item is not on a layer.

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

refPoint1a[3] = array of three doubles.

refPoint1b[3] = array of three doubles.

refPoint2a[3] = array of three doubles.

refPoint2b[3] = array of three doubles.

refPoint3[3] = array of three doubles.

textPoint[3] = array of three doubles. This is the upper-left corner of the dimension bounding box.

textDirection[3] = array of three doubles

dimNormal[3] = array of three doubles

angularDimInfo[9] This data is only returned for angular dimensions. The array of 9 values is as follows:

quadrant = as defined in swQuadant_e.

directionLine1[3] = array of three doubles.

directionLine2[3] = array of three doubles.

isInteriorAngle = BOOLEAN returned as a double. TRUE if it is an interior angle.

isFlipped = BOOLEAN returned as a double. TRUE if it is flipped.

precision = number of decimal places.

arrowLength = arrow length.

arrowHeadWidth = arrowhead width.

arrowHeadHeight = arrowhead height.

arrowHeadStyle = arrowhead style as defined in swArrowStyle_e.

witnessGap = extension gap.

witnessExt = extension's extension.

dimValue = dimension value.

textHeight = dimension text height.

arrowsOut = BOOLEAN returned as a double and is TRUE if the arrows are outside.

isDiameter = BOOLEAN returned as a double and is used by radial dimensions. If this value is TRUE, then the dimValue returned is the diameter value; if FALSE, then the dimValue returned is the radial value.

RadialDimensionflags = bit code defining properties for radial dimensions or 0 if the dimension is not radial. See RadialDimensionFlags.
