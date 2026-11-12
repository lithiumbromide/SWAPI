---
title: "View::GetDimensionDisplayString"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionDisplayString.htm"
---

# View::GetDimensionDisplayString

This method is obsolete and has been superseded by [View::GetDimensionDisplayString2](View__GetDimensionDisplayString2.htm).

Description

This method gets all of the dimension strings in the current drawing view.

Syntax (OLE Automation)

retval = View.GetDimensionDisplayString ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings containing the dimension text |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionDisplayString ( retval )

| Output: | (BSTR*) retval | Array of strings containing the dimension text |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For each dimension in the drawing view, this method returns 10 strings. If any of the dimension strings are not used, then those strings are returned as NULL strings.

[ value1, tolMax1 tolMin1, value2, tolMax2, tolMin2, prefix, suffix, callout1, callout2 ]

This set of data is returned for each dimension in the view. See View::GetDimensionCount to determine the number of dimensions in the view.
