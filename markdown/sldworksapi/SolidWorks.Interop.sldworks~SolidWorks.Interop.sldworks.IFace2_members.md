---
title: "IFace2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IFace2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html"
---

# IFace2 Interface Members

The following tables list the members exposed by[IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Check | Checks whether the face is a valid, and, if not, returns the faults. |
| Property | IMaterialPropertyValues | Gets or sets the material properties for the selected face in the active configuration. |
| Property | INormal | Gets the unit normal vector for any planar face. NOTE: This property is a get-only property. Set is not implemented . |
| Property | MaterialIdName | Gets or sets the material name. |
| Property | MaterialPropertyValues | Gets or sets the material properties for the selected face in the active configuration. |
| Property | MaterialUserName | Gets or sets the material name, which is visible to the user. |
| Property | Normal | Gets the unit normal vector for any planar face. NOTE: This property is a get-only property. Set is not implemented . |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddPropertyExtension | Adds a property extension to this face. |
| Method | AttachSurface | Attaches a surface to this face. |
| Method | CreateSheetBody | Creates a sheet body from this face. |
| Method | CreateSheetBodyByFaceExtension | Creates a sheet body by extending the face. |
| Method | DetachSurface | Detaches a surface from this face. |
| Method | EnumEdges | Enumerates the edges in a face. |
| Method | EnumLoops | Enumerates the loops in a face. |
| Method | FaceInSurfaceSense | Checks whether the face normal has the opposite direction (sense) as the underlying surface. |
| Method | GetAllAssemblyDecalProperties | Gets all of the decal properties applied to this face in an assembly component. |
| Method | GetAllDecalProperties | Gets all of the decal properties applied to this face in a part. |
| Method | GetArea | Gets the area of this face. |
| Method | GetBody | Gets the body containing this face. |
| Method | GetBox | Gets the box boundaries for this face. |
| Method | GetClosestPointOn | Uses the X,Y,Z input point to determine the closest point on the face. |
| Method | GetDecalsCount | Gets the number of decals applied to this face. |
| Method | GetEdgeCount | Gets the number of the edges that bound this face. |
| Method | GetEdges | Get the edges bounding this face. |
| Method | GetFaceId | Gets the face ID of an imported body. |
| Method | GetFeature | Gets the feature that owns this face. |
| Method | GetFeatureId | Gets the order number for the owning feature of this face. |
| Method | GetFirstLoop | Gets the first loop in this face, which is not necessarily the outer loop. |
| Method | GetLoopCount | Gets the number of loops in this face. |
| Method | GetLoops | Gets all of the loops on this face. |
| Method | GetMaterialPropertyValues2 | Gets the material property values for this face. |
| Method | GetNextFace | Gets the next face in a body. |
| Method | GetPatternSeedFeature | Gets the seed feature of a pattern. |
| Method | GetProjectedPointOn | Gets the point where the input point is projected on to this face. |
| Method | GetPropertyExtension | Gets the property extension on this face. |
| Method | GetSeedFeature | Gets the seed feature of a patterned, mirrored, or copied body for this face. |
| Method | GetShellType | Gets the shell type for this face. |
| Method | GetSilhoutteEdges | Obsolete. Superseded by IFace2::GetSilhoutteEdgesVB . |
| Method | GetSilhoutteEdgesVB | Gets the silhouette edges. |
| Method | GetSurface | Gets the surface referenced by this face. |
| Method | GetTessNorms | Gets the normal vector for each of the triangles that make up the shaded picture tessellation. |
| Method | GetTessTextures | Gets the texture coordinates for the triangles. |
| Method | GetTessTriangleCount | Gets the number of triangles that make up the shaded picture tessellation for this face. |
| Method | GetTessTriangles | Gets the triangles that make up the shaded picture tessellation for this face. |
| Method | GetTessTriStripEdges | Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face. |
| Method | GetTessTriStripNorms | Gets the normal vector for each of the triangles that make up the shaded picture tessellation for this face. |
| Method | GetTessTriStrips | Gets the vertices that make up the shaded picture tessellation for this face. |
| Method | GetTessTriStripSize | Gets the array size required for IFace2::GetTessTriStrips and IFace2::IGetTessTriStrips . |
| Method | GetTessTriStripTextures | Gets the texture coordinate components for each vertex on each triangle strip on this face. |
| Method | GetTexture | Gets the texture applied to this face in the specified configuration. |
| Method | GetTrackingIDs | Gets the tracking IDs assigned to this face . |
| Method | GetTrackingIDsCount | Gets the number of tracking IDs on this face. |
| Method | GetTrimCurves | Obsolete. Superseded by IFace2::GetTrimCurves2 . |
| Method | GetTrimCurves2 | Gets the definition of all of the entities that describe a trimmed face. |
| Method | GetTrimCurveTopology | Gets the trim curve topology for this face. |
| Method | GetTrimCurveTopologyCount | Gets the number of elements in the trim curve topology for this face. |
| Method | GetTrimCurveTopologyTypes | Gets the types of elements in the trim curve topology for this face. |
| Method | GetUVBounds | Gets the values that describe the U, V bounds of this face. |
| Method | HasMaterialPropertyValues | Gets whether this face has an appearance. |
| Method | HasTextureCoordinates | Gets whether this face has texture coordinates. |
| Method | Highlight | Adds highlighting to or removes highlighting from a face. |
| Method | ICreateSheetBody | Creates a sheet body from this face. |
| Method | ICreateSheetBodyByFaceExtension | Creates a sheet body by extending the face. |
| Method | IGetAllDecalProperties | Gets the decal properties applied to this face. |
| Method | IGetBody | Gets the body containing this face. |
| Method | IGetBox | Gets the box boundaries for this face. |
| Method | IGetClosestPointOn | Uses the X,Y,Z input point to determine the closest point on the face. |
| Method | IGetDecalProperties | Gets the properties of the specified decal on this face. |
| Method | IGetEdges | Get the edges bounding this face. |
| Method | IGetFacetData | Obsolete. Superseded by IFace2::GetTessNorms , IFace2::IGetTessNorms , IFace2::GetTessTextures , IFace2::IGetTessTextures, IFace2::GetTessTriangleCount, IFace2::GetTessTriangles, IFace2::IGetTessTriangles , IFace2::GetTessTriStripEdges , IFace2::IGetTessTriStripEdges , IFace::GetTessTriStripNorms , IFace2::IGetTessTriStripNorms , IFace2::GetTessTriStrips , and IFace2::IGetTessTriStrips . |
| Method | IGetFeature | Gets the feature that owns this face. |
| Method | IGetFirstLoop | Gets the first loop in this face, which is not necessarily the outer loop. |
| Method | IGetLoops | Gets all of the loops on this face. |
| Method | IGetMaterialPropertyValues2 | Gets the material property values for this face. |
| Method | IGetNextFace | Gets the next face in a body. |
| Method | IGetPatternSeedFeature | Gets the seed feature of a pattern. |
| Method | IGetSilhoutteEdgeCount | Gets the number of silhouette edges for this face. |
| Method | IGetSilhoutteEdges | Gets the silhouette edges for this face with the specified root point and in the specified direction. |
| Method | IGetSurface | Gets the surface referenced by this face. |
| Method | IGetTessNorms | Gets the normal vector for each of the triangles that make up the shaded picture tessellation. |
| Method | IGetTessTextures | Gets the texture coordinates for the triangles. |
| Method | IGetTessTriangles | Gets the triangles that make up the shaded picture tessellation for this face. |
| Method | IGetTessTriStripEdges | Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face. |
| Method | IGetTessTriStripEdgeSize | Gets the size of the array returned by IFace2::GetTessTriStripEdges and IFace2::IGetTessTriStripEdges . |
| Method | IGetTessTriStripNorms | Gets the normal vector for each of the triangles that make up the shaded picture tessellation for this face. |
| Method | IGetTessTriStrips | Gets the vertices that make up the shaded picture tessellation for this face. |
| Method | IGetTrackingIDs | Gets the tracking IDs assigned to this face . |
| Method | IGetTrimCurveSize | Obsolete. Superseded by IFace2::IGetTrimCurveSize2 . |
| Method | IGetTrimCurveSize2 | Gets the size of the array required for IFace2::GetTrimCurves2 |
| Method | IGetTrimCurveTopology | Gets the trim curve topology for this face. |
| Method | IGetTrimCurveTopologyTypes | Gets the trim curve topology type array for this face. |
| Method | IGetUVBounds | Gets the values that describe the U, V bounds of this face. |
| Method | IHighlight | Adds highlighting to or removes highlighting from a face. |
| Method | IImprintCurve | Imprints a curve on the selected face. |
| Method | IIsCoincident | Gets whether this face and the specified face, which is located on a different body, are coincident. |
| Method | IIsSame | Gets whether the two faces are the same. |
| Method | ImprintCurve | Imprints a curve on the selected face. |
| Method | ImprintCurveCount | Gets the number of new edges and faces to create when imprinting a curve. |
| Method | IRemoveInnerLoops | Removes the inner loops on this face if the face is from a sheet (surface) body. |
| Method | IRemoveMaterialProperty2 | Removes the material property values from this face. |
| Method | IReverseEvaluate | Gets the UV parameters for the given XYZ location on this face. |
| Method | IsCoincident | Gets whether this face and the specified face, which is located on a different body, are coincident. |
| Method | ISetMaterialPropertyValues2 | Sets the material property values for this face. |
| Method | IsSame | Gets whether the two faces are the same. |
| Method | RemoveFaceId | Removes the face ID on an imported body. |
| Method | RemoveInnerLoops | Removes the inner loops on this face if the face is from a sheet (surface) body. |
| Method | RemoveMaterialProperty | Obsolete. Superseded by IFace2::RemoveMaterialProperty2 . |
| Method | RemoveMaterialProperty2 | Removes the material property values from this face. |
| Method | RemoveRedundantTopology | Removes redundant topology from the face. |
| Method | RemoveTexture | Obsolete. Superseded by IFace2::RemoveTexture2 . |
| Method | RemoveTexture2 | Removes the texture applied to this face in the specified configuration. |
| Method | RemoveTextureByDisplayState | Removes the texture applied to this face in the specified display state. |
| Method | RemoveTrackingID | Removes a tracking ID assigned to this face . |
| Method | ResetPropertyExtension | Clears all values stored in the property extension. |
| Method | ReverseEvaluate | Gets the UV parameters for the given XYZ location on this face. |
| Method | SetFaceId | Sets the face ID on an imported body. |
| Method | SetMaterialPropertyValues2 | Sets the material property values for this face. |
| Method | SetTexture | Applies texture to this face in the specified configuration. |
| Method | SetTextureByDisplayState | Applies texture to this face in the specified display state. |
| Method | SetTrackingID | Assigns a tracking ID to this face. |

[Top](#topBookmark)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
