---
title: "Face2::GetTrimCurves"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face2/Face2__GetTrimCurves.htm"
---

# Face2::GetTrimCurves

This method is obsolete and has been superseded by [Face2::GetTrimCurves2](sldworksAPI.chm::/Face2/Face2__GetTrimCurves2.htm).

Description

This method gets the trim curves for this face.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face2->GetTrimCurves ( wantCubic, &retval )

| Input: | (VARIANT_BOOL) wantCubic | TRUE if the trim curves are to be cubic, FALSE if not |
| --- | --- | --- |
| Output: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns an array containing the definition of all of the entities that describe a trimmed face. The data is arranged in collections of surface curves (curves defined in the 2D parametric space of the surface, or SP curves) organized into loops (closed composite curves).

All SP curves are returned as b-splines. To control the tolerance of the SP curves, use [Modeler::SetTolerances](../Modeler/Modeler__SetTolerances.htm).

The surface and trim curve parameterization returned by this method might be different from the parameterization returned by other methods, such as [Face::GetUVBounds](../Face/Face__GetUVBounds.htm), Surface::Parameterization, [Edge::GetCurveParams](../Edge/Edge__GetCurveParams.htm), and so on.

If you set wantCubic to TRUE, then this method returns the underlying Bsurface definition. If you want to use the Bsurface in combination with its trim curves, set wantCubic=TRUE because it provides better alignment of the trim curves with the Bsurface because they are generated at the same time.

Each face typically has at least one outer loop and zero or more inner loops. Outer loops define the periphery of the face; inner loops define holes in the face. Outer loops are returned before inner loops if possible. To be certain, use Loop2::IsOuter.

#### Periodic Faces

Periodic faces present many obstacles in translation. As a general rule, it is best to chop up all periodic surfaces by making a call to Body::GetProcessedBody. This method returns a new body to the caller with periodic faces chopped up into multiple faces. Processing this new body, instead of the original body, avoids many of the pitfalls associated with periodics.

If this face is periodic and crosses the seam (0 and 360° location), then this method splits the face into more than one trimmed surface to return this set of data. The first time that this method is called on any face, it returns data for the first trimmed surface on the face. Each subsequent call to this method on the same face returns data for the next trimmed surface, if one exists. See the packedDouble8 parameter to determine the number of surfaces for this face.

To avoid returning multiple surfaces per face, process the body returned from Body::GetProcessedBody.

In addition, using the Body object returned from Body::GetProcessedBody usually prevents returning multiple outer loops when it encounters certain periodic surfaces. In other words, it can prevent generating multiple faces (each with an outer loop) for a particular periodic surface.

#### Edges

If your program calls both [Face::GetEdges](../Face/Face__GetEdges.htm) and this method or to both [Face::EnumEdges](../Face/Face__EnumEdges.htm) and this method, then this method stores a temporary buffer containing the edges for this face. If this temporary buffer exists, then calls to Face::GetEdges or Face::EnumEdges access the buffer. This is beneficial if you are attempting to align the trim curves of the face with their corresponding Edges.

If your call to Face::GetEdges or Face::EnumEdges is made immediately following your call to this method, then the order of the trim curves aligns with the order of the edges. However, if you are processing all the trimcurves and then processing all the edges, your first call to access the edges uses the temporary buffer of edges generated in your last call to this method. Because your last call to this method and your current call to get the edges were probably made from different faces, you will see a mismatch of data. This mismatch of data may been seen when Face::GetEdgeCount does not match the SafeArray size from Face::GetEdges or it may be seen when the edge data does not match the face being examined. Therefore, calls to Face::GetEdges or Face::EnumEdges should be made in the same loop and immediately following your call to Face::GetEdges. The temporary buffer of edges is destroyed after each call to Face::GetEdges or Face::EnumEdges.

There might not be a corresponding edge for each trim curve. This is true for periodic surfaces for which no edge exists along the seam (0 and 360° location), yet this method returns a trim curve. You can detect this situation by comparing the number of edges on the face, [Face::GetEdgeCount](../Face/Face__GetEdgeCount.htm) , with the number of trim (SP) curves on the face, PackedDouble1.

