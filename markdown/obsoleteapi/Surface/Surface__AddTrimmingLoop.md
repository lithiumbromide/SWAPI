---
title: "Surface::AddTrimmingLoop"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Surface/Surface__AddTrimmingLoop.htm"
---

# Surface::AddTrimmingLoop

This method is obsolete and has been superseded by [Surface::AddTrimmingLoop2](sldworksAPI.chm::/Surface/Surface__AddTrimmingLoop2.htm).

Description

This method creates a trimming loop out of <NumCrvs> surface parametric (UV-curves) and adds it to a list of such loops. The list is created by a previous call to one of the base surface creation functions (for example, Body::CreateRevolutionSurface).

Syntax (OLE Automation)

retval = Surface.AddTrimmingLoop ( nCrvs, vOrder, vDim, vPeriodic, vNumKnots, vNumCtrlPoints, vKnots, vCtrlPointDbls)

| Input: | (long) nCrvs | Number of surface parametric (UV) curves constituting the loop; it is also directly related to the dimension of each of the SafeArrays Order, Dim, Periodic, NumKnots, NumControlPnts, which must be loaded with the information regarding each of the curves, specifically the dimension of those arrays is ArraySize = nCrvs |
| --- | --- | --- |
| Input: | (VARIANT) vOrder | VARIANT of type SafeArray of <ArraySize> doubles; each element (double) holding two integers representing the orders of two of the spline curves in the list; Order[i] contains the (integer) order for curve[2*i] and curve[2*i+1] |
| Input: | (VARIANT) vDim | VARIANT of type SafeArray of <ArraySize> doubles; each element (double) holding two integers representing the dimension of control points of two of the spline curves in the list; Dimension[i] contains the (integer) control point dimension for curve[2*i] and curve[2*i+1] |
| Input: | (VARIANT) vPeriodic | VARIANT of type SafeArray of <ArraySize> doubles; each element (double) holding two integers representing the periodicity of two of the spline curves in the list; Periodic[i] contains the (integer) periodicity for curve[2*i] and curve[2*i+1] |
| Input: | (VARIANT) vNumKnots | VARIANT of type SafeArray of <ArraySize> doubles; each element (double) holding two integers representing the number of knots of two of the spline curves in the list; NumKnots[i] contains the (integer) number of knots for curve[2*i] and curve[2*i+1] |
| Input: | (VARIANT) vNumCtrlPoints | VARIANT of type SafeArray of <ArraySize> doubles; each element (double) holding two integers representing the number of control points of two of the spline curves in the list; NumControlPnts[i] contains the (integer) number of control points for curve[2*i] and curve[2*i+1] |
| Input: | (VARIANT) vKnots | VARIANT of type SafeArray of <TotalNumKnots> doubles, where TotalNumKnots = numKnotsInCurve[i] from i = 1 to NumCrvs |
| Input: | (VARIANT) vCtrlPointDbls | VARIANT of type SafeArray of <TotalNumCPCoords> doubles, where TotalNumCPCoords = ( dimensionOfCPinCurve[i] * numControlPntsInCurve[i] ) from i = 1 to NumCrvs |
| Return: | (BOOL) retval | TRUE if successful in adding a trimming loop to the surface, FALSE otherwise |

Syntax (COM)

status = Surface->IAddTrimmingLoop ( CurveCount, Order, Dim, Periodic, NumKnots, NumCtrlPoints, Knots, CtrlPointDbls )

| Input: | (long) CurveCount | Number of surface parametric (UV) curves constituting the loop; it is also directly related to the dimension of each of the arrays Order, Dim, Periodic, NumKnots, NumControlPnts, which must be loaded with the information regarding each of the curves, specifically the dimension of those arrays is ArraySize = nCrvs |
| --- | --- | --- |
| Input: | (long*) Order | Pointer to array of <ArraySize> longs; each element representing the orders of two of the spline curves in the list; Order[i] contains the (integer) order for curve[2*i] and curve[2*i+1] |
| Input: | (long*) Dim | Pointer to array of <ArraySize> longs; each element representing the dimension of control points of two of the spline curves in the list; Dimension[i] contains the (integer) control point dimension for curve[2*i] and curve[2*i+1]; if you set the first value in this array to negative its absolute value, then 3D trim curves are expected |
| Input: | (long*) Periodic | Pointer to array of <ArraySize> longs; each element representing the periodicity of two of the spline curves in the list; Periodic[i] contains the (integer) periodicity for curve[2*i] and curve[2*i+1] |
| Input: | (long*) NumKnots | Pointer to array of <ArraySize> longs; each element representing the number of knots of two of the spline curves in the list; NumKnots[i] contains the (integer) number of knots for curve[2*i] and curve[2*i+1] |
| Input: | (long*) NumCtrlPoints | Pointer to array of <ArraySize> longs; each element representing the number of control points of two of the spline curves in the list. NumControlPnts[i] contains the (integer) number of control points for curve[2*i] and curve[2*i+1] |
| Input: | (double*) Knots | Pointer to array of <TotalNumKnots> doubles, where TotalNumKnots = numKnotsInCurve[i] from i = 1 to NumCrvs |
| Input: | (double*) CtrlPointDbls | Pointer to array of <TotalNumCPCoords> doubles, where TotalNumCPCoords = ( dimensionOfCPinCurve[i] * numControlPntsInCurve[i] ) from i = 1 to NumCrvs |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The information on each UV-curve is in bspline form (knots and control point coordinates), all of which are compacted into the two arrays Knots and CtrlPointDbls.

For non-rational curves the dimension value in Dim is 2. For rational curves the dimension value in Dim is 3. The minimum order value in Order is 2. An order 2 curve must consist of only one segment.

For each curve the number of control points in NumCtrlPoints >= its order.

For non-periodic curves there must be (NumCtrlPoints + Order) knot values, the maximum multiplicity of an internal knot value is (Order – 1), and the maximum multiplicity of an end knot value is Order.

For periodic curves there must be (NumCtrlPoints + 1) knot values and the maximum multiplicity of any knot value is (Order – 1). If the periodic knot has multiplicity greater than 1, repetitions must be given at the end of the knot vector.

This method expects 2D polyomial (x,y) or 2D rational (x,y,w) curves to be passed as trimming curves. However, you can set a flag so that this method accepts 3D-polyomial (x,y,z) or 3D-rational (x,y,z,w) trim curves. To do this, set the first value in the Dim array to negative its absolute value (that is, if the value is 3, set it to -3). When you do this, 3D-trim curves are expected.

Upon adding this trimming loop, you can generate a trimmed surface by calling Body2::CreateTrimmedSurface.
