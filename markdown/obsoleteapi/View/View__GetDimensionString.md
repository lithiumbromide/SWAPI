---
title: "View::GetDimensionString"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionString.htm"
---

# View::GetDimensionString

This method is obsolete and has been superseded by [View::GetDimensionString2](View__GetDimensionString2.htm).

Description

This method returns an array of strings containing the text associated with each dimension in the view. See View::GetDimensionCount to determine the number of strings to be returned.

Syntax (OLE Automation)

retval = View.GetDimensionString ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the text associated with each dimension |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionString ( retval )

| Output: | (BSTR*) retval | Text associated with each dimension |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
