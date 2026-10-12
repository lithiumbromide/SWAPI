---
title: "View::GetDimensionInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionInfo.htm"
---

# View::GetDimensionInfo

This method is obsolete and has been superseded by [View::GetDimensionInfo2](View__GetDimensionInfo2.htm).

Description

This method returns information about the dimension. All values returned are in meters.

Syntax (OLE Automation)

retval = View.GetDimensionInfo ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the dimension information |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionInfo (retval )

| Output: | (double*) retval | Pointer to an array of doubles containing the dimension information |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For COM implementation, see View::GetDimensionCount to determine the overall size of the array needed. The maximum number of doubles contained in the array will be (1 + dimensionCount * 46).

The data returned is an array of doubles as follows:

[ dimensionCount, [ dimensionType, lineStyle, refPoint1a[3], refPoint1b[3], refPoint2a[3], refPoint2b[3], refPoint3[3], textPoint[3], textDirection[3], dimNormal[3], angularDimInfo[9], precision, arrowLength, arrowHeadWidth, arrowHeadHeight, arrowHeadStyle, witnessGap, witnessExt, dimValue, textHeight, arrowsOut, isDiameter ] ]

where:

dimensionCount = the number of dimensions found in the drawing view

For each dimension, we have a repeating set of the following data:

dimensionType = returns 0 = Linear, 1 = Angular, 2 = Radial, 3 = Ordinate

lineStyle = line style (Dimension Style = 5)

refPoint1a[3] = array of three doubles.

refPoint1b[3] = array of three doubles.

refPoint2a[3] = array of three doubles.

refPoint2b[3] = array of three doubles.

refPoint3[3] = array of three doubles.

textPoint[3] = array of three doubles. This is the upper-left corner of the dimension bounding box.

textDirection[3] = an array of three doubles

dimNormal[3] = an array of three doubles

angularDimInfo[9] = data is only returned for angular dimensions. The array of 9 values is as follows:

quadrant = as defined in swQuadant_e.

directionLine1[3] = array of three doubles.

directionLine2[3] = array of three doubles.

isInteriorAngle = BOOLEAN returned as a double. TRUE if it is an interior angle.

isFlipped = a boolean returned as a double. TRUE if it is flipped.

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
