---
title: "View::GetDimensionIds3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionIds3.htm"
---

# View::GetDimensionIds3

This method is obsolete and has been superseded by [View::GetDimensionIds4](sldworksAPI.chm::/View/View__GetDimensionIds4.htm).

Description

This method returns a list of dimension names from the current drawing view.

Syntax (OLE Automation)

retval = View.GetDimensionIds3 ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings; each string represents one dimension name from the current drawing view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionIds3 ( &retval )

| Output: | (BSTR) retval | Array of strings; each string represents one dimension name from the current drawing view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The order of the dimension names returned align with the order of information returned from View::GetDimensionInfo5. This alignment of information is valid as long as the calls to this method and View::GetDimensionInfo5 are made consecutively.

One string is returned for each dimension in the view. See View::GetDimensionCount3 to determine the number of dimensions in the view.

This method is identical to the now obsolete View::GetDimensionIds2 except View::GetDimensionIds2 did not output dangling dimensions. This method does.
