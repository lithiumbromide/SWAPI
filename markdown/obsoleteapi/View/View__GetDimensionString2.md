---
title: "View::GetDimensionString2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionString2.htm"
---

# View::GetDimensionString2

This method is obsolete and has been superseded by [View::GetDimensionString3](View__GetDimensionString3.htm).

Description

This method returns an array of strings containing the text associated with each dimension in the view. Use View::GetDimensionCount2 to determine the number of strings to be returned.

Syntax (OLE Automation)

retval = View.GetDimensionString2 ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the text associated with each dimension |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionString2 ( retval )

| Output: | (BSTR*) retval | Text associated with each dimension |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is identical to View::GetDimensionString except when a base ordinate is not visible, the subordinates were not previously output, whether they were visible or not. With this method, the output of each visbile subordinate occurs whether or not its base ordinate is visible.
