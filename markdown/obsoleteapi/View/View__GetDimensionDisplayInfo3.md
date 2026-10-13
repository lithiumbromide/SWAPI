---
title: "View::GetDimensionDisplayInfo3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionDisplayInfo3.htm"
---

# View::GetDimensionDisplayInfo3

This method is obsolete and has been superseded by [View::GetDimensionDisplayInfo4](View__GetDimensionDisplayInfo4.htm).

Description

This method returns each dimension in the current drawing view in the form of line, arc, and text data.

Syntax (OLE Automation)

retval = View.GetDimensionDisplayInfo3 ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionDisplayInfo3 ( retval )

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For COM implementation, call View::GetDimensionCount3 to determine the overall size of the array needed. The maximum number of doubles contained in the array will be (dimensionCount * 173 + 1).

The data returned is an array of doubles as follows:

[ dimensionCount, lineCount, [ lineStartPt[3], lineEndPt[3] ], arcCount, [ arcCenter[3], arcStartPt[3], arcEndPt[3] ], arrowCount, [ arrowTipPt[3], arrowVector[3], arrowWidth, arrowHeight ], tolType, isDual, showParens, textAngle, value1Pos[3], tolmax1Pos[3], tolmin1Pos[3], value2Pos[3], tolmax2Pos[3], tolmin2Pos[3], prefixPos[3], suffixPos[3], tolbox1Corner1[3], tolbox1Corner2[3], tolbox2Corner1[3], tolbox2Corner2[3], parenArc1Start[3], parenArc1End[3], parenArc1Center[3], parenArc1Vector[3], parenArc2Start[3], parenArc2End[3], parenArc2Center[3], parenArc2Vector[3], callout1TextPos[3], callout2TextPos[3] ]

where:

dimensionCount = number of dimensions found in the drawing view

For each dimension, a repeating set of the following data exists:

lineCount = number of extension and leader lines for this dimension.

lineStartPt[3] = array of three doubles representing the line start point.

lineEndPt[3] = array of three doubles representing the line end point.

… Repeating the lineStartPt[3] and lineEndPt[3] pair up to lineCount lines.

arcCount = number of leader lines which are arcs for this dimension.

arcCenter[3] = array of three doubles representing the arc center point.

arcStartPt[3] = array of three doubles representing the arc start point.

arcEndPt[3] = array of three doubles representing the arc end point.

… Repeating the arcVertex[3], arcStartPt[3], and arcEndPt[3] group up to arcCount arcs.

arrowCount = number of arrowheads for this dimension.

arrowTipPt[3] = array of three doubles representing the arrowhead tip location.

arrowVector[3] = array of three doubles representing the arrow direction.

arrowWidth = arrowhead width.

arrowHeight = arrowhead height.

… Repeating the arrowTipPt[3], arrowVector[3], arrowWidth and arrowHeight group up to arrowCount arrowheads.

tolType = tolerance type as defined in swTolType_e enumeration.

isDual = TRUE if this dimension is a dual dimension, FALSE otherwise.

showParens = TRUE if parenthesis are shown, FALSE otherwise.

The next 25 values represent text angle and positioning. All text positions are the upperleft corner of the string.

textAngle = text angle in radians (counter clockwise from +ve x-axis)

value1Pos[3] = XYZ postion of text 1. The position is the upper-left corner of the actual string.

tolmax1Pos[3] = XYZ position of max tolerance text 1.

tolmin1Pos[3] = XYZ position of min tolerance text 1.

value2Pos[3] = XYZ position of text 2. Data returned is only valid if isDual is TRUE.

tolmax2Pos[3] = XYZ position of maximum tolerance text 2. Data returned is valid when isDual is TRUE.

tolmin2Pos[3] = XYZ position of minimum tolerance text 2. Data returned is valid when isDual is TRUE.

prefixPos[3] = XYZ position of prefix text.

suffixPos[3] = XYZ position of suffix text.

The next 12 values represent the box corners for dimensions with swTolBASIC tolerance types

tolbox1Corner1[3] = XYZ corner 1 of tolerance box 1.

