---
title: "View::GetDimensionDisplayString3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionDisplayString3.htm"
---

# View::GetDimensionDisplayString3

This method is obsolete and has been superseded by [View::GetDimensionDisplayString4](sldworksAPI.chm::/View/View__GetDimensionDisplayString4.htm).

Description

This method gets all of the dimension strings in the current drawing view.

Syntax (OLE Automation)

retval = View.GetDimensionDisplayString3 ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings containing the dimension text |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionDisplayString3 ( retval )

| Output: | (BSTR*) retval | Array of strings containing the dimension text |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For each dimension in the drawing view, this method returns 10 strings. If any of the dimension strings are not used, then those strings are returned as NULL strings.

[ value1, tolMax1 tolMin1, value2, tolMax2, tolMin2, prefix, suffix, callout1, callout2 ]

This set of data is returned for each dimension in the view. See View::GetDimensionCount3 to determine the number of dimensions in the view.

This method is identical to the now obsolete View::GetDimensionDisplayString2 except a dangling dimension was not output by that method. This version of this method outputs dangling dimensions.
