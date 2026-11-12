---
title: "View::GetDimensionDisplayInfoSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionDisplayInfoSize.htm"
---

# View::GetDimensionDisplayInfoSize

This method is obsolete and has been superseded by [View::GetDimensionDisplayInfoSize2](sldworksAPI.chm::/View/View__GetDimensionDisplayInfoSize2.htm).

Description

This method gets the size of the dimension lines array in this view.

Syntax (OLE Automation)

retval = View.GetDimensionDisplayInfoSize ( )

| Output: | (long) retval | Size of the dimension lines array |
| --- | --- | --- |

Syntax (COM)

status = View->GetDimensionDisplayInfoSize ( &retval )

| Output: | (long) retval | Size of the dimension lines array |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call this method before calling View::GetDimensionDisplayInfo4.
