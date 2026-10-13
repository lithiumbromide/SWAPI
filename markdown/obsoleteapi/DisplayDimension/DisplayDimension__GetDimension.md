---
title: "DisplayDimension::GetDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetDimension.htm"
---

# DisplayDimension::GetDimension

This method is obsolete and has been superseded by [DisplayDimension::GetDimension2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__GetDimension2.htm).

Description

This method gets the model dimension that was used to create this display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetDimension ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the model Dimension object |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->IGetDimension ( &retval )

| Output: | (LPDIMENSION) retval | Pointer to the Dimension object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SolidWorks API. The original base-extrude dimension is represented by the Dimension object in the SolidWorks API.
