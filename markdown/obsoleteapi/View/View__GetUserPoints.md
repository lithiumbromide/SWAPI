---
title: "View::GetUserPoints"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetUserPoints.htm"
---

# View::GetUserPoints

This method is obsolete and has been superseded by [View::GetUserPoints2](sldworksAPI.chm::/View/View__GetUserPoints2.htm).

Description

This method returns all of the user points in this drawing view.

Syntax (OLE Automation)

retval = View.GetUserPoints ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetUserPoints ( &retval )

| Output: | (double) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[ [ X, Y, Z ], .. ]

size = Number of Points * 3

This set of data repeats itself for each user point in the view. The size of the array is (NumPts * 3). To determine the number of points in the view, see View::GetUserPointsCount.

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (that is, - the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from View::GetXForm.
