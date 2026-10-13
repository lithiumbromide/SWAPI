---
title: "IBody2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IBody2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html"
---

# IBody2 Interface Members

The following tables list the members exposed by [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Check3 | Gets whether the body is a valid and returns an IFaultEntity object if any faults exist. |
| Property | DisableDisplay | Gets or sets whether to hide or show this body. |
| Property | DisableHighlight | Disables highlighting of the selected body in the graphics area. |
| Property | IMaterialPropertyValues | Obsolete. Superseded by IBody2::IMaterialPropertyValues2 . |
| Property | IMaterialPropertyValues2 | Gets or sets the material properties for a body other than the base body in the active configuration. |
| Property | IsSafe | Not implemented. |
| Property | MaterialPropertyValues | Obsolete. Superseded by IBody2::MaterialPropertyValues2 . |
| Property | MaterialPropertyValues2 | Gets or sets the material properties for a body other than the base body in the active configuration. |
| Property | Name | Gets or sets the name of the selected body. |
| Property | Visible | Gets whether this body is visible or hidden. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddConstantFillets | Creates constant radius fillets on the specified edges on this body. |
| Method | AddProfileArc | Creates an arc profile curve and returns a pointer to that curve. |
| Method | AddProfileBspline | Creates an B-spline profile curve and returns a pointer to that curve. |
| Method | AddProfileBsplineByPts | Adds a profile B-spline. |
| Method | AddProfileLine | Creates a line profile curve and returns a pointer to that curve. |
| Method | AddPropertyExtension | Obsolete. Superseded by IBody2::AddPropertyExtension2 . |
| Method | AddPropertyExtension2 | Adds a property extension to this body. |
| Method | AddVertexPoint | Adds a vertex. |
| Method | ApplyTransform | Applies a transform to this body. |
| Method | Check | Obsolete. Superseded by IBody2::Check3 . |
| Method | Check2 | Obsolete. Superseded by IBody2::Check3 . |
| Method | ConvertToMeshBody | Converts a solid body to a mesh BREP (boundary representation) body. |
| Method | Copy | Obsolete. Superseded by IBody2::Copy2 . |
| Method | Copy2 | Gets a copy of this body. |
| Method | CreateBaseFeature | Creates a base feature for the imported body. |
| Method | CreateBlendSurface | Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces. |
| Method | CreateBodyFromFaces | Creates a temporary body from the faces. |
| Method | CreateBodyFromSurfaces | Creates a body from a list of trimmed surfaces. |
| Method | CreateBoundedSurface | Creates a bounded surface from an independent base surface. |
| Method | CreateBsplineSurface | Creates a new B-spline surface. |
| Method | CreateExtrusionSurface | Creates a new surface of extrusion (infinitely long tabulated cylinder). |
| Method | CreateNewSurface | Creates a handle for a new surface to serve as geometry for a face to be added to the body. |
| Method | CreateOffsetSurface | Creates a new surface offset from an existing surface. |
| Method | CreatePlanarSurface | Creates a new infinite planar surface. |
| Method | CreatePlanarTrimSurfaceDLL | Creates a planar trim surface for this body. |
| Method | CreateRevolutionSurface | Creates a new surface of revolution. |
| Method | CreateRuledSurface | Creates a ruled surface from the specified curves and apex point. |
| Method | CreateTempBodyFromSurfaces | Creates a temporary body from a list of existing trimmed surfaces. |
| Method | CreateTrimmedSurface | Creates a trimmed surface from a base surface and a list of existing trimming curves. |
| Method | DeleteBlends | Obsolete. Superseded by IBody2::DeleteBlends2 . |
| Method | DeleteBlends2 | Obsolete. Superseded by IBody2::DeleteBlends3 . |
| Method | DeleteBlends3 | Removes a set of fillet faces from a temporary body and heals the body. |
| Method | DeleteFaces | Obsolete. Superseded by IBody2::DeleteFaces3 . |
| Method | DeleteFaces2 | Obsolete. Superseded by IBody2::DeleteFaces3 . |
| Method | DeleteFaces3 | Obsolete. Superseded by IBody2::IDeleteFaces4 . |
| Method | DeleteFaces4 | Obsolete. Superseded by IBody2::DeleteFaces5 . |
| Method | DeleteFaces5 | Deletes a set of faces from a temporary body. |
| Method | DeleteFacesMakeSheetBodies | Creates sheet bodies from deleted faces. |
| Method | DeSelect | Deselects this body. |
| Method | Diagnose | Gets the IDiagnoseResult object for this body. |
| Method | Display | Obsolete. Superseded by IBody2::Display3 . |
| Method | Display2 | Obsolete. Superseded by IBody2::Display3 . |
| Method | Display3 | Displays this temporary body in the context of the specified part or component. |
| Method | DisplayWireFrameXOR | Displays a temporary body in the given part's context in XOR mode. |
| Method | DraftBody | Obsolete. Superseded by IBody2::DraftBody2 . |
| Method | DraftBody2 | Adds drafts to the specified faces on a temporary body. This method modifies the body. |
| Method | EnumFaces | Returns an enumerated list of the faces in a body. |
| Method | ExtendSurface | Creates a new temporary body by extending the selected edges. |
| Method | FindAttribute | Finds an attribute on a body. |
| Method | GetBodyBox | Gets the bounding box for this body. |
| Method | GetCoincidenceTransform | Obsolete. Superseded by IBody2::GetCoincidenceTransform2 . |
| Method | GetCoincidenceTransform2 | Calculates the transformation matrix, which would make the input body coincident with this body if the transformation matrix is applied. |
| Method | GetEdgeCount | Gets the number of edges for this body. |
| Method | GetEdges | Gets the edges for this body. |
| Method | GetExcessBodyArray | Gets the excess bodies after sewing. |
| Method | GetExtremePoint | Calculates the extreme point of the model in the specified direction. |
| Method | GetFaceCount | Gets the number of faces in this body. |
| Method | GetFaces | Gets all of the faces on the body. |
| Method | GetFeatureCount | Gets the number of features in this body in a multibody sheet metal part. |
| Method | GetFeatures | Gets the features in this body in a multibody sheet metal part. |
| Method | GetFirstFace | Finds the first face in a body and returns the face. |
| Method | GetFirstSelectedFace | Gets the first selected face on this body. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines. |
| Method | GetGraphicsBody | Gets the graphics body associated with this body. |
| Method | GetIgesErrorCode | Gets the current IGES error code. |
| Method | GetIgesErrorCount | Gets the number of errors encountered while running an IGES routine. |
| Method | GetIntersectionEdges | Obsolete. Superseded by IBody2::GetIntersectionEdges2 . |
| Method | GetIntersectionEdges2 | Gets the edges resulting from the intersection of the specified tool body and this body. |
| Method | GetMassProperties | Gets the mass properties of this body. |
| Method | GetMaterialIdName | Obsolete. Superseded by IBody2::GetMaterialIdName2 . |
| Method | GetMaterialIdName2 | Gets the material name for this body. |
| Method | GetMaterialPropertyName | Gets the names of the material database and the material for the specified configuration. |
| Method | GetMaterialUserName | Obsolete. Superseded by IBody2::GetMaterialUserName2 . |
| Method | GetMaterialUserName2 | Gets the material name for this body; the material name is visible to the user. |
| Method | GetMeshBody | Gets the mesh body associated with this body. |
| Method | GetMiddleSurface | Inserts a midsurface in a body. |
| Method | GetNextSelectedFace | Gets the next selected face. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines. |
| Method | GetOriginalPatternedBody | Gets the original body from this patterned body. Also gets the transformation of this body with respect to the original body. |
| Method | GetProcessedBody | Obsolete. Superseded by IBody2::GetProcessedBody2 . |
| Method | GetProcessedBody2 | Pre-processes the geometry of the body using the specified parameters. |
| Method | GetProcessedBodyWithSelFace | Gets a processed body. |
| Method | GetPropertyExtension | Obsolete. Superseded by IBody2::GetPropertyExtension2 . |
| Method | GetPropertyExtension2 | Gets the specified property extension on this body. |
| Method | GetSafeBody | Not implemented. |
| Method | GetSelectedFaceCount | Gets the number of selected faces on this body. For use with IBody2::GetProcessedBodyWithSelFace and IBody2::IGetPrcoessedBodyWithSelFace and intended for IGES routines. |
| Method | GetSelectedFaces | Gets the selected faces. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines. |
| Method | GetSelectionId | Gets the selection ID of the body, if one exists. |
| Method | GetSheetBody | Gets a sheet (surface) body in this body. |
| Method | GetTessellation | Gets the ITessellation object. |
| Method | GetTexture | Gets the texture applied to this body in the specified configuration. |
| Method | GetTrackingIDs | Gets the tracking IDs assigned to this body . |
| Method | GetTrackingIDsCount | Gets the number of tracking IDs on this body. |
| Method | GetType | Gets the type of the body. |
| Method | GetUpdateStamp | Gets the update stamp for the body as of the last rebuild. |
| Method | GetVertexCount | Gets the number of vertices in this body. |
| Method | GetVertices | Gets the vertices in this body. |
| Method | HasMaterialPropertyValues | Gets whether this body has an appearance. |
| Method | Hide | Hides this temporary body in the context of the specified part. |
| Method | HideBody | Hides or shows this body. |
| Method | IAddProfileArc | Creates an arc profile curve and returns a pointer to that curve. |
| Method | IAddProfileArcDLL | Adds a profile arc. |
| Method | IAddProfileBspline | Creates an B-spline profile curve and returns a pointer to that curve. |
| Method | IAddProfileBsplineByPts | Adds a profile B-spline. |
| Method | IAddProfileBsplineDLL | Adds a profile B-spline. |
| Method | IAddProfileLine | Creates a line profile curve and returns a pointer to that curve. |
| Method | IAddProfileLineDLL | Adds a profile line. |
| Method | IAddVertexPoint | Adds a vertex. |
| Method | ICombineVolumes | Combines the volumes of two bodies. |
| Method | ICopy | Gets a copy of this body. |
| Method | ICreateBaseFeature | Creates a base feature for the imported body. |
| Method | ICreateBlendSurface | Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces. |
| Method | ICreateBodyFromFaces | Creates a temporary body from the faces. |
| Method | ICreateBoundedSurface | Creates a bounded surface from an independent base surface. |
| Method | ICreateBsplineSurface | Creates a new B-spline surface. |
| Method | ICreateBsplineSurfaceDLL | Creates a B-spline surface in this body. |
| Method | ICreateExtrusionSurface | Creates a new surface of extrusion (infinitely long tabulated cylinder). |
| Method | ICreateExtrusionSurfaceDLL | Creates an extruded surface. |
| Method | ICreateNewSurface | Creates a handle for a new surface to serve as geometry for a face to be added to the body. |
| Method | ICreateOffsetSurface | Creates a new surface offset from an existing surface. |
| Method | ICreatePlanarSurface | Creates a new infinite planar surface. |
| Method | ICreatePlanarSurfaceDLL | Creates a planar surface. |
| Method | ICreatePlanarTrimSurfaceDLL | Creates a planar trim surface for this body. |
| Method | ICreatePsplineSurfaceDLL | Creates a B-surface from a piecewise surface. |
| Method | ICreateRevolutionSurface | Creates a new surface of revolution. |
| Method | ICreateRevolutionSurfaceDLL | Creates a surface of revolution for this body. |
| Method | ICreateRuledSurface | Creates a ruled surface from the specified curves and apex point. |
| Method | ICreateTempBodyFromSurfaces | Creates a temporary body from a list of existing trimmed surfaces. |
| Method | IDeleteBlends | Obsolete. Superseded by IBody2::IDeleteBlends2 . |
| Method | IDeleteBlends2 | Obsolete. Superseded by IBody2::DeleteBlends3 . |
| Method | IDeleteBlends3 | Removes a set of fillet faces from a temporary body and heals the body. |
| Method | IDeleteFaces2 | Obsolete. Superseded by IBody2::IDeleteFaces3 . |
| Method | IDeleteFaces3 | Obsolete. Superseded by IBody2::IDeleteFaces4 . |
| Method | IDeleteFacesMakeSheetBodies | Creates sheet bodies from deleted faces. |
| Method | IDeleteFacesMakeSheetBodiesCount | Gets the number of sheet bodies to create from the deleted faces. |
| Method | IDisplay | Obsolete. Superseded by IBody2::Display3 . |
| Method | IDisplayWireFrameXOR | Displays a temporary body in the given part's context in XOR mode. |
| Method | IDraftBody | Obsolete. Superseded by IBody2::IDraftBody2 . |
| Method | IDraftBody2 | Adds drafts to the specified faces on a temporary body. This method modifies the body. |
| Method | IExtendSurface | Creates a new temporary body by extending the selected edges. |
| Method | IGetBodyBox | Gets the bounding box for this body. |
| Method | IGetEdges | Gets the edges for this body. |
| Method | IGetExcessBodyArray | Gets the excess bodies after sewing. |
| Method | IGetExcessBodyCount | Gets the number of excess bodies. |
| Method | IGetFaces | Gets all of the faces on the body. |
| Method | IGetFeatures | Gets the features in this body in a multibody sheet metal part. |
| Method | IGetFirstFace | Finds the first face in a body and returns the face. |
| Method | IGetFirstSelectedFace | Gets the first selected face on this body. For use with IBody2::IGetProcessedBodyWithSelFace and intended for IGES routines. |
| Method | IGetIntersectionEdgeCount | Gets the number of intersecting edges between this body and the specified tool body. |
| Method | IGetIntersectionEdges | Obsolete. Superseded by IBody2::GetIntersectionEdges2 . |
| Method | IGetMassProperties | Gets the mass properties of this body. |
| Method | IGetMaterialPropertyValuesForFace | Gets the color of the specified face. |
| Method | IGetMiddleSurface | Inserts a midsurface in a body. |
| Method | IGetNextSelectedFace | Gets the next selected face. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines. |
| Method | IGetProcessedBody | Obsolete. Superseded by IBody2::GetProcessedBody2 . |
| Method | IGetProcessedBodyWithSelFace | Gets a processed body. |
| Method | IGetSelectedFaces | Gets the selected faces. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines. |
| Method | IGetSheetBody | Gets a sheet (surface) body in this body. |
| Method | IGetTessellation | Gets the ITessellation object. |
| Method | IGetTrackingIDs | Gets the tracking IDs assigned to this body . |
| Method | IGetVertices | Gets the vertices in this body. |
| Method | IHide | Hides a temporary body using the specified part's context. |
| Method | IMatchedBoolean | Obsolete. Superseded by IBody2::IMatchedBoolean3 . |
| Method | IMatchedBoolean2 | Obsolete. Superseded by IBody2::IMatchedBoolean3 . |
| Method | IMatchedBoolean3 | Obsolete. Superseded by IBody2::IMatchedBoolean4 . |
| Method | IMatchedBoolean4 | Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly. |
| Method | IOperations | Obsolete. Superseded by IBody2::Operations2 . |
| Method | IOperations2 | Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies. |
| Method | IRemoveFacesFromSheet | Removes the specified faces from a sheet (surface) body. |
| Method | IRemoveMaterialProperty | Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies. |
| Method | ISave | Saves this body. |
| Method | ISectionBySheet | Sections a body using a sheet (surface) body. |
| Method | ISetCurrentSurface | Places an existing surface into a temporary body that is under construction. |
| Method | ISetXform | Obsolete. Superseded by IBody2::ApplyTransform . |
| Method | IsGraphicsBody | Gets whether this body is a graphics body. |
| Method | IsMeshBody | Gets whether this body is a mesh body. |
| Method | IsPatternSeed | Gets whether this body is the seed of a patterned body. |
| Method | IsSheetMetal | Gets whether this body was created by a sheet metal feature. |
| Method | IsTemporaryBody | Gets whether the body is a temporary body. |
| Method | MakeOffset | Creates a new temporary body by offsetting the selected surface body by the specified distance and in the specified direction. |
| Method | MatchedBoolean | Obsolete. Superseded by IBody2::MatchedBoolean3 . |
| Method | MatchedBoolean2 | Obsolete. Superseded by IBody2::MatchedBoolean3 . |
| Method | MatchedBoolean3 | Obsolete. Superseded by IBody2::MatchedBoolean4 . |
| Method | MatchedBoolean4 | Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly. |
| Method | MinimumRadius | Gets the minimum radius of this body. |
| Method | Negate | Reverses the direction (i.e., orientation) of the body. |
| Method | OffsetPlanarWireBody | Offsets a planar wire body in the normal plane by the specified distance. |
| Method | Operations | Obsolete. Superseded by IBody2::Operations2 . |
| Method | Operations2 | Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies. |
| Method | RemoveFacesFromSheet | Removes the specified faces from a sheet (surface) body. |
| Method | RemoveMaterialProperty | Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies. |
| Method | RemoveRedundantTopology | Removes redundant topology from the body. |
| Method | RemoveTexture | Removes the texture applied to this body in the specified configuration. |
| Method | RemoveTextureByDisplayState | Removes the texture applied to this body in the specified display state. |
| Method | RemoveTrackingID | Removes a tracking ID assigned to this body . |
| Method | ResetEdgeTolerances | Resets the tolerance on all edges of this body. |
| Method | ResetPropertyExtension | Obsolete. Superseded by IBody2::ResetPropertyExtension2 . |
| Method | ResetPropertyExtension2 | Clears all values stored in the property extension. |
| Method | Save | Saves this body. |
| Method | Select | Obsolete. Superseded by IBody2::Select2 . |
| Method | Select2 | Selects this body and marks it. |
| Method | SetCurrentSurface | Places an existing surface into a temporary body that is under construction. |
| Method | SetIgesInfo | Sends IGES-specific data to the geometric modeler. |
| Method | SetMaterialIdName | Obsolete. Superseded by IBody2::SetMaterialIdName2 . |
| Method | SetMaterialIdName2 | Sets the material name for this body. |
| Method | SetMaterialProperty | Sets the material for this body. |
| Method | SetMaterialUserName | Obsolete. Superseded by IBody2::SetMaterialUserName2 . |
| Method | SetMaterialUserName2 | Sets the material name for this body. This material name is visible to the user. |
| Method | SetTexture | Applies texture to this body in the specified configuration. |
| Method | SetTextureByDisplayState | Sets the texture applied to this body in the specified display state. |
| Method | SetTrackingID | Assigns a tracking ID to this body. |
| Method | SetXform | Obsolete. Superseded by IBody2::ApplyTransform . |

[Top](#topBookmark)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IEnumBodies2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.html)
