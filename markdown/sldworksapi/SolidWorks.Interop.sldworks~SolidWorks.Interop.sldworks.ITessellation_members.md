---
title: "ITessellation Interface Members"
project: "SOLIDWORKS API Help"
interface: "ITessellation_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html"
---

# ITessellation Interface Members

The following tables list the members exposed by [ITessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CurveChordAngleTolerance | Gets or sets the maximum angle, in radians, that is allowed between a chord and its originating curve. |
| Property | CurveChordTolerance | Gets or sets the maximum permitted distance from a chord (facet fin) to the curve (edge entity). |
| Property | ImprovedQuality | Gets or sets whether to return higher-quality data. |
| Property | MatchType | Gets or sets the type of Parasolid facet match for the tessellation. |
| Property | MaxFacetWidth | Gets or sets the maximum width of any side of a facet. |
| Property | MinFacetWidth | Gets or sets the minimum facet width for this tessellation. |
| Property | NeedEdgeFinMap | Gets or sets the need edge fin map option. |
| Property | NeedErrorList | Gets or sets the need error list option. |
| Property | NeedFaceFacetMap | Gets or sets the need face facet map option. |
| Property | NeedVertexNormal | Gets or sets the need vertex normal option. |
| Property | NeedVertexParams | Gets or sets the need vertex params option. |
| Property | SurfacePlaneAngleTolerance | Gets or sets the surface plane angle tolerance. |
| Property | SurfacePlaneTolerance | Gets or sets the surface plane tolerance. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetEdgeFins | Gets all of the fin IDs corresponding to a edge. |
| Method | GetErrorList | Gets the tessellation error list. |
| Method | GetFaceFacets | Gets the facets IDs that correspond to a SOLIDWORKS face. |
| Method | GetFacetCount | Gets the number of facets used to create this tessellation. |
| Method | GetFacetFace | Gets a face that corresponds to a facet. |
| Method | GetFacetFins | Gets all of the fin IDs of the fins that border this facet. |
| Method | GetFinCoFin | Gets the ID of the CoFin that is shared by a fin. |
| Method | GetFinCount | Gets the number of fins for this tessellation. |
| Method | GetFinEdge | Gets the edge corresponding to a fin. |
| Method | GetFinVertices | Gets the IDs of the two vertices that correspond to a fin. |
| Method | GetVertexCount | Gets the number of vertices for this tessellation. |
| Method | GetVertexNormal | Gets the information that describes the normal direction corresponding to vertex. |
| Method | GetVertexParams | Gets the parameters corresponding to a tessellation vertex. |
| Method | GetVertexPoint | Gets the X, Y and Z values that describe a tessellation vertex. |
| Method | IGetEdgeFins | Gets all of the fin IDs corresponding to a edge. |
| Method | IGetEdgeFinsCount | Gets the number of fins corresponding to an edge. |
| Method | IGetErrorList | Obsolete. Superseded by ITessellation::IGetErrorList2 . |
| Method | IGetErrorList2 | Gets the tessellation error list. |
| Method | IGetErrorListCount | Gets number of tessellation errors by error type. |
| Method | IGetFaceFacets | Obsolete. Superseded by ITessellation::IGetFaceFacets2 . |
| Method | IGetFaceFacets2 | Gets the facets IDs that correspond to a face. |
| Method | IGetFaceFacetsCount | Obsolete. Superseded by ITessellation::IGetFaceFacetsCount2 . |
| Method | IGetFaceFacetsCount2 | Gets the number of facets corresponding to a face. |
| Method | IGetFacetFace | Obsolete. Superseded by ITessellation::IGetFacetFace2 . |
| Method | IGetFacetFace2 | Gets a face that corresponds to a facet. |
| Method | IGetFacetFins | Gets all of the fin IDs of the fins that border this facet. |
| Method | IGetFacetFinsCount | Gets the number of fins corresponding to a facet. |
| Method | IGetFinEdge | Gets the edge corresponding to a fin. |
| Method | IGetFinVertices | Gets the IDs of the two vertices that correspond to a fin. |
| Method | IGetVertexNormal | Gets the information that describes the normal direction corresponding to vertex. |
| Method | IGetVertexParams | Gets the parameters corresponding to a tessellation vertex. |
| Method | IGetVertexPoint | Gets the X, Y and Z values that describe a tessellation vertex. |
| Method | Tessellate | Performs the tessellation. |

[Top](#topBookmark)

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
