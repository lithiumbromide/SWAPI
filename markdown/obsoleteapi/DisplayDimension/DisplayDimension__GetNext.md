---
title: "DisplayDimension::GetNext"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetNext.htm"
---

# DisplayDimension::GetNext

This method is obsolete and has been superseded by [DisplayDimension::GetNext2](DisplayDimension__GetNext2.htm).

Description

This method gets the next display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetNext ( )

| Return: | (LPDISPATCH) retval | pointer to a Dispatch object, the next DisplayDimension |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->IGetNext ( &retval )

| Output: | (LPDISPLAYDIMENSION retval | Pointer to a the next DisplayDimension |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as "Display Dimensions" and are represented by the DisplayDimension object in the SolidWorks API. The original base-extrude dimension is represented by the Dimension object in the SolidWorks API.
