---
title: "IFeature Interface Members"
project: "SOLIDWORKS API Help"
interface: "IFeature_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html"
---

# IFeature Interface Members

The following tables list the members exposed by [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CreatedBy | Gets the name of the user who created the feature. |
| Property | CustomPropertyManager | Gets the custom property information for weldment and cut-list item features only. |
| Property | DateCreated | Gets the date on which the feature was created. |
| Property | DateModified | Gets the date on which the feature was last modified. |
| Property | Description | Gets or sets the description for this feature. |
| Property | ExcludeFromCutList | Gets or sets whether to exclude this feature from the cut list. |
| Property | Is3DInterconnectFeature | Gets whether this is a 3D Interconnect feature. |
| Property | Is3DInterconnectUpdateAvailable | Gets whether an update is available for this 3D Interconnect part or assembly. |
| Property | Name | Gets or sets the name of the current feature. |
| Property | Visible | Gets the visibility state of this feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddComment | Adds a comment to this feature. |
| Method | AddPropertyExtension | Adds a property extension to this feature. |
| Method | BreakLink | Breaks the link to third-party native CAD parts and assemblies. |
| Method | DeSelect | Deselects this feature. |
| Method | EnumDisplayDimensions | This method returns a display dimensions enumeration for this feature. |
| Method | GetAffectedFaceCount | Gets the number of faces modified by a feature, such as a draft feature. |
| Method | GetAffectedFaces | Gets the faces modified by a feature, such as a draft feature. |
| Method | GetBody | Obsolete. Superseded by IFeatures::GetFaces , IFeatures::IGetFaces2 , IFace2::GetBody , and IFace2::IGetBody . |
| Method | GetBox | Gets the bounding box for this feature. |
| Method | GetChildren | Gets the child features belonging to this feature. |
| Method | GetCreatedVersion | Gets the SOLIDWORKS version number in which the selected feature was created. |
| Method | GetDefinition | Gets the feature data object for a feature, such as an advanced mate, extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature. |
| Method | GetDisplayDimension | Gets the display dimension object for the specified pattern property. |
| Method | GetEditStatus | Gets whether the feature can currently be edited. |
| Method | GetErrorCode | Obsolete. Superseded by IFeature::GetErrorCode2 . |
| Method | GetErrorCode2 | Gets the error code for this feature. |
| Method | GetFaceCount | Gets the number of faces in this feature. |
| Method | GetFaces | Gets the faces in this feature. |
| Method | GetFirstDisplayDimension | Provides access to the dimensions that belong to this feature by returning the first display dimension associated with this feature. |
| Method | GetFirstSubFeature | Gets the first sub-feature that belongs to this feature. |
| Method | GetID | Gets the feature ID of this feature. |
| Method | GetImportedFeatureParameters | Gets the data object for this 3D Interconnect part or assembly. |
| Method | GetImportedFileName | Gets the file name from an imported feature. |
| Method | GetMaterialIdName | Gets the material name. |
| Method | GetMaterialPropertyValues | Obsolete. Superseded by IFeature::GetMaterialPropertyValues2 . |
| Method | GetMaterialPropertyValues2 | Gets the material property values for this feature in the specified configurations. |
| Method | GetMaterialUserName | Gets the material name for this feature, which is visible to the user. |
| Method | GetModifiedVersion | Gets the SOLIDWORKS version number in which this feature was last modified. |
| Method | GetNameForSelection | Gets the selected feature's type and name. |
| Method | GetNextDisplayDimension | Gets the next display dimension associated with this feature. |
| Method | GetNextFeature | Gets the next feature in the part. |
| Method | GetNextSubFeature | Gets the next sub-feature from the owner of this sub-feature. |
| Method | GetOwnerFeature | Gets the feature that owns this feature. |
| Method | GetParents | Gets the parent features for this feature. |
| Method | GetPropertyExtension | Gets the property extension on this feature. |
| Method | GetSpecificFeature | Obsolete. Superseded by IFeature::GetSpecificFeature2 . |
| Method | GetSpecificFeature2 | Gets the more specific interface to a selected feature. |
| Method | GetTexture | Gets the texture applied to this feature in the specified configuration. |
| Method | GetTypeName | Gets the type of feature. NOTE: To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call this method; otherwise, call IFeature::GetTypeName2 . |
| Method | GetTypeName2 | Gets the type of feature. NOTE: To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call IFeature::GetTypeName ; otherwise, call this method. |
| Method | GetUIState | Gets the user-interface state of the current feature. |
| Method | GetUpdateStamp | Gets the current update stamp for this feature. |
| Method | HasFrozenUpdatePending | Gets whether this feature has pending freeze updates. |
| Method | HasMaterialPropertyValues | Gets whether this feature has an appearance. |
| Method | IGetAffectedFaces | Gets the faces modified by a feature, such as a draft feature. |
| Method | IGetBody | Obsolete. Superseded by IFeatures::GetFaces , IFeatures::IGetFaces2 , IFace2::GetBody , and IFace2::IGetBody . |
| Method | IGetBody2 | Obsolete. Superseded by IFeatures::GetFaces , IFeatures::IGetFaces2 , IFace2::GetBody , and IFace2::IGetBody . |
| Method | IGetBox | Gets the bounding box for this feature. |
| Method | IGetChildCount | Gets the number of child features that belong to this feature. |
| Method | IGetChildren | Gets the child features belonging to this feature. |
| Method | IGetDefinition | Gets the feature data object for a feature, such as an extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature. |
| Method | IGetFaces | Obsolete. Superseded by IFeature::IGetFaces2 . |
| Method | IGetFaces2 | Gets the faces in this feature. |
| Method | IGetFirstSubFeature | Gets the first sub-feature that belongs to this feature. |
| Method | IGetMaterialPropertyValues | Obsolete. Superseded by IFeature::IGetMaterialPropertyValues2 . |
| Method | IGetMaterialPropertyValues2 | Gets the material property values for this feature in the specified configurations. |
| Method | IGetNextFeature | Gets the next feature. |
| Method | IGetNextSubFeature | Gets the next sub-feature from the owner of this sub-feature. |
| Method | IGetParentCount | Gets the number of parent features for this feature. |
| Method | IGetParents | Gets the parent features for this feature. |
| Method | IGetSpecificFeature | Obsolete. Superseded by IFeature::GetSpecificFeature2 . |
| Method | IIsSuppressed2 | Gets whether the feature in the specified configurations is suppressed. |
| Method | IListExternalFileReferences | Obsolete. Superseded by IFeature::IListExternalFileReferences2 . |
| Method | IListExternalFileReferences2 | Gets the names and statuses of the external references for this feature in a part or assembly. |
| Method | IModifyDefinition | Obsolete. Superseded by IFeature::IModifyDefinition2 . |
| Method | IModifyDefinition2 | Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::IGetDefinition . |
| Method | IParameter | Gets a pointer to the object for the specified parameter or a pointer to the specified parameter. |
| Method | IRemoveMaterialProperty2 | Removes material property values from this feature. |
| Method | IsBase | Obsolete. Superseded by IFeature::IsBase2 . |
| Method | IsBase2 | Gets whether this feature is a base feature. |
| Method | IsDimXpertAnnotation | Gets whether this feature is a DimXpert annotation. |
| Method | IsDimXpertFeature | Gets whether this feature is a DimXpert feature. |
| Method | ISetBody | Obsolete. Superseded by IFeature::ISetBody3 . |
| Method | ISetBody2 | Obsolete. Superseded by IFeature::ISetBody3 . |
| Method | ISetBody3 | Replaces the body of the base feature. |
| Method | ISetMaterialPropertyValues | Obsolete. Superseded by IFeature::ISetMaterialPropertyValues2 . |
| Method | ISetMaterialPropertyValues2 | Sets the material property values for this feature in the specified configurations. |
| Method | ISetSuppression2 | Sets the suppression state of this feature. |
| Method | IsFrozen | Gets whether this feature is frozen. |
| Method | IsHiddenLock | Gets whether this feature is the freeze bar. |
| Method | IsRolledBack | Gets whether this feature is rolled back. |
| Method | IsSuppressed | Obsolete. Superseded by IFeature::IsSuppressed2 . |
| Method | IsSuppressed2 | Gets whether the feature in the specified configurations is suppressed. |
| Method | ListExternalFileReferences | Obsolete. Superseded by IFeature::ListExternalFileReferences2 . |
| Method | ListExternalFileReferences2 | Gets the names and statuses of the external references on the feature in a part or assembly. |
| Method | ListExternalFileReferencesCount | Gets the number of external references on the feature in a part or assembly. |
| Method | MakeSubFeature | Makes a feature become a subfeature of this feature. |
| Method | ModifyDefinition | Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::GetDefinition . |
| Method | MoveFreezeBarTo | Obsolete. Superseded by IFeature::MoveFreezeBarTo2 . |
| Method | MoveFreezeBarTo2 | Moves the freeze bar to the specified location in the FeatureManager design tree. |
| Method | Parameter | Gets a pointer to the object for the specified parameter or a pointer to the specified parameter. |
| Method | RemoveMaterialProperty | Obsolete. Superseded by IFeature::RemoveMaterialProperty2 . |
| Method | RemoveMaterialProperty2 | Removes material property values from this feature. |
| Method | RemoveTexture | Removes texture from this feature in either all of the configurations or only the specified configuration. |
| Method | RemoveTextureByDisplayState | Removes texture from this feature in the specified display state. |
| Method | ResetPropertyExtension | Deletes the property extension for this feature. |
| Method | Select | Obs olete. Superseded by IFeature::Select2 . |
| Method | Select2 | Selects and marks this feature. |
| Method | SelectByMark | Obsolete. Superseded by IFeature::Select2 . |
| Method | SetBodiesToKeep | Set the bodies to keep and their configurations for features that create multiple bodies in parts and assemblies. |
| Method | SetBody | Obsolete. Superseded by IFeature::SetBody2 . |
| Method | SetBody2 | Replaces an imported base feature body. |
| Method | SetImportedFeatureParameters | Sets the data object for this 3D Interconnect part or assembly. |
| Method | SetImportedFileName | Sets the file name of an imported feature. |
| Method | SetMaterialIdName | Sets the material name for this feature. |
| Method | SetMaterialPropertyValues | Obsolete. Superseded by IFeature::SetMaterialPropertyValues2 . |
| Method | SetMaterialPropertyValues2 | Sets the material property values for this feature in the specified configurations. |
| Method | SetMaterialUserName | Sets the material user name for this feature, which is visible to the user. |
| Method | SetSuppression | Obsolete. Superseded by IFeature::SetSuppression2 . |
| Method | SetSuppression2 | Sets the suppression state of this feature. |
| Method | SetTexture | Applies texture to this feature in either all configurations or only the specified configuration. |
| Method | SetTextureByDisplayState | Applies texture to this feature in the specified display state. |
| Method | SetUIState | Sets the user-interface state of the current feature. |
| Method | Update3DInterconnectModel | Updates the model for this 3D Interconnect part or assembly. |
| Method | UpdateExternalFileReferences | Updates the external file references on this model. |

[Top](#topBookmark)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
