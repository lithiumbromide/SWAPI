---
title: "IEdge Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IEdge_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_methods.html"
---

# IEdge Interface Methods

For a list of all members of this type, see [IEdge members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateWireBody | Creates a wire body from this edge. |
| Method | Display | Highlights this edge with the specified color. |
| Method | EdgeInFaceSense | Checks whether the edge and the loop lying on the specified face have the same direction (sense). |
| Method | EnumCoEdges | Lists the coedges that reference this edge. |
| Method | Evaluate | Obsolete. Superseded by IEdge::Evaluate2 . |
| Method | Evaluate2 | Evaluates the edge for the specified U parameter. |
| Method | GetBody | Gets the body for this edge. |
| Method | GetClosestPointOn | Uses the X,Y,Z input point and returns the closest point on the edge. |
| Method | GetCoEdges | Gets the coedges that reference this edge. |
| Method | GetCurve | Gets the underlying curve for this edge. |
| Method | GetCurveParams | Obsolete. Superseded by IEdge::GetCurveParams2 . |
| Method | GetCurveParams2 | Obsolete. Superseded by IEdge::GetCurveParams3 . |
| Method | GetCurveParams3 | Gets a data object containing the curve parameters for this edge. |
| Method | GetEndVertex | Gets the ending vertex for this edge. |
| Method | GetID | Gets the edge ID of this edge in an imported body. |
| Method | GetParameter | Gets the parameterization of the edge. |
| Method | GetStartVertex | Gets the starting vertex for this edge. |
| Method | GetTangentEdges | Gets all of the edges tangent to this edge. |
| Method | GetTangentEdgesCount | Gets the number of edges tangent to this edge. |
| Method | GetTrackingIDs | Gets the tracking IDs assigned to this edge . |
| Method | GetTrackingIDsCount | Gets the number of tracking IDs on this edge. |
| Method | GetTwoAdjacentFaces | Obsolete. Superseded by IEdge::GetTwoAdjacentFaces2 . |
| Method | GetTwoAdjacentFaces2 | Gets the two faces adjacent to an edge. |
| Method | Highlight | Add highlights or removes highlights from this edge. |
| Method | IEdgeInFaceSense | Obsolete. Superseded by IEdge::IEdgeInFaceSense2 . |
| Method | IEdgeInFaceSense2 | Checks whether the edge and the loop lying on the specified face have the same direction (sense). |
| Method | IEvaluate | Obsolete. Superseded by IEdge::IEvaluate2 . |
| Method | IEvaluate2 | Evaluates the edge for the specified U parameter. |
| Method | IGetClosestPointOn | Uses the X,Y,Z input point and returns the closest point on the edge. |
| Method | IGetCurve | Gets the underlying curve for this edge. |
| Method | IGetCurveParams | Obsolete. Superseded by IEdge::IGetCurveParams2 . |
| Method | IGetCurveParams2 | Returns the curve parameters for this edge, including the edge and curve direction (sense). |
| Method | IGetEndVertex | Gets the ending vertex for this edge. |
| Method | IGetParameter | Gets the parameterization of the edge. |
| Method | IGetStartVertex | Gets the starting vertex for this edge. |
| Method | IGetTangentEdges | Gets all of the edges tangent to this edge. |
| Method | IGetTrackingIDs | Gets the tracking IDs assigned to this edge . |
| Method | IGetTwoAdjacentFaces | Obsolete. Superseded by IEdge::IGetTwoAdjacentFaces2 . |
| Method | IGetTwoAdjacentFaces2 | Gets the two faces adjacent to an edge. |
| Method | IsParamReversed | Gets whether the edge and its underlying curve have the same parameterization or if the direction is reversed. |
| Method | IsTolerant | Gets whether an edge is tolerant and its tolerance value. |
| Method | RemoveId | Removes the edge ID assigned to this edge of an imported body. |
| Method | RemoveRedundantTopology | Removes redundant topology from the edge. |
| Method | RemoveTrackingID | Removes a tracking ID assigned to this edge . |
| Method | SetId | Sets the edge ID of this edge of an imported body. |
| Method | SetTrackingID | Assigns a tracking ID to this edge. |

[Top](#topBookmark)

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
