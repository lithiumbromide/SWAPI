---
title: "View::GetDimensionCount2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionCount2.htm"
---

# View::GetDimensionCount2

This method is obsolete and has been superseded by [View::GetDimensionCount3](View__GetDimensionCount3.htm).

Description

This method returns the number of dimensions in the view.

Syntax (OLE Automation)

retval = View.GetDimensionCount2 ()

| Return: | (long) retval | Number of dimensions in the view |
| --- | --- | --- |

Syntax (COM)

status = View->GetDimensionCount2 ( &retval )

| Output: | (long) retval | Number of dimensions in the view. |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is identical to the now obsolete View::GetDimensionCount except when a base ordinate is not visible, the subordinates were not output, regardless if they are visible or not.

With this method, the output of each subordinate, if it is visible, occurs regardless if its base ordinate is visible.
