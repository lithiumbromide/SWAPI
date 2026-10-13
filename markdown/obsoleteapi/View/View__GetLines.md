---
title: "View::GetLines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetLines.htm"
---

# View::GetLines

This method is obsolete and has been superseded by [View::GetLines2](View__GetLines2.htm).

Description

This method returns information for each line that was sketched in this drawing view.

NOTE: This method only return lines that have been deliberately sketched in this drawing view. All part and assembly geometry shown in a drawing view is represented by polylines. To access the polylines, use View::GetPolylines3 method.

Syntax (OLE Automation)

retval = View.GetLines ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetLines ( &retval )

| Output: | (double) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ LineType, StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, ... ]

where this array of 7 values repeats itself for each line in the view. The number of doubles returned is (lineCount * 7). To determine the number of lines in the view, refer to View::GetLineCount.

See swLineTypes_e for valid line types.

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from View::GetXForm.
