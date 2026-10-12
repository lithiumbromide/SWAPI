---
title: "IComponent2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IComponent2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html"
---

# IComponent2 Interface Members

The following tables list the members exposed by [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ComponentReference | Gets or sets a component reference for this component. |
| Property | CustomPropertyManager | Gets the configuration-specific custom property manager for this assembly component. |
| Property | DisplayTitle | Gets this component's title as displayed in the FeatureManager design tree. |
| Property | ExcludeFromBOM | Obsolete. Superseded by IComponent2::GetExcludeFromBOM2 and IComponent2::SetExcludeFromBOM2 . |
| Property | IMaterialPropertyValues | Gets or sets the material properties for the selected component in the active configuration. |
| Property | IsGraphicsOnly | Gets whether this component is graphics only. |
| Property | IsSpeedPak | Gets whether the active configuration for this component is SpeedPak. |
| Property | IsVirtual | Gets whether this component is a virtual component. NOTE: This property is a get-only property. Set is not implemented . |
| Property | MaterialPropertyValues | Gets or sets the material properties for the selected component in the active configuration. |
| Property | Name | Obsolete. Superseded by IComponent2::Name2 . |
| Property | Name2 | Gets or sets the name of the selected component. |
| Property | PresentationTransform | Gets or sets the component transform. |
| Property | ReferencedConfiguration | Gets or sets the active configuration used by this component. |
| Property | ReferencedDisplayState | Obsolete. Superseded by IComponent2::ReferencedDisplayState2 . |
| Property | ReferencedDisplayState2 | Gets or sets the active display state of this component. |
| Property | Solving | Gets the Solve as option (rigid or flexible) of this component. |
| Property | Transform | Obsolete. Superseded by IComponent2::Transform2 . |
| Property | Transform2 | Gets or sets the component transform. |
| Property | UseNamedConfiguration | Gets whether a specified configuration or the in-use/last active configuration is used. |
| Property | Visible | Gets or sets the visibility state of this component. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddPropertyExtension | Adds a property extension to this component. |
| Method | DeSelect | Deselects this component. |
| Method | EnumBodies | Obsolete. Superseded by IComponent2::EnumBodies2 . |
| Method | EnumBodies2 | Obsolete. Superseded by IComponent2::EnumBodies3 . |
| Method | EnumBodies3 | Gets the bodies in the component in a multibody part. |
| Method | EnumRelatedBodies | Creates an enumerated list of bodies. |
| Method | EnumSectionedBodies | Gets the sectioned bodies seen in the specified view and returns them in an enumerated list. |
| Method | FeatureByName | Gets the specified feature for this component. |
| Method | FindAttribute | Finds an attribute on a component. |
| Method | FirstFeature | Gets the first feature in this component. |
| Method | GetBodies | Obsolete. Superseded by IComponent2::GetBodies2 . |
| Method | GetBodies2 | Obsolete. Superseded by IComponent2::GetBodies3 . |
| Method | GetBodies3 | Gets the bodies in this component. |
| Method | GetBody | Gets the body that belongs to this instance of this component. |
| Method | GetBox | Gets the bounding box for component. |
| Method | GetChildren | Gets all of the children components of this component. |
| Method | GetConfigurationCount | Gets the number of configurations for this lightweight assembly component. |
| Method | GetConfigurationNames | Gets the names of configurations for this lightweight assembly component. |
| Method | GetConstrainedStatus | Gets the constrained status of this component. |
| Method | GetCorresponding | Gets the corresponding object in the context of the assembly for a specific instance of the component. |
| Method | GetCorrespondingEntity | Gets the entity that corresponds with the Dispatch pointer in the context of the component. |
| Method | GetDecals | Gets the decals applied to this component. |
| Method | GetDecalsCount | Gets the number of decals applied to this component. |
| Method | GetDrawingComponent | Gets the drawing component for this component. |
| Method | GetExcludeFromBOM2 | Gets whether this component is excluded from the bills of materials (BOMs) in the specified configurations. |
| Method | GetHiddenUnloadedChildrenCount | Gets the number of hidden children components of this component that were not loaded when an assembly was opened selectively . |
| Method | GetID | Gets the component ID for this component. |
| Method | GetImportedPath | Gets the full path name of the model imported for this component. |
| Method | GetMaterialIdName | Gets the material name for this component. |
| Method | GetMaterialPropertyValues2 | Gets the material properties for this component. |
| Method | GetMaterialUserName | Gets the user-visible name of the material for this component. |
| Method | GetMates | Gets the mates for this component. |
| Method | GetModelDoc | Obsolete. Superseded by IComponent2::GetModelDoc2 . |
| Method | GetModelDoc2 | Gets the model document for this component. |
| Method | GetModelMaterialPropertyValues | Gets the material properties of this lightweight component in the specified configuration. |
| Method | GetModelTexture | Gets the texture applied to this lightweight component in the specified configuration. |
| Method | GetParent | Gets the parent component. |
| Method | GetPathName | Gets the full path name for this component. |
| Method | GetPLMID | Gets the ID of this SOLIDWORKS Design connected to the 3DEXPERIENCE platform document. |
| Method | GetPropertyExtension | Gets the property extension on this component. |
| Method | GetReferencedDisplayStates | Gets the display states of this component that are referenced by the specified assembly display state(s). |
| Method | GetRenderMaterials | Obsolete. Superseded by IComponent2::GetRenderMaterials2 . |
| Method | GetRenderMaterials2 | Gets the appearances applied to this component in the specified display states. |
| Method | GetRenderMaterialsCount | Obsolete. Superseded by IComponent2::GetRenderMaterialsCount2 . |
| Method | GetRenderMaterialsCount2 | Gets the number of appearances applied to this component in the specified display states. |
| Method | GetRepresentationParent | Gets the representation parent of this SOLIDWORKS Design connected to the 3DEXPERIENCE platform document. |
| Method | GetSectionedBodies | Gets the sectioned bodies in the specified section view. |
| Method | GetSelectByIDString | Gets the name of the component for possible use with IModelDocExtension::SelectByID2 , for selectively opening a document using ISldWorks::OpenDoc7 and IDocumentSpecification , etc. |
| Method | GetSmartComponentData | Gets the features, components, and feature references of a Smart Component. |
| Method | GetSpecificTransform | Get the collapsed or exploded transform of a component when the assembly is exploded. |
| Method | GetSuppression | Obsolete. Superseded by IComponent2::GetSuppression2 . |
| Method | GetSuppression2 | Gets the suppression state of this component. |
| Method | GetTessNorms | Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component. |
| Method | GetTessTriangles | Gets the triangles that make up the shaded picture tessellation for this component. |
| Method | GetTessTriStripEdges | Gets the edge IDs for the triangle strips. |
| Method | GetTessTriStripNorms | Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component. |
| Method | GetTessTriStrips | Gets the vertices that make up the shaded picture tessellation for this component. |
| Method | GetTexture | Gets the texture applied to this component in the specified configuration. |
| Method | GetTotalTransform | Combines the original transform of this component with the presentation transform of this component. |
| Method | GetType | Gets this lightweight assembly component's document type. |
| Method | GetUnloadedComponentNames | Gets the component's unloaded children components' path names, referenced configuration names, reasons why they are unloaded, document types, and names. |
| Method | GetVisibility | Gets the visibility state for this component. |
| Method | GetVisibilityInAsmDisplayStates | Gets the visibilities of this component in the specified assembly display state(s). |
| Method | GetXform | Obsolete. Superseded by IComponent2::Transform2 . |
| Method | HasAssemblyFeatures | Gets whether this component has assembly features in the specified configuration. |
| Method | HasMaterialPropertyValues | Gets whether this component has an appearance. |
| Method | HasUnloadedComponents | Gets whether this component has hidden or suppressed unloaded children components. |
| Method | IFindAttribute | Finds an attribute on a component. |
| Method | IGetBody | Gets the body that belongs to this instance of this component. |
| Method | IGetBox | Gets the bounding box for component. |
| Method | IGetChildren | Gets all of the children components of this component. |
| Method | IGetChildrenCount | Gets the number of children components for this component. |
| Method | IGetCorrespondingEntity | Gets the entity that corresponds with the Dispatch pointer in the context of the component. |
| Method | IGetDecals | Gets the decals applied to this component. |
| Method | IGetMaterialPropertyValues2 | Gets the material properties for this component. |
| Method | IGetMaterialPropertyValuesForFace | Gets the color of the specified face. |
| Method | IGetModelDoc | Obsolete. Superseded by IComponent2::GetModelDoc2 . |
| Method | IGetModelMaterialPropertyValues | Gets the material properties of this lightweight component in the specified configuration. |
| Method | IGetRenderMaterials | Obsolete. Superseded by IComponent2::GetRenderMaterials2 . |
| Method | IGetTemporaryBodyID | Gets the current body tag ID, which is not a permanent ID. |
| Method | IGetTessNorms | Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component. |
| Method | IGetTessTriangleCount | Gets the number of triangles that make up the shaded picture tessellation for this component. |
| Method | IGetTessTriangles | Gets the triangles that make up the shaded picture tessellation for this component. |
| Method | IGetTessTriStripEdges | Gets the edge IDs for the triangle strips. |
| Method | IGetTessTriStripEdgeSize | Gets the number of tessellation triangle edges. |
| Method | IGetTessTriStripNorms | Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component. |
| Method | IGetTessTriStrips | Gets the vertices that make up the shaded picture tessellation for this component. |
| Method | IGetTessTriStripSize | Gets the array size of floats required to contain the data returned when calling IComponent2::IGetTessTriStrips . |
| Method | IGetVisibility | Gets the visibility state for this component. |
| Method | IGetXform | Obsolete. Superseded by IComponent2::Transform2 . |
| Method | IListExternalFileReferences | Obsolete. Superseded by IComponent2::IListExternalFileReferences2 . |
| Method | IListExternalFileReferences2 | Gets the names and statuses of the external references on the component. |
| Method | IRemoveMaterialProperty2 | Removes material property values from the component. |
| Method | IsDisplayDataOutOfDate | Gets the status of the display data for this component. |
| Method | IsEnvelope | Gets whether this component is an envelope. |
| Method | ISetMaterialPropertyValues2 | Sets the material properties for this component. |
| Method | ISetVisibility | Sets the visibility state for this component. |
| Method | ISetXform | Obsolete. Superseded by IComponent2::Transform2 . |
| Method | ISetXformAndSolve | Obsolete. Superseded by IComponent2::SetTransformAndSolve2 . |
| Method | IsFixed | Gets whether the component is fixed or floating. |
| Method | IsHidden | Gets whether this component is hidden or suppressed. |
| Method | IsLoaded | Gets whether a component is loaded. |
| Method | IsMirrored | Gets whether this component is mirrored. |
| Method | IsNameOverridden | Gets whether this component's name is overridden. |
| Method | IsPatternInstance | Gets whether the component is a member of a pattern instance. |
| Method | IsRoot | Gets whether this component is the root component. |
| Method | IsSmartComponent | Gets whether this component is a Smart Component. |
| Method | IsSuppressed | Gets whether this component is suppressed. |
| Method | ListExternalFileReferences | Obsolete. Superseded by IComponent2::ListExternalFileReferences2 . |
| Method | ListExternalFileReferences2 | Gets the names and statuses of the external file references on the component. |
| Method | ListExternalFileReferencesCount | Gets the number of external references on the component. |
| Method | MakeVirtual | Obsolete. by Superseded by IComponent2::MakeVirtual2 . |
| Method | MakeVirtual2 | Makes this component and optionally its child components virtual by saving them in the current assembly. |
| Method | RemoveMaterialProperty | Obsolete. Superseded by IComponent2::RemoveMaterialProperty2 . |
| Method | RemoveMaterialProperty2 | Removes the appearance from the component. |
| Method | RemovePresentationTransform | Removes the presentation transform from this component. |
| Method | RemoveTexture | Removes the texture from this component in the specified configuration. |
| Method | RemoveTextureByDisplayState | Removes the texture applied to this component in the specified display state. |
| Method | ReplaceReference | Obsolete. Superseded by AssemblyDoc::ReplaceComponents . |
| Method | ResetPropertyExtension | Clears all of the values stored in the property extension. |
| Method | SaveVirtualComponent | Saves a virtual component to an external file. |
| Method | Select | Obsolete. Superseded by IComponent2::Select3 . |
| Method | Select2 | Obsolete. Superseded by IComponent2::Select3 . |
| Method | Select3 | Obsolete. Superseded by IComponent2::Select4 . |
| Method | Select4 | Selects this component. |
| Method | SelectByMark | Obsolete. Superseded by IComponent2::Select3 . |
| Method | SetCosmosWorksMaterial | Assigns the material to use during analysis to this component. |
| Method | SetExcludeFromBOM2 | Sets whether to exclude this component from the bills of materials (BOMs) in the specified configurations. |
| Method | SetMaterialIdName | Sets the material name for this component. |
| Method | SetMaterialPropertyValues2 | Sets the material properties for this component. |
| Method | SetMaterialUserName | Sets the material user name for this component. |
| Method | SetReferencedDisplayStates | Sets the specified display state of this component to be referenced by the specified assembly display state(s). |
| Method | SetSmartComponentData | Sets the features, components, and feature references of a Smart Component. |
| Method | SetSuppression | Obsolete. Superseded by IComponent2::SetSuppression2 . |
| Method | SetSuppression2 | Sets the suppression state of this component. |
| Method | SetTexture | Applies texture to this component in the specified configuration. |
| Method | SetTextureByDisplayState | Sets the texture applied to this component in the specified display state. |
| Method | SetTransformAndSolve | Obsolete. Superseded by IComponent2::SetTransformAndSolve2 . |
| Method | SetTransformAndSolve2 | Obsolete. Superseded by IComponent2::SetTransformAndSolve3 . |
| Method | SetTransformAndSolve3 | Sets the transform and solves for the mates for this component. |
| Method | SetVisibility | Sets the visibility state for this component. |
| Method | SetVisibilityInAsmDisplayStates | Sets the visibility of this component in the specified assembly display state(s). |
| Method | SetXform | Obsolete. Superseded by IComponent2::Transform2 . |
| Method | SetXformAndSolve | Obsolete. Superseded by IComponent2::SetTransformAndSolve2 . |
| Method | UpdateExternalFileReferences | Updates the external file references of this model. |

[Top](#topBookmark)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::GetPathName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.html)
