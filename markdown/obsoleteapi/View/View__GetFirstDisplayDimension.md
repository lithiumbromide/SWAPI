---
title: "View::GetFirstDisplayDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetFirstDisplayDimension.htm"
---

# View::GetFirstDisplayDimension

This method is obsolete and has been superseded by [View::GetFirstDisplayDimension2](View__GetFirstDisplayDimension2.htm).

Description

This method returns the first display dimension in this drawing view.

Syntax (OLE Automation)

retval = View.GetFirstDisplayDimension ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the first DisplayDimension object |
| --- | --- | --- |

Syntax (COM)

status = View->IGetFirstDisplayDimension ( &retval )

| Output: | (LPDISPLAYDIMENSION) retval | Pointer to the first DisplayDimension object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A dimension can be displayed more than once. For example, the Base-Extrude dimension could be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SolidWorks API. The original Base-Extrude dimension is represented by the Dimension object in the SolidWorks API.
