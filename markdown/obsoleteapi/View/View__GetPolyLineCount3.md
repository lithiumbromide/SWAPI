---
title: "View::GetPolyLineCount3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetPolyLineCount3.htm"
---

# View::GetPolyLineCount3

This method is obsolete and has been superseded by [View::GetPolylineCount4](View__GetPolylineCount4.htm).

Description

This method returns the number of polylines in the view and the array size needed for a call to View::IGetPolylines3.

Syntax (OLE Automation)

Not available. Use the upper bound on the SareArray returned from View::GetPolyLines3.

Syntax (COM)

status = View->GetPolyLineCount3 ( PointCount, &retval )

| Output: | (long*) PointCount | Size of array needed to allocate in doubles for View::GetPolylines3 |
| --- | --- | --- |
| Output: | (long) retval | Number of polylines found in the view |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| If... | Then... |
| --- | --- |
| Changes are made to the parts or assemblies shown in this drawing | Polylines are only generated that are in the visible viewing bounds when the drawing is opened. |
| Drawing is already open | All polylines in the drawing are generated. If you open a drawing that is zoomed in to a particular region, then the polylines that are outside the zoomed region do not exist if the parts or assemblies shown in this drawing have been changed. To force the generation of all possible polyline data, call ModelDoc2::ViewZoomtofit. |
