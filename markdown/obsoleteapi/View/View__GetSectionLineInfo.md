---
title: "View::GetSectionLineInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetSectionLineInfo.htm"
---

# View::GetSectionLineInfo

This method is obsolete and has been superseded by [View::GetSectionLineInfo2](sldworksAPI.chm::/View/View__GetSectionLineInfo2.htm).

Description

This method gets all information on section lines in the view.

Syntax (OLE Automation)

retval = View.GetSectionLineInfo ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetSectionLineInfo ( retval )

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before using this method, use View::GetSectionLineCount to determine the size of the data being returned.

The return value is the following array of doubles:

[ numSectionLines, [ numSegments, [ lineType, startPt[3], endPt[3] ], arrowStart1[3], arrowEnd1[3], arrowWidth1, arrowHeight1, arrowStyle1, arrowStart2[3], arrowEnd2[3], arrowWidth2, arrowHeight2, arrowStyle2, textPt1[3], textPt2[3], textHeight ] ]

where:

numSectionLines = number of section lines in this view. See also View::GetSectionLineCount.

The following set of data repeats itself for each section line in the view. The number of times the information is given is numSectionLines:

numSegments = number of line segments in this section line.

The following three variables repeat themselves for each segment in the current section line. The number of times the information is given is numSegments:

lineType = linetype for this line segment. See swLineTypes_e.

startPt[3] = X,Y,Z start point for the current segment of this section line.

endPt[3] = X,Y,Z end point for the current segment of this section line.

arrowStart1[3] = X,Y,Z start point for arrow head 1 on this section line.

arrowEnd1[3] = X,Y,Z end point for arrow head 1 on this section line.

arrowWidth1 = width of arrow 1 on this section line.

arrowHeight1 = height of arrow 1 on this section line.

arrowStyle1 = style of arrow 1 on this section line.

arrowStart2[3] = X,Y,Z start point for arrow head 2 on this section line.

arrowEnd2[3] = X,Y,Z end point for arrow head 2 on this section line.

arrowWidth2 = width of arrow 2 on this section line.

arrowHeight2 = height of arrow 2 on this section line.

arrowStyle2 = style of arrow 2 on this section line.

textPt1[3] = X,Y,Z point for the text location near arrow 1.

textPt2[3] = X,Y,Z point for the text location near arrow 2.

textHeight = text height in meters.

To get the actual text value, see GetSectionLineStrings.
