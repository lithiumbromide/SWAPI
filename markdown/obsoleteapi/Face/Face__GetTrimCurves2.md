---
title: "Face::GetTrimCurves2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTrimCurves2.htm"
---

# Face::GetTrimCurves2

This method is obsolete and has been superseded by [Face2::GetTrimCurves2](sldworksAPI.chm::/Face2/Face2__GetTrimCurves2.htm).

Description

This method returns arrays containing the definition of all the entities that describe a trimmed face.

Syntax (OLE Automation)

retval = Face.GetTrimCurves2 ( wantCubic, wantNRational )

| Input: | (BOOL) wantCubic | TRUE if the trim curves are to be cubic, FALSE if not |
| --- | --- | --- |
| Input: | (BOOL) wantNRational | TRUE if the trim curves are to be non-rational, FALSE if not |
| Return: | (VARIANT) retval | VARIANT of type SafeArray containing an array of doubles (see below) |

Syntax (COM)

status = Face->IGetTrimCurve ( retval )

| Output: | (double*) retval | Array of doubles of size returned by Face::IGetTrimCurveSize2 (see below) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method returns an array containing the definition of all of the entities that describe a trimmed face. The data is arranged in collections of surface curves (curves defined in the 2-D parametric space of the surface, or SP curves) organized into loops (closed composite curves).

All SP curves are returned as b-splines. To control the tolerance of the SP curves, use [Modeler::SetTolerances](../Modeler/Modeler__SetTolerances.htm).

For IGetTrimCurve2, a call to [Face::IGetTrimCurveSize2](Face__IGetTrimCurveSize2.htm) must precede the call to IGetTrimCurve2 to get the size of the array required and pre-process the trim curve data.

The surface and trim curve parameterization returned by this method might be different from the parameterization returned by other methods, such as [Face::GetUVBounds](Face__GetUVBounds.htm), Surface::Parameterization, [Edge::GetCurveParams](../Edge/Edge__GetCurveParams.htm), and so on.

If you set wantCubic to TRUE, then this method returns the underlying Bsurface definition. If you want to use the Bsurface in combination with its trim curves, set wantCubic=TRUE since it provides better alignment of the trim curves with the Bsurface because they are generated at the same time.

Each face typically has at least one outer loop and zero or more inner loops. Outer loops define the periphery of the face; inner loops define holes in the face. Outer loops are returned before inner loops if possible. If you need to be certain, use Loop2::IsOuter.

#### Periodic Faces

Periodic faces present many obstacles in translation. As a general rule, it is best to chop up all periodic surfaces by making a call to Body::GetProcessedBody. This function will return a new body to the caller with periodic faces chopped up into multiple faces. Processing this new body, instead of the original body, will avoid many of the pitfalls (see below) associated with periodics.

If this face is periodic and crosses the "seam" (0 & 360 degree location), then this method will split the face into more than one trimmed surface for the purposes of returning this set of data. The first time that this function is called on any face, it will return data for the first trimmed surface on the face. Each subsequent call to this function on the same face will return data for the next trimmed surface, if one exists. Refer to the packedDouble8 parameter to determine the number of surfaces for this face.

To avoid the return of multiple surfaces per face, we recommend processing the body returned from Body::GetProcessedBody.

In addition, using the body object returned from Body::GetProcessedBody will usually prevent GetTrimCurves2 from returning multiple outer loops when it encounters certain periodic surfaces. In other words, it can prevent GetTrimCurves2 from generating multiple faces (each with an outer loop) for a particular periodic surface.

#### Edges

If your program uses calls to both [Face::GetEdges](Face__GetEdges.htm) and GetTrimCurves2 or to both [Face::EnumEdges](Face__EnumEdges.htm) and GetTrimCurves2, then you should be aware of the following:

GetTrimCurves2 stores a temporary buffer containing the edges for this face. If this temporary buffer exists, then calls to Face::GetEdges or Face::EnumEdges access the buffer. This is beneficial if you are attempting to align the trim curves of the face with their corresponding Edges. If your call to Face::GetEdges or Face::EnumEdges is made immediately following your call to GetTrimCurves2, then the order of the trim curves will align with the order of the Edges. However, if you are processing all the trimcurves and then processing all the edges, you will find that your first call to access the edges will use the temporary buffer of edges generated in your last call to GetTrimCurves2. Since your last call to GetTrimCurves2 and your current call to get the edges were probably made from different faces, you will see a mismatch of data. This mismatch of data may been seen when GetEdgeCount does not match the SafeArray size from Face::GetEdges or it may be seen when the edge data does not match the face being examined. Therefore, calls to Face::GetEdges or Face::EnumEdges should be made in the same loop and immediately following your call to Face::GetEdges. The temporary buffer of edges is destroyed after each call to Face::GetEdges or Face::EnumEdges.

