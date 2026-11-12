---
title: "View::GetFirstDisplayDimension2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetFirstDisplayDimension2.htm"
---

# View::GetFirstDisplayDimension2

This method is obsolete and has been superseded by [View::GetFirstDisplayDimension3](View__GetFirstDisplayDimension3.htm).

Description

This method returns the first display dimension in this drawing view.

Syntax (OLE Automation)

retval = View.GetFirstDisplayDimension2 ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the first DisplayDimension object |
| --- | --- | --- |

Syntax (COM)

status = View->IGetFirstDisplayDimension2 ( &retval )

| Output: | (LPDISPLAYDIMENSION) retval | Pointer to the first DisplayDimension object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A SolidWorks dimension can be displayed more than once. For example, the Base-Extrude dimension could be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SolidWorks API. The original Base-Extrude dimension is represented by the Dimension object in the SolidWorks API.

This function is identical to the now obsolete View::GetFirstDisplayDimension except when a base ordinate is not visible, the subordinates were not previously output, whether they were visible or not. With this method the output of each subodinate, if it is visible, occurs whether or not its base ordinate is visible.
