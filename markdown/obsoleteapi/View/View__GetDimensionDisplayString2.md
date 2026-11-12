---
title: "View::GetDimensionDisplayString2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionDisplayString2.htm"
---

# View::GetDimensionDisplayString2

This method is obsolete and has been superseded by [View::GetDimensionDisplayString3](View__GetDimensionDisplayString3.htm).

Description

This method gets all of the dimension strings in the current drawing view.

Syntax (OLE Automation)

retval = View.GetDimensionDisplayString2 ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings containing the dimension text |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionDisplayString2 ( retval )

| Output: | (BSTR*) retval | Array of strings containing the dimension text |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For each dimension in the drawing view, this method returns return 10 strings. If any of the dimension strings are not used, then those strings are returned as NULL strings.

[ value1, tolMax1 tolMin1, value2, tolMax2, tolMin2, prefix, suffix, callout1, callout2 ]

This set of data is returned for each dimension in the view. See View::GetDimensionCount2 to determine the number of dimensions in the view.

This method is identical to View::GetDimensionDisplayString except when a base ordinate is not visible, then the subordinates were not output, regardless of whether they were visible or not. With this method, the output of each subordinate, if it is visible, occurs regardless of whether or not its base ordinate is visible.