There might not be a corresponding edge for each trim curve. This is especially true for periodic surfaces for which no edge exists along the seam (0 and 360 degree location), yet this method returns a trim curve. You can detect this situation by simply comparing the number of edges on the face, [Face::GetEdgeCount](Face__GetEdgeCount.htm) , with the number of trim (SP) curves on the face, PackedDouble1 (see below).

To force edge generation along the seam of a periodic surface, use Body::GetProcessedBody. This method creates a copy of the body with faces and surfaces chopped up. However, there are still certain situations (poles of a surface, cusps on a surface, and so on) in which this method returns a trim curve where no edge exists. In this situation, the list of edges returned from GetEdges or EnumEdges does not align with the list of trim curves. Again, you can detect this by comparing the value returned by GetEdgeCount with PackedDouble1 (see below), but you need to handle matching the edges with their corresponding trim curve.

#### Return Values

The data is returned in a large array of doubles. Integer data is packed among the doubles in pairs.

The format of faceData[] is as follows:

```vb
[ packedDouble1, packedDouble2[ ], packedDouble3[ ], knotValues[ ], ctrlPointCoords[ ], packedDouble8 ]
```

| packedDouble1 | An integer pair containing number of loops and total number of SP curves (trim curves). The length of any edge list generated immediately after a call to GetTrimCurves2 will be equal to the number of SP curves. |
| --- | --- |
| packedDouble2[ ] | Series of integer pairs containing the number of SP curves in each loop; the first integer in each pair represents the number of curves in the odd loops, the second represents the even. The total number of integer pairs here is half the number of loops, rounded up |
| packedDouble3[ ] | For each SP curve, a set of two integer pairs. The first contains the order of the curve and a boolean indicating if it is periodic. If the curve is periodic, it will be clamped (that is, knots of multiplicity = order will exist at each end of the curve). The second contains the dimension of the curve and the number of control points in it. If the dimension is 2, the curve is non-rational; if the dimension is 3 the curve is rational. |
| knotValues[ ] | Array of doubles containing the knot values for all the SP curves in order. The number of knots for each curve is equal to the order of the curve plus the number of control points. |
| ctrlPointCoords[ ] | Array of doubles containing the coordinates of the control points for all the SP curves in order. These are given as a sequence of (U,V) pairs if non-rational, and (U,V,W) triples if rational, where W is the homogeneous coordinate known as the weight. |
| packedDouble8 | Integer pair as follows: the first integer is the total number of trimmed surfaces being output for the given face (the modeler sometimes outputs more than one trimmed surface for a face). The second integer indicates the index of the current trimmed surface being output. All the data in the faceData [] array is for the current trimmed surface. Therefore, if packedDouble8 says there are two trim surfaces, you should use the same Face pointer and call GetTrimCurves2 again to get the data for the second trim surface. |

If b-splines were requested (WantCubic = TRUE), then the underlying Bsurface is also returned. The faceData[ ] array would be as follows:

```vb
[ packedDouble1, packedDouble2[ ], packedDouble3[ ], knotValues[ ], ctrlPointCoords[ ], packedDouble4, packedDouble5, packedDouble6, packedDouble7, surfaceKnotValuesU[ ], surfaceKnotValuesV[ ], surfaceCtrlPointCoords[ ], packedDouble8 ]
```

| packedDouble1 | See definition above. |
| --- | --- |
| packedDouble2[ ] | See definition above. |
| packedDouble3[ ] | See definition above. |
| knotValues[ ] | See definition above. |
| ctrlPointCoords[ ] | See definition above. |
| packedDouble4 | Integer pair containing the dimension of the surface. (3 is non-rational and 4 is rational). The second member of the pair is not used and contains a zero. |
| PackedDouble5 | Integer pair containing the U-order and the V-order of the surface. |
| PackedDouble6 | Integer pair containing the number of control points in U and the number of control points in V |
| packedDouble7 | Integer pair containing booleans indicating if the surface is periodic in U and in V. If the surface is periodic, it will be clamped (that is, knots of multiplicity = order will exist at each end of the surface). |
| surfaceKnotValuesU[ ] | Array of doubles containing the knot values in U for the surface. The number of knots in U is equal to the order in U plus the number of control points in U. |
| surfaceKnotValuesV[ ] | Array of doubles containing the knot values in V as above for U. |
| surfaceCtrlPointCoords[ ] | Array of doubles containing the coordinates of the control points for the surface. These are given as a sequence of (X,Y,Z) triples if non-rational, and (X,Y,Z,W) tuples if rational, where W is the homogeneous coordinate known as the weight. The coordinates are given in row-wise order (V varying most quickly). |
| packedDouble8 | See definition above. |
