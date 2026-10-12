---
title: "View::GetDimensionIds2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionIds2.htm"
---

# View::GetDimensionIds2

This method is obsolete and has been superseded by [View::GetDimensionIds3](View__GetDimensionIds3.htm).

Description

This method returns a list of dimension names from the current drawing view.

Syntax (OLE Automation)

retval = View.GetDimensionIds2 ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings; each string represents one dimension name from the current drawing view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionIds2 ( &retval )

| Output: | (BSTR) retval | Array of strings; each string represents one dimension name from the current drawing view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The order of the dimension names returned aligns with the order of information returned from View::GetDimensionInfo4. This alignment of information is valid as long as the calls to this method and View::GetDimensionInfo4 are made consecutively.

One string is returned for each dimension in the view. See [View::GetDimensionCount2](View__GetDimensionCount2.htm) to determine the number of dimensions in the view.

This method is identical to View::GetDimensionIds except when a base ordinate was not visible, the subordinates were not previously output, regardless of whether they were visible or not. With View::GetDimensionIds2, the output of each subordinate, if it is visible, occurs regardless of whether or not its base ordinate is visible.
