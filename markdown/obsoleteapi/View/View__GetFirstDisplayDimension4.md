---
title: "View::GetFirstDisplayDimension4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetFirstDisplayDimension4.htm"
---

# View::GetFirstDisplayDimension4

This method is obsolete and has been superseded by [View::GetFirstDisplayDimension5](sldworksAPI.chm::/View/View__GetFirstDisplayDimension5.htm).

Description

This method returns the first display dimension in this drawing view.

Syntax (OLE Automation)

retval = View.GetFirstDisplayDimension4 ( )

| Return: | (LPDISPLAYDIMENSION) retval | Pointer to the first DisplayDimension object |
| --- | --- | --- |

Syntax (COM)

status = View->GetFirstDisplayDimension4 ( &retval )

| Output: | (LPDISPLAYDIMENSION) retval | Pointer to the first DisplayDimension object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A SolidWorks dimension can be displayed more than once. For example, the base-extrude dimension could be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SolidWorks API. The original base-extrude dimension is represented by the Dimension object in the SolidWorks API.

This method includes suppressed dimensions.
