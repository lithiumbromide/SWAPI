---
title: "View::GetFirstDisplayDimension3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetFirstDisplayDimension3.htm"
---

# View::GetFirstDisplayDimension3

This method is obsolete and has been superseded by [View::GetFirstDisplayDimension4](View__GetFirstDisplayDimension4.htm).

Description

This method returns the first display dimension in this drawing view.

Syntax (OLE Automation)

retval = View.GetFirstDisplayDimension3 ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the first DisplayDimension object |
| --- | --- | --- |

Syntax (COM)

status = View->IGetFirstDisplayDimension3 ( &retval )

| Output: | (LPDISPLAYDIMENSION) retval | Pointer to the first DisplayDimension object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A SolidWorks dimension can be displayed more than once. For example, the Base-Extrude dimension could be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SolidWorks API. The original Base-Extrude dimension is represented by the Dimension object in the SolidWorks API.

This method is identical to the now obsolete View::GetFirstDisplayDimension2 except in the case of a dangling dimension. View::GetFirstDisplayDimension2 did not output it, this method does.
