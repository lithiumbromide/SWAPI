---
title: "View::GetLines2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetLines2.htm"
---

# View::GetLines2

This method is obsolete and has been superseded by [View::GetLines3](View__GetLines3.htm).

Description

This method returns information for each line that was sketched in this drawing view.

NOTE: This method only returns lines that have been deliberately sketched in this drawing view. All part and assembly geometry shown in a drawing view is represented by polylines. To access the polylines, use View::GetPolylines3.

Syntax (OLE Automation)

retval = View.GetLines2 ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetLines2 ( &retval )

| Output: | (double)retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ color, lineType, lineStyleIndex, lineWeight, StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, ... ]

where all data values are returned as doubles:

color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

LineType = line type. Valid returns as defined in swLineTypes_e. A lineType is a combination of a lineStyle and lineWeight.

LineStyleIndex = index location of this line style inside SolidWorks Line Style Manager.

lineWeight = integer value defining the line weight.

where this array of 10 values repeats itself for each line in the view. The number of doubles returned will be (lineCount * 10). To determine the number of lines in the view, use View::GetLineCount.

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (that is, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from View::GetXForm.