To force edge generation along the seam of a periodic surface, use Body::GetProcessedBody. This method creates a copy of the body with faces and surfaces chopped up. However, there are still certain situations (poles of a surface, cusps on a surface, and so on) in which this method returns a trim curve where no edge exists. In this situation, the list of edges returned from Face::GetEdges or Face::EnumEdges does not align with the list of trim curves. Again, you can detect this by comparing the value returned by Face::GetEdgeCount with PackedDouble1 , but you need to handle matching the edges with their corresponding trim curve.

#### Return Values

The data is returned in a large array of doubles. Integer data is packed among the doubles in pairs.

The format of faceData[] is as follows:

[ packedDouble1, packedDouble2[ ], packedDouble3[ ], knotValues[ ], ctrlPointCoords[ ], packedDouble8 ]

| packedDouble1 | An integer pair containing number of loops and total number of SP curves (trim curves). The length of any edge list generated immediately after a call to GetTrimCurves2 will be equal to the number of SP curves. |
| --- | --- |
| packedDouble2[ ] | Series of integer pairs containing the number of SP curves in each loop; the first integer in each pair represents the number of curves in the odd loops, the second represents the even. The total number of integer pairs here is half the number of loops, rounded up |
| packedDouble3[ ] | For each SP curve, a set of two integer pairs. The first contains the order of the curve and a boolean indicating if it is periodic. If the curve is periodic, it will be clamped (that is, knots of multiplicity = order will exist at each end of the curve). The second contains the dimension of the curve and the number of control points in it. If the dimension is 2, the curve is non-rational; if the dimension is 3 the curve is rational. |
| knotValues[ ] | Array of doubles containing the knot values for all the SP curves in order. The number of knots for each curve is equal to the order of the curve plus the number of control points. |
| ctrlPointCoords[ ] | Array of doubles containing the coordinates of the control points for all the SP curves in order. These are given as a sequence of (U,V) pairs if non-rational, and (U,V,W) triples if rational, where W is the homogeneous coordinate known as the weight. |
| packedDouble8 | Integer pair as follows: the first integer is the total number of trimmed surfaces being output for the given face (the modeler sometimes outputs more than one trimmed surface for a face). The second integer indicates the index of the current trimmed surface being output. All the data in the faceData [] array is for the current trimmed surface. Therefore, if packedDouble8 says there are two trim surfaces, you should use the same Face pointer and call GetTrimCurves2 again to get the data for the second trim surface. |

If b-splines were requested (WantCubic = TRUE), then the underlying Bsurface is also returned. The faceData[ ] array would be as follows:

[ packedDouble1, packedDouble2[ ], packedDouble3[ ], knotValues[ ], ctrlPointCoords[ ], packedDouble4, packedDouble5, packedDouble6, packedDouble7, surfaceKnotValuesU[ ], surfaceKnotValuesV[ ], surfaceCtrlPointCoords[ ], packedDouble8 ]

| packedDouble1 | See previous definition. |
| --- | --- |
| packedDouble2[ ] | See previous definition. |
| packedDouble3[ ] | See previous definition. |
| knotValues[ ] | See previous definition. |
| ctrlPointCoords[ ] | SSee previous definition. |
| packedDouble4 | Integer pair containing the dimension of the surface (3 is non-rational and 4 is rational). The second member of the pair is not used and contains a 0. |
| PackedDouble5 | Integer pair containing the U-order and the V-order of the surface. |
| PackedDouble6 | Integer pair containing the number of control points in U and the number of control points in V |
| packedDouble7 | Integer pair containing BOOLEANs indicating if the surface is periodic in U and in V. If the surface is periodic, it will be clamped (that is, knots of multiplicity = order will exist at each end of the surface). |
| surfaceKnotValuesU[ ] | Array of doubles containing the knot values in U for the surface. The number of knots in U is equal to the order in U plus the number of control points in U. |
| surfaceKnotValuesV[ ] | Array of doubles containing the knot values in V as above for U. |
| surfaceCtrlPointCoords[ ] | Array of doubles containing the coordinates of the control points for the surface. These are given as a sequence of (X,Y,Z) triples if non-rational, and (X,Y,Z,W) tuples if rational, where W is the homogeneous coordinate known as the weight. The coordinates are given in row-wise order (V varying most quickly). |
| packedDouble8 | See previous definition. |
