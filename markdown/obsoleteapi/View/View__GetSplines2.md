---
title: "View::GetSplines2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetSplines2.htm"
---

# View::GetSplines2

This method is obsolete and has been superseded by [View::GetSplines3](sldworksAPI.chm::/View/View__GetSplines3.htm).

Description

This method returns information for each spline that was sketched in this drawing view.

NOTE: This method only returns splines that have been deliberately sketched in this drawing view. All part and assembly geometry shown in a drawing view is represented by polylines. To access the Polylines, use View::GetPolylines3.

Syntax (OLE Automation)

retval = View.GetSplines2 ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetSplines2 ( &retval )

| Output: | (double) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Format of return values is an array of doubles with the format:

[ [ Color, LineType, LineStyleIndex, LineWeight, NumSplinePoints, [x,y,z] ] … ]

where:

Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

LineType = line type. Valid returns as defined in swLineTypes_e. A lineType is a combination of a lineStyle and lineWeight.

LineStyleIndex = index location of this line style inside SolidWorks Line Style Manager

LineWeight = integer value defining the line weight

This complete set of data repeats itself for each spline found in the view. For each spline, the array returned contains the color, line type, number of spline points in the spline, and X,Y,Z value for each of those points. Therefore, the [x,y,z] parameter is an array of NumSplinePoints that can vary in size from spline to spline.

The [x,y,z] points for each spline are not the same as the points used to generate the spline. This method tessellates the spline based on the display quality and place points along the spline appropriately.

The data returned from this method is in terms of vew space. If you want the data in terms of sheet space (that is, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from View::GetXForm.

To determine the number of splines in the view, refer to View::GetSplineCount or get the number of elements in the SafeArray returned by the call to GetSplines.

If you are using COM, then your call to IGetSplines must be preceded by a call to GetSplineCount.
