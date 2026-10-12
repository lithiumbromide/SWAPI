---
title: "GetTrimCurves2 Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetTrimCurves2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.html"
---

# GetTrimCurves2 Method (IFace2)

Gets the definition of all of the entities that describe a trimmed face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrimCurves2( _
   ByVal WantCubic As System.Boolean, _
   ByVal WantNRational As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim WantCubic As System.Boolean
Dim WantNRational As System.Boolean
Dim value As System.Object

value = instance.GetTrimCurves2(WantCubic, WantNRational)
```

### C#

```csharp
System.object GetTrimCurves2(
   System.bool WantCubic,
   System.bool WantNRational
)
```

### C++/CLI

```cpp
System.Object^ GetTrimCurves2(
   System.bool WantCubic,
   System.bool WantNRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubic`: True if the trim curves are to be cubic, false if not
- `WantNRational`: True if the trim curves are to be non-rational, false if not

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Face2::GetTrimCurves2](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetTrimCurves2.html).

## Remarks

This method returns an array containing the definition of all of the entities that describe a trimmed face. The data is arranged in collections of surface curves (curves defined in the 2D parametric space of the surface, or SP-curves) organized into loops (closed composite curves).

All SP-curves are returned as b-splines. To control the tolerance of the SP-curves, use [IModeler::GetToleranceValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~GetToleranceValue.html) or [IModeler::SetToleranceValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~SetToleranceValue.html).

A call to [IFace2::IGetTrimCurveSize2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTrimCurveSize2.html) must precede the call to IFace2::GetTrimCurves2 to get the size of the array required and pre-process the trim curve data.

The surface and trim curve parameterization returned by this method might be different from the parameterization returned by other methods, such as [IFace2::GetUVBounds](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetUVBounds.html), [ISurface::Parameterization](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~Parameterization.html), [IEdge::GetCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurveParams2.html), and so on.

If you set WantCubic to true, then this method returns the underlying Bsurface definition. If you want to use the Bsurface in combination with its trim curves, set WantCubic = True because it provides better alignment of the trim curves with the Bsurface as they are generated at the same time.

Each face typically has at least one outer loop and zero or more inner loops. Outer loops define the periphery of the face; inner loops define holes in the face. Outer loops are returned before inner loops when possible. If you need to be certain, use [ILoop2::IsOuter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IsOuter.html).

##### Periodic Faces

Periodic faces present many obstacles in translation. As a general rule, it is best to chop up all periodic surfaces by making a call to [IBody2::GetProcessedBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetProcessedBody2.html). This method returns a new body to the caller with periodic faces chopped up into multiple faces. Processing this new body, instead of the original body, avoids many of the pitfalls associated with periodics.

If this face is periodic and crosses the "seam" (0 & 360 location), then this method splits the face into more than one trimmed surface for the purposes of returning this set of data. The first time that this method is called on any face, it returns data for the first trimmed surface on the face. Each subsequent call to this function on the same face returns data for the next trimmed surface, if one exists. The packedDouble8 parameter determines the number of surfaces for this face.

To avoid the return of multiple surfaces per face, process the body returned from IBody2::GetProcessedBody2.

Using the Body2 object returned from IBody2::GetProcessedBody2 usually prevents IFace2::GetTrimCurves2 from returning multiple outer loops when it encounters certain periodic surfaces. In other words, it can prevent IFace2::GetTrimCurves2 from generating multiple faces (each with an outer loop) for a particular periodic surface.

##### Edges

If your program uses calls to both [IFace2::GetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetEdges.html) and IFace2::GetTrimCurves2 or to both [IFace2::EnumEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~EnumEdges.html) and Face2::GetTrimCurves2, then:

IFace2::GetTrimCurves2 stores a temporary buffer containing the edges for this face. If this temporary buffer exists, then calls to IFace2::GetEdges or IFace2::EnumEdges access the buffer. This is beneficial if you are attempting to align the trim curves of the face with their corresponding edges.

If your call to IFace2::GetEdges or IFace2::EnumEdges is made immediately following your call to IFace2::GetTrimCurves2, then the order of the trim curves aligns with the order of the edges. However, if you are processing all the trim curves and then processing all the edges, your first call to access the edges uses the temporary buffer of edges generated in your last call to IFace2::GetTrimCurves2.

Because your last call to IFace2::GetTrimCurves2 and your current call to get the edges were probably made from different faces, you will see a mismatch of data. This mismatch of data might be seen when [IFace2::GetEdgeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetEdgeCount.html) does not match the array size from IFace2::GetEdges or it might be seen when the edge data does not match the face being examined. Therefore, calls to IFace2::GetEdges or IFace2::EnumEdges should be made in the same loop and immediately following your call to IFace2::GetEdges. The temporary buffer of edges is destroyed after each call to IFace2::GetEdges or IFace2::EnumEdges.

A corresponding edge for each trim curve might not exist. This is true for periodic surfaces for which no edge exists along the seam (0 and 360), yet this method returns a trim curve. You can detect this situation by comparing the number of edges on the face, IFace2::GetEdgeCount , with the number of trim (SP) curves on the face, PackedDouble1.

To force edge generation along the seam of a periodic surface, use IBody2::GetProcessedBody. This method creates a copy of the body with faces and surfaces chopped up. However, there are still certain situations (poles of a surface, cusps on a surface, and so on) in which this method returns a trim curve where no edge exists. In this situation, the list of edges returned from IFace2::GetEdges or IFace2::EnumEdges does not align with the list of trim curves. Again, you can detect this by comparing the value returned by IFace2::GetEdgeCount with PackedDouble1, but you must handle matching the edges with their corresponding trim curve.

##### Return Values

The data is returned in an array of doubles. Integer data is packed among the doubles in pairs.

The format of faceData[] is as follows:

```vb
[ packedDouble1, packedDouble2[ ], packedDouble3[ ], knotValues[ ], ctrlPointCoords[ ], packedDouble8 ]
```

| packedDouble1 | An integer pair containing number of loops and total number of SP-curves (trim curves). The length of any edge list generated immediately after a call to IFace2::GetTrimCurves2 will be equal to the number of SP-curves. |
| --- | --- |
| packedDouble2[ ] | Series of integer pairs containing the number of SP-curves in each loop. The first integer in each pair represents the number of curves in the odd loops; the second represents the even. The total number of integer pairs is half the number of loops, rounded up |
| packedDouble3[ ] | For each SP-curve, a set of two integer pairs. The first contains the order of the curve and a Boolean indicating if it is periodic. If the curve is periodic, it is clamped (that is, knots of multiplicity = order exists at each end of the curve). The second contains the dimension of the curve and the number of control points in it. If the dimension is 2, then the curve is non-rational; if the dimension is 3, then the curve is rational. NOTE : An SP-curve might be treated as periodic if it is closed and G1 continuous even if the b-spline representation returned is not periodic. For example, the periodic flag returned for the boundary curve of a sheet body with a circle as the boundary loop is true, because the circle is closed and is tangent-continuous at the start/end point, but the data returned for the b-spline representation is in the clamped format, i.e., for a non-periodic b-spline. |
| knotValues[ ] | Array of doubles containing the knot values for all the SP-curves in order. The number of knots for each curve is equal to the order of the curve plus the number of control points. |
| ctrlPointCoords[ ] | Array of doubles containing the coordinates of the control points for all the SP-curves in order. These are given as a sequence of (U,V) pairs if non-rational, and (U,V,W) triples if rational, where W is the homogeneous coordinate known as the weight. |
| packedDouble8 | Integer pair as follows: the first integer is the total number of trimmed surfaces being output for the given face (the modeler sometimes outputs more than one trimmed surface for a face). The second integer indicates the index of the current trimmed surface being output. All the data in the faceData [] array is for the current trimmed surface. Therefore, if packedDouble8 says there are two trim surfaces, you should use the same IFace2 pointer and call IFace2::GetTrimCurves2 again to get the data for the second trim surface. |

If b-splines were requested (WantCubic = True), then the underlying Bsurface is also returned. The faceData[ ] array would be as follows:

```vb
[ packedDouble1, packedDouble2[ ], packedDouble3[ ], knotValues[ ], ctrlPointCoords[ ], packedDouble4, packedDouble5, packedDouble6, packedDouble7, surfaceKnotValuesU[ ], surfaceKnotValuesV[ ], surfaceCtrlPointCoords[ ], packedDouble8 ]
```

| packedDouble1 | See previous definition. |
| --- | --- |
| packedDouble2[ ] | See previous definition. |
| packedDouble3[ ] | See previous definition. |
| knotValues[ ] | See previous definition. |
| ctrlPointCoords[ ] | See previous definition. |
| packedDouble4 | Integer pair containing the dimension of the surface (3 is non-rational and 4 is rational). The second member of the pair is not used and contains a 0. |
| PackedDouble5 | Integer pair containing the U-order and the V-order of the surface. |
| PackedDouble6 | Integer pair containing the number of control points in U and the number of control points in V. |
| packedDouble7 | Integer pair containing Booleans indicating if the surface is periodic in U and in V. If the surface is periodic, it is clamped (that is, knots of multiplicity = order exist at each end of the surface). |
| surfaceKnotValuesU[ ] | Array of doubles containing the knot values in U for the surface. The number of knots in U is equal to the order in U plus the number of control points in U. |
| surfaceKnotValuesV[ ] | Array of doubles containing the knot values in V as above for U. |
| surfaceCtrlPointCoords[ ] | Array of doubles containing the coordinates of the control points for the surface. These are given as a sequence of (X,Y,Z) triples if non-rational, and (X,Y,Z,W) tuples if rational, where W is the homogeneous coordinate known as the weight. The coordinates are given in row-wise order (U varying most quickly). |
| packedDouble8 | See previous definition. |

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetTrimCurveTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopology.html)
[IFace2::GetTrimCurveTopologyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyCount.html)
[IFace2::GetTrimCurveTopologyTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyTypes.html)
[IFace2::IGetTrimCurveSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2.html)
[IFace2::IGetTrimCurveTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopology.html)
[IFace2::IGetTrimCurveTopologyTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopologyTypes.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
