---
title: "View::GetDimensionString3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionString3.htm"
---

# View::GetDimensionString3

This method is obsolete and has been superseded by [View::GetDimensionString4](sldworksAPI.chm::/View/View__GetDimensionString4.htm).

Description

This method return an array of strings containing the text associated with each dimension in the view. See View::GetDimensionCount3 to determine the number of strings to be returned.

Syntax (OLE Automation)

retval = View.GetDimensionString3 ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the text associated with each dimension |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionString3 ( retval )

| Output: | (BSTR*) retval | Text associated with each dimension |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is identical to the now obsolete View::GetDimensionString2 except in the case of a dangling dimension. This method outputs a dangling dimension; the previous version of this method does not.
