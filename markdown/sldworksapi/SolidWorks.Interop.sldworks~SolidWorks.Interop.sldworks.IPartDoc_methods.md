---
title: "IPartDoc Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IPartDoc_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_methods.html"
---

# IPartDoc Interface Methods

For a list of all members of this type, see[IPartDoc members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddPropertyExtension | Adds a property extension to this part. |
| Method | Body | Obsolete. Superseded by IPartDoc::GetBodies2 and IPartDoc::EnumBodies3 . |
| Method | CreateExplodedView | Creates an explode view of this multibody part. |
| Method | CreateFeatureFromBody | Obsolete. Superseded by IPartDoc::CreateFeatureFromBody3 . |
| Method | CreateFeatureFromBody2 | Obsolete. Superseded by IPartDoc::CreateFeatureFromBody3 . |
| Method | CreateFeatureFromBody3 | Creates a new imported feature from the specified temporary body. |
| Method | CreateNewBody | Creates a new body to use for import sewing operations and returns it to the caller. |
| Method | CreateSurfaceFeatureFromBody | Creates a surface feature from a body. |
| Method | DeleteEntityName | Deletes the name associated with the specified entity. |
| Method | EditRebuild | Obsolete. Superseded by IModelDoc2::EditRebuild3 . |
| Method | EditRollback | Rolls back the part's history to the feature just before the currently selected feature in the FeatureManager design tree. |
| Method | EditSuppress | Obsolete. Superseded by IModelDoc2::EditSuppress2 . |
| Method | EditUnsuppress | Obsolete. Superseded by IModelDoc2::EditUnsuppress2 . |
| Method | EditUnsuppressDependent | Obsolete. Superseded by IModelDoc2::EditUnsuppressDependent2 . |
| Method | EnumBodies | Obsolete. Superseded by IPartDoc::EnumBodies3 . |
| Method | EnumBodies2 | Obsolete. Superseded by IPartDoc::EnumBodies3 . |
| Method | EnumBodies3 | Enumerates the bodies in this part. |
| Method | EnumRelatedBodies | Obsolete. Superseded by IPartDoc::EnumRelatedBodies2 . |
| Method | EnumRelatedBodies2 | Creates an enumerated list of bodies. |
| Method | EnumRelatedSectionedBodies | Obsolete. Superseded by IPartDoc::EnumRelatedSectionedBodies . |
| Method | EnumRelatedSectionedBodies2 | Gets an enumeration of the related sectioned bodies in a part. |
| Method | ExportFlatPatternView | Obsolete. Superseded by IPartDoc::ExportToDWG2 . |
| Method | ExportToDWG | Obsolete. Superseded by IPartDoc::ExportToDWG2 . |
| Method | ExportToDWG2 | Saves various aspects of a part (sheet metal, faces, loops, and annotation views) to one or more DXF/DWG files, preserving the specified file name. |
| Method | FeatureById | Gets the feature with the specified ID in the part. |
| Method | FeatureByName | Gets the named feature in the part. |
| Method | FeatureExtrusion | Obsolete. Superseded by IFeatureManager::FeatureExtrusion2 . |
| Method | FeatureExtrusion2 | Obsolete. Superseded by IFeatureManager::FeatureExtrusion2 . |
| Method | FeatureExtrusion3 | Obsolete. Superseded by IFeatureManager::FeatureExtrusion2 . |
| Method | FeatureExtrusionThin | Obsolete. Superseded by IFeatureManager::FeatureExtrusionThin2 . |
| Method | FeatureExtrusionThin2 | Obsolete. Superseded by IFeatureManager::FeatureExtrusionThin2 . |
| Method | FeatureExtrusionThin3 | Obsolete. Superseded by IFeatureManager::FeatureExtrusionThin2 . |
| Method | FeatureRevolve | Obsolete. Superseded by IFeatureManager::FeatureRevolve . |
| Method | FeatureRevolve2 | Obsolete. Superseded by IFeatureManager::FeatureRevolve . |
| Method | FeatureRevolveCut | Obsolete. Superseded by IFeatureManager::FeatureRevolveCut . |
| Method | FeatureRevolveThin | Obsolete. Superseded by IFeatureManager::FeatureRevolveThin . |
| Method | FeatureRevolveThin2 | Obsolete. Superseded by IFeatureManager::FeatureRevolveThin . |
| Method | FeatureRevolveThinCut | Obsolete. Superseded by IFeatureManager::FeatureRevolveThinCut . |
| Method | FeatureXpert | Executes FeatureXpert, powered by SOLIDWORKS Intelligent Feature Technology ( SWIFT), in parts. |
| Method | FirstFeature | Gets the first feature in the part. |
| Method | ForceRebuild | Obsolete. Superseded by IModelDoc2::ForceRebuild3 . |
| Method | GetBodies | Obsolete. Superseded by IPartDoc::GetBodies2 . |
| Method | GetBodies2 | Gets the bodies in this part. |
| Method | GetCorresponding | Obsolete. Superseded by IModelDocExtension::GetCorresponding . |
| Method | GetCorrespondingEntity | Obsolete. Superseded by IModelDocExtension::GetCorrespondingEntity . |
| Method | GetEntityByName | Gets an entity (face, edge, vertex) by name. |
| Method | GetEntityName | Gets the name of the specified entity. |
| Method | GetExplodedViewConfigurationName | Gets the name of the configuration for the specified explode view of this multibody part. |
| Method | GetExplodedViewCount | Gets the number of explode views in the specified configuration of this multibody part. |
| Method | GetExplodedViewNames | Gets the names of all the explode views in the specified configuration of this multibody part. |
| Method | GetMateReferenceEntity | Gets the mate reference entity. |
| Method | GetMaterialPropertyName | Obsolete. Superseded by IPartDoc::GetMaterialPropertyName2 . |
| Method | GetMaterialPropertyName2 | Gets the names of the material database and the material for the specified configuration. |
| Method | GetMaterialVisualProperties | Gets the material visual properties for this part. |
| Method | GetNamedEntities | Gets an array of names of named entities (face, edge, vertex, and so on) in this part. |
| Method | GetNamedEntitiesCount | Gets the number of named entities (face, edge, vertex, and so on) in this part. |
| Method | GetPartBox | Gets the box enclosing the part. |
| Method | GetProcessedBody | Obsolete. Superseded by IBody2::GetProcessedBody2 and IPartDoc::IGetProcessedBody2 . |
| Method | GetPropertyExtension | Gets the specified property extension on this part document. |
| Method | GetRelatedBodies | Creates a list of all the related bodies in a part. |
| Method | GetRelatedSectionedBodies | Gets all of the related sectioned bodies in a part. |
| Method | GetSectionedBody | Gets the sectioned body seen in the specified drawing view. |
| Method | GetTessNorms | Gets the normal vector for each of the triangles, which make up the shaded picture tessellation. |
| Method | GetTessTriangleCount | Gets the number of triangles that make up the shaded picture tessellation for this part. |
| Method | GetTessTriangles | Gets the triangles that make up the shaded picture tessellation for this part. |
| Method | GetTessTriStripEdges | Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part. |
| Method | GetTessTriStripNorms | Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this part. |
| Method | GetTessTriStrips | Gets the vertices that make up the shaded picture tessellation for this part. |
| Method | GetTessTriStripSize | Gets the size of the array floats required to contain the data returned when calling IPartDoc::GetTessTriStrips and IPartDoc::IGetTessTriStrips . |
| Method | GetTessTriStripTextures | Gets the texture coordinate components for each vertex on each triangle strip on each face of this part. |
| Method | IBodyObject | Obsolete. Superseded by IPartDoc::GetBodies2 and IPartDoc::EnumBodies3 . |
| Method | IBodyObject2 | Obsolete. Superseded by IPartDoc::GetBodies2 and IPartDoc::EnumBodies3 . |
| Method | ICreateFeatureFromBody | Obsolete. Superseded by IPartDoc::ICreateFeatureFromBody4 . |
| Method | ICreateFeatureFromBody2 | Obsolete. Superseded by IPartDoc::ICreateFeatureFromBody4 . |
| Method | ICreateFeatureFromBody3 | Obsolete. Superseded by IPartDoc::ICreateFeatureFromBody4 . |
| Method | ICreateFeatureFromBody4 | Creates a new imported feature from the specified temporary body. |
| Method | ICreateNewBody | Obsolete. Superseded by IPartDoc::ICreateNewBody2 . |
| Method | ICreateNewBody2 | Creates a new body to use for import sewing operations and returns it to the caller. |
| Method | ICreateSurfaceFeatureFromBody | Creates a surface feature from a body. |
| Method | ICreateSurfaceFeatureFromBodyCount | Obsolete. Superseded by IPartDoc::ICreateSurfaceFeatureFromBodyCount2 . |
| Method | ICreateSurfaceFeatureFromBodyCount2 | Gets the number of surface features to create from the body. |
| Method | IDeleteEntityName | Deletes the name associated with the specified entity. |
| Method | IExportToDWG | Obsolete. Superseded by IPartDoc::IExportToDWG2 . |
| Method | IExportToDWG2 | Saves various aspects of a part (sheet metal, faces, loops, and annotation views) to one or more DXF/DWG files, preserving the specified filename. |
| Method | IFeatureById | Gets the feature with the specified ID in the part. |
| Method | IFeatureByName | Gets the named feature in the part. |
| Method | IFirstFeature | Gets the first feature in the part. |
| Method | IGetCorrespondingEntity | Obsolete. Superseded by IModelDocExtension::GetCorrespondingEntity . |
| Method | IGetEntityByName | Gets an entity (face, edge, vertex) by name. |
| Method | IGetEntityName | Gets the name of the specified entity. |
| Method | IGetNamedEntities | Gets an array of names of named entities (face, edge, vertex, and so on) in this part. |
| Method | IGetPartBox | Gets the box enclosing the part. |
| Method | IGetProcessedBody | Obsolete. Superseded by IPartDoc::IGetProcessedBody2 . |
| Method | IGetProcessedBody2 | Pre-processes the geometry of a body so that: Closed periodic faces (for example, the lateral face of a cylinder) are split into two faces. Faces that straddle the seam, if any, of the underlying surface are split into two faces. |
| Method | IGetProcessedBodyWithSelFace | Obsolete. Superseded by IPartDoc::IGetProcessedBodyWithSelFace2 . |
| Method | IGetProcessedBodyWithSelFace2 | Gets a processed body. |
| Method | IGetSectionedBody | Obsolete. Superseded by IPartDoc::IGetSectionedBody2 . |
| Method | IGetSectionedBody2 | Gets the sectioned body seen in the specified drawing view. |
| Method | IGetTessNorms | Gets the normal vector for each of the triangles, which make up the shaded picture tessellation. |
| Method | IGetTessTriangles | Gets the triangles that make up the shaded picture tessellation for this part. |
| Method | IGetTessTriStripEdges | Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part. |
| Method | IGetTessTriStripEdgeSize | Gets the size of the array returned by IPartDoc::GetTessTriStripEdges and IPartDoc::IGetTessTriStripEdges . |
| Method | IGetTessTriStripNorms | Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this part. |
| Method | IGetTessTriStrips | Gets the vertices that make up the shaded picture tessellation for this part. |
| Method | ImportDiagnosis | Diagnoses and repairs any gaps or bad faces on imported features. |
| Method | ImportDiagnosisGapCloser | Allows you to repair a gap by moving the vertices on the edges surrounding the gap to new positions to close the gap on the imported model. |
| Method | InsertBasePart | Obsolete. Superseded by IPartDoc::InsertPart . |
| Method | InsertBendNotes | Inserts bend notes for the specified flat-pattern feature of this sheet metal part. |
| Method | InsertBends | Obsolete. Superseded by IPartDoc::InsertBends2 . |
| Method | InsertBends2 | Creates bends in a thin-feature part. |
| Method | InsertBendTable | Creates a bend table annotation for the flat pattern of this sheet metal part. |
| Method | InsertImportedFeature | Inserts a third-party native CAD file into this part. |
| Method | InsertMirrorAll | Mirrors the part about a selected planar face. |
| Method | InsertMirrorFeature | Obsolete. Superseded by IFeatureManager::InsertMirrorFeature . |
| Method | InsertPart | Obsolete. Superseded by IPartDoc::InsertPart2 . |
| Method | InsertPart2 | Obsolete. Superseded by IPartDoc::InsertPart3 . |
| Method | InsertPart3 | Inserts the specified part in the specified configuration into this part. |
| Method | ISetEntityName | Sets the name of the entity if the entity does not have a name. |
| Method | IsMirrored | Gets whether this part is mirrored. |
| Method | IsWeldment | Gets whether this part contains a weldment feature. |
| Method | MakeSection | Saves sketch profiles for use in the wizard. |
| Method | MirrorFeature | Displays a dialog that allows the end-user to mirror a feature about a selected plane or planar face. |
| Method | MirrorPart | Obsolete. Superseded by IPartDoc::MirrorPart2 . |
| Method | MirrorPart2 | Creates a new part document that mirrors this part about a selected reference plane or planar face. |
| Method | RemoveAllDisplayStates | Removes all display states and appearances from this part document. |
| Method | ReorderFeature | Reorders features and their operations. |
| Method | ResetPropertyExtension | Clears all values stored in the property extension. |
| Method | SaveToFile | Obsolete. Superseded by IPartDoc::SaveToFile2 . |
| Method | SaveToFile2 | Obsolete. Superseded by IPartDoc::SaveToFile3 . |
| Method | SaveToFile3 | Saves the selected weldment member, surface body, or solid body to another part document. |
| Method | SetCosmosWorksMaterial | Assigns the material to use during analysis to this part. |
| Method | SetDroppedFileName | Sets the filename for a recently dropped file. |
| Method | SetEntityName | Sets the name of the entity if the entity does not have a name and the name is unique to the part. |
| Method | SetLineColor | Sets the color for the lines in the part document. |
| Method | SetLineStyle | Sets the style or font for the lines in the part document. |
| Method | SetLineWidth | Sets the thickness or weight for the lines in the part document. |
| Method | SetMaterialPropertyName | Obsolete. Superseded by IPartDoc::SetMaterialPropertyName2 . |
| Method | SetMaterialPropertyName2 | Sets the name of the material property for the specified configuration. |
| Method | SetMaterialVisualProperties | Sets the material visual properties for the active configuration and any specified configurations of this part. |
| Method | ShowExploded | Displays the specified explode view for this multibody part. |

[Top](#topBookmark)

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
