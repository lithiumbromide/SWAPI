---
title: "View::GetPolylines2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetPolylines2.htm"
---

# View::GetPolylines2

This method is obsolete and has been superseded by [View::GetPolyLines3](View__GetPolyLines3.htm).

Description

This method returns information about the polylines in this view.

NOTE: All geometry from a part or assembly shown in a drawing view is represented by polylines. If you need this geometry to be output to your system as lines, arcs, and so on, then you must create routines to recognize the polyline information as a straight line, arc, and so on, and then generate the appropriate geometry.

Syntax (OLE Automation)

retval = View.GetPolylines2 ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of polylines |
| --- | --- | --- |

Syntax (COM)

status = View->IGetPolylines2 ( &retval )

| Output: | (double) retval | Pointer to array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

To get items sketched in this drawing view, use View::GetArcs4, View::GetLines3, View::GetSplines3, or View::GetEllipses5.

Format of return values is an array of doubles with the format:

[ Color, LineStyle, LineFont, LineWeight, NumPolyPoints, [x,y,z] ]

where the [x,y,z] parameter is an array of NumPolyPoints.

To determine the number of polylines in the view, use View::GetPolyLineCount2.

| If LineStyle is... | Then... |
| --- | --- |
| Returned as -1 | The user has probably modified the line display manually in the drawing and you should use the LineFont and LineWeight return values to recreate the exact polyline style. The LineFont value is an index value which can be used in DrawingDoc::GetLineFontInfo2 and DrawingDoc::GetLineFontName2. |
| Is not returned as -1 | Its value contains line weight information and the LineFont and LineWeight values in the returned array are not used. In this case,use LineStyle as the index value input to DrawingDoc::GetLineFontInfo and DrawingDoc::GetLineFontName. |

NOTE: The polyline data is stored with the accuracy of a float. The return array contains doubles, but these are float values converted to doubles.

| If... | Then... |
| --- | --- |
| Changes are made to the parts or assemblies shown in this drawing | Polylines are only generated that are in the visible viewing bounds when the drawing is opened. |
| Drawing is already open | All polylines in the drawing are generated. If you open a drawing that is zoomed in to a particular region, then the polylines that are outside the zoomed region do not exist if the parts or assemblies shown in this drawing have been changed. To force the generation of all possible polyline data, call ModelDoc2::ViewZoomtofit. |
