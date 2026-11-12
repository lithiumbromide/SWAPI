---
title: "View::GetPolylines3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetPolyLines3.htm"
---

# View::GetPolylines3

This method is obsolete and has been superseded by [View::GetPolylines4](View__GetPolylines4.htm).

Description

This method returns information about the polylines in this view. All geometry from a part or assembly shown in a drawing view is represented by polylines.

Syntax (OLE Automation)

retval = View.GetPolylines3 ( )

| Return: | (VARIANT) retval | SafeArray of polylines |
| --- | --- | --- |

Syntax (COM)

status = View->IGetPolylines3 ( retval )

| Output: | (double*) retval | Pointer to array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns geometric data for arcs and circles. Polylines used to represent lines, splines, and ellipses must be interpreted by your application if you need to generate the underlying geometry type.

To get the size of array needed to hold this data in COM applications, call View::GetPolyLineCount3.

To get items that were sketched in this drawing view,use View::GetArcs4, View::GetLines3, View::GetSplines3, or View::GetEllipses5.

Format of the return value is the following array of doubles:

[ Type, GeomDataSize, GeomData[ ], Color, LineStyle, LineFont, LineWeight, NumPolyPoints, [x,y,z] ]

where:

Type = underlying geometry type, possible values are:

- 0 Polyline type
- 1 Arc or dircle type

GeomDataSize = number of elements in the GeomData array. For Type = 0, this will be 0.

GeomData[ ] = geometric data to use to represent the underlying geometry type. The data returned in this array is based on the underlying geometry type and is as follows:

- Type = 0. This array is empty.
- Type = 1. [ centerPtX, centerPtY, centerPtZ, startPtX, startPtY, startPtZ, endPtX, endPtY, endPtZ, normalX, normalY, normalZ ]

Color = polyline color.

LineStyle = value combines polyline font and weight information. This value can be used as an input to GetLineFontInfo and GetLineFontName. If this value is -1, then the user has probably modified the line display manually in the drawing and you should use the LineFont and LineWeight return values to recreate the exact polyline style.

LineFont = value is used for polyline font information. This value can be used as an input to the GetLineFontInfo2 and GetLineFontName2. This value is only valid if LineStyle is -1.

LineWeight = polyline weight where Thin = 0.0, Normal = 1.0, Thick = 2.0. This value is only valid if LineStyle is -1.

NumPolyPoints = number of XYZ points found in the [x,y,z] return value.

[x,y,z] = array of points used to describe the polyline. This array has NumPolyPoints points. This data ise returned for every polyline regardless of Type.

To determine the number of polylines in the view, use View::GetPolyLineCount.

| If... | Then... |
| --- | --- |
| Changes are made to the parts or assemblies shown in this drawing | Polylines are only generated that are in the visible viewing bounds when the drawing is opened. |
| Drawing is already open | All polylines in the drawing are generated. If you open a drawing that is zoomed in to a particular region, then the polylines that are outside the zoomed region do not exist if the parts or assemblies shown in this drawing have been changed. To force the generation of all possible polyline data, call ModelDoc2::ViewZoomtofit. |