tolbox1Corner2[3] = XYZ corner 2 of tolerance box 1.

tolbox2Corner1[3] = XYZ corner 1 of tolerance box 2. Data returned is valid when isDual is TRUE

tolbox2corner2[3] = XYZ corner 2 of tolerance box 2. Data returned is valid when isDual is TRUE

The next 24 values are valid when showParens is TRUE (i.e. - when this is a reference dimension)

parenArc1Start[3] = XYZ start point of the arc representing parenthesis 1.

parenArc1End[3] = XYZ end point of the arc representing parenthesis 1.

parenArc1Center[3] = XYZ center point of the arc representing parenthesis 1.

parenArc1Vector[3] = XYZ reference direction for the arc representing parenthesis 1.

parenArc2Start[3] = XYZ start point of the arc representing parenthesis 2.

parenArc2End[3] = XYZ end point of the arc representing parenthesis 2.

parenArc2Center[3] = XYZ center point of the arc representing parenthesis 2.

parenArc2Vector[3] = XYZ reference direction for the arc representing parenthesis 2.

callout1TextPos[3] = XYZ position of first callout text (text above)

callout2TextPos[3] = XYZ position of second callout text (text below)

… Repeating the entire lineCount … callout2TextPos group up to dimensionCount dimensions.

For example, if a particular view had two dimensions, and the first dimension had 3 lines, 0 arcs, and 3 arrows, and the second dimension had 2 lines, 1 arc, and 2 arrows, then the array returned would be as follows:

[ 2, 3, line1StartPtx, y, z, line1EndPtx, y, z, line2StartPtx, y, z, line2EndPtx, y, z, line3StartPtx, y, z, line3EndPtx, y, z, 0, 2, arrow1TipPtx, y, z, arrow1Vectorx, y, z, arrow1Width, arrow1Height, arrow2TipPtx, y, z, arrow2Vectorx, y, z, arrow2Width, arrow2Height, tolType, isDual, showParens, textAngle, value1Posx, y, z, tolmax1Posx, y, z, tolmin1Posx, y, z, value2Posx, y, z, tolmax2Posx, y, z, tolmin2Posx, y, z, prefixPosx, y, z, suffixPosx, y, z, tolbox1Corner1x, y, z, tolbox1Corner2x, y, z, tolbox2Corner1x, y, z, tolbox2Corner2x, y, z, parenArc1Startx, y, z, parenArc1Endx, y, z, parenArc1Centerx, y, z, parenArc1Vectorx, y, z, parenArc2Startx, y, z, parenArc2Endx, y, z, parenArc2Centerx, y, z, parenArc2Vectorx, y, z, callout1TextPosx, y, z, callout2TextPosx, y, z, 2, line1StartPtx, y, z, line1EndPtx, y, z, line2StartPtx, y, z, line2EndPtx, y, z, 1, arc1Vertexx, y, z, arc1StartPtx, y, z, arc1EndPtx, y, z, 2, arrow1TipPtx, y, z, arrow1Vectorx, y, z, arrow1Width, arrow1Height, arrow2TipPtx, y, z, arrow2Vectorx, y, z, arrow2Width, arrow2Height, tolType, isDual, showParens, textAngle, value1Posx, y, z, tolmax1Posx, y, z, tolmin1Posx, y, z, value2Posx, y, z, tolmax2Posx, y, z, tolmin2Posx, y, z, prefixPosx, y, z, suffixPosx, y, z, tolbox1Corner1x, y, z, tolbox1Corner2x, y, z, tolbox2Corner1x, y, z, tolbox2Corner2x, y, z, parenArc1Startx, y, z, parenArc1Endx, y, z, parenArc1Centerx, y, z, parenArc1Vectorx, y, z, parenArc2Startx, y, z, parenArc2Endx, y, z, parenArc2Centerx, y, z, parenArc2Vectorx, y, z, callout1TextPosx, y, z, callout2TextPosx, y, z ]

where the 3, 0, 2 and 2, 1, 2 represent the number of lines, arcs, and arrows for each of the two dimensions.
