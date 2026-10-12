---
title: "View::GetDimensionIds"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionIds.htm"
---

# View::GetDimensionIds

This method is obsolete and has been superseded by [View::GetDimensionIds2](View__GetDimensionIds2.htm).

Description

This method returns a list of dimension names from the current drawing view.

Syntax (OLE Automation)

retval = View.GetDimensionIds ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings; each string in the array represents one dimension name from the current drawing view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionIds ( &retval )

| Output: | (BSTR) retval | Array of strings; each string in the array represents one dimension name from the current drawing view |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The order of the dimension names returned aligns with the order of information returned from View::GetDimensionInfo. This alignment of information is valid as long as the calls to this method and View::GetDimensionInfo are made consecutively.

One string is returned for each dimension in the view. See View::GetDimensionCount to determine the number of dimensions in the view.
