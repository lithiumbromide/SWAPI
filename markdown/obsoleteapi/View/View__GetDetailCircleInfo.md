---
title: "View::GetDetailCircleInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDetailCircleInfo.htm"
---

# View::GetDetailCircleInfo

This method is obsolete and has been superseded by [View::GetDetailCircleInfo2](sldworksAPI.chm::/View/View__GetDetailCircleInfo2.htm).

Description

This method gets information about each detail circle in the drawing view.

Syntax (OLE Automation)

retval = View.GetDetailCircleInfo ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDetailCircleInfo ( retval )

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ numDetailCircles, [ centerPt[3], startPt[3], endPt[3], lineType, textPt[3], textHeight, numArrows, [ arrowTip[3], arrowComponent[3], arrowWidth, arrowHeight, arrowStyle ] ] ]

where:

numDetailCircles equals the number of detail circles in this view. See also View::GetDetailCircleCount.

The following set of data repeats itself for each detail circle in the view. The number of times the following information is given is numDetailCircles:

centerPt[3] = X,Y,Z center point for this detail circle

startPt[3] = X,Y,Z start point for this detail circle

endPt[3] = X,Y,Z end point for this detail circle

lineType = linetype for this detail circle as defined in swLineTypes_e

textPt[3] = X,Y,Z point for the text location.

textHeight = text height in meters

numArrows = number of arrows for this detail circle.

The following set of data repeats itself for each arrow in the current detail circle. The number of times the following information is given is numArrows:

arrowTip[3] = X,Y,Z start point for this arrow head

arrowComponent[3] = X,Y,Z component for this arrow head

arrowWidth = width of this arrow head

arrowHeight = height of this arrow head

arrowStyle = style of this arrow head as defined in swArrowStyle_e

To get the actual text value, see View::GetDetailCircleStrings.
