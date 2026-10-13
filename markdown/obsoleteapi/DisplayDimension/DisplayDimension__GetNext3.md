---
title: "DisplayDimension::GetNext3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetNext3.htm"
---

# DisplayDimension::GetNext3

This method is obsolete and has been superseded by [DisplayDimension::GetNext4](DisplayDimension__GetNext4.htm).

Description

This method gets the next display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetNext3 ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the next DisplayDimension |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->IGetNext3 ( &retval )

| Output: | (LPDISPLAYDIMENSION) retval | Pointer to the next DisplayDimension object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as "Display Dimensions" and are represented by the DisplayDimension object in the SolidWorks API. The original base-extrude dimension is represented by the Dimension object in the SolidWorks API.

This method is identical to DisplayDimension::GetNext2, except that it returns dangling dimensions.
