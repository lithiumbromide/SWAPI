---
title: "DisplayDimension::GetNext4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetNext4.htm"
---

# DisplayDimension::GetNext4

This method is obsolete and has been superseded by [DisplayDimension::GetNext5](sldworksAPI.chm::/DisplayDimension/DisplayDimension__GetNext5.htm).

Description

This method gets the next display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetNext4 ( )

| Return: | (LPDISPLAYDIMENSION) retval | Pointer to the next DisplayDimension object |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->GetNext4 ( &retval )

| Output: | (LPDISPLAYDIMENSION) retval | Pointer to the next DisplayDimension object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SolidWorks API. The original base-extrude dimension is represented by the Dimension object in the SolidWorks API.

This method includes suppressed dimensions.
