---
title: "IModelDocExtension Interface Members"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html"
---

# IModelDocExtension Interface Members

The following tables list the members exposed by[IModelDocExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ActiveCommandTab | Gets and sets the active SOLIDWORKS CommandManager tab. |
| Property | ActiveCommandTabIndex | Gets and sets the index of the active SOLIDWORKS CommandManager tab. |
| Property | AnnotationViewCount | Gets the number of annotation views in this part or assembly document. |
| Property | AnnotationViews | Gets the annotation views in this part or assembly document. |
| Property | AppPageSetup | Gets the SOLIDWORKS application page setup interface for this document. |
| Property | CommandTabVisible | Gets and sets the visibility of the specified SOLIDWORKS CommandManager tab. |
| Property | CustomPropertyBuilderTemplate | Gets or sets the custom property builder template for this part. |
| Property | CustomPropertyManager | Gets the custom properties for this document or configuration. |
| Property | DimXpertManager | Gets the DimXpert schema for this configuration. |
| Property | DisplayMode | Gets and sets the display modes for the specified display state setting. |
| Property | DisplayStateSpecMaterialPropertyValues | Gets and sets the appearance settings for the specified display state setting. |
| Property | DisplayTitle | Gets and sets this model's title to display in the FeatureManager design tree. |
| Property | Document | Gets the model document. |
| Property | FeatureManagerFilterString | Gets or sets the string in the FeatureManager design tree filter. |
| Property | FlyoutFeatureTreeVisibility | Gets or sets the state of the flyout FeatureManager design tree. |
| Property | HasLegacyCustomProperties | Gets whether this model has legacy custom properties. |
| Property | IncludeMassPropertiesOfHiddenBodies | Gets or sets whether to include the mass properties of hidden components in the assembly. |
| Property | LinkedDisplayState | Gets or sets whether a display state is linked in this part. |
| Property | NeedsRebuild | Obsolete. Superseded by IModelDocExtension::NeedsRebuild2 . |
| Property | NeedsRebuild2 | Gets whether the model document needs to be rebuilt. |
| Property | ShowPartRebuildIndicators | Gets or sets whether to display rebuild indicators on parts that have out-of-date frozen features. |
| Property | SunLightInformation | Gets the specified sunlight information. |
| Property | ToolboxPartType | Gets and sets whether this part is a SOLIDWORKS Toolbox part. |
| Property | Transparency | Gets and sets the transparency states for the specified display state setting. |
| Property | UsePageSetup | Gets or sets whether this document uses its own page setup values, SOLIDWORKS application page setup values, or setup values on individual drawing sheets. |
| Property | ViewDisplayRealView | Gets or sets the RealView Graphics setting. |
| Property | Visibility | Gets and sets the visibility states for the specified display state setting. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddAngularRunningDim | Adds the specified angular running dimension for selected entities. |
| Method | AddComment | Adds a comment to this document's Comment Folder. |
| Method | AddDecal | Adds a decal to the model. |
| Method | AddDefaultRenderMaterial | Not supported in SOLIDWORKS 2011 and later and not superseded. |
| Method | AddDimension | Creates a display dimension at the specified location for selected entities. |
| Method | AddDisplayStateSpecificRenderMaterial | Adds the specified appearance to the specified display states in the active configuration and returns the IDs assigned to that appearance. |
| Method | AddOrdinateDimension | Inserts an ordinate dimension. |
| Method | AddOrUpdateSearchData | Adds or updates the SOLIDWORKS Search, third-party, application keyword and value to the model document. |
| Method | AddPathLengthDim | Inserts a path length dimension at the specified coordinates for a selected path. |
| Method | AddRenderMaterial | Not supported in SOLIDWORKS 2011 and later. Superseded by IModelDocExtension::AddDisplayStateSpecificRenderMaterial and IModelDocExtension::IAddDisplayStateSpecificRenderMaterial . |
| Method | AddSpecificDimension | Creates the specified display dimension at the specified location for selected entities. |
| Method | AddSymmetricDimension | Creates a full symmetrical angular dimension at the specified location for the selected entities. |
| Method | AlignDimensions | Aligns the selected dimensions in drawing documents. |
| Method | AlignRunningDimension | Aligns the extension lines of all angular dimensions to be the same distance from the center as the baseline dimension (0 ⁰) in the set of angular running dimensions. |
| Method | ApplyFormatPainterToAll | Applies Format Painter to all dimensions and annotations in the active document. |
| Method | ApplyTexture | Obsolete. Superseded by IModelDocExtension::SetTexture . |
| Method | BreakAllExternalFileReferences2 | Breaks all external references and allows you to insert the features of the original part, or parts, if the external references are broken. |
| Method | Capture3DView | Captures the 3D View of this part or assembly. |
| Method | ChangeSketchPlane | Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations. |
| Method | CloseMessageBar | Closes the specified message bar in this document's window. |
| Method | CloseUserNotification | Closes the specified user notification in this document's window. |
| Method | Compare3DPMI | Compare DimXpert annotations, reference dimensions, and other annotations between different versions of the same part document. |
| Method | CopyDraftingStandard | Copy the current custom drafting standard. |
| Method | Create3DBoundingBox | Creates a 3D bounding box for a cut list item in a weldment part. |
| Method | CreateAdvancedHoleElementData | Creates an Advanced Hole element data object of the specified type. |
| Method | CreateBalloonOptions | Creates an object that stores BOM balloon options. |
| Method | CreateCallout | Creates a callout independent of a selection. |
| Method | CreateDecal | Creates a decal for this model. |
| Method | CreateMassProperty | Obsolete. Superseded by IModelDocExtension::CreateMassProperty2 . |
| Method | CreateMassProperty2 | Creates a mass properties object. |
| Method | CreateMeasure | Creates a measure tool. |
| Method | CreateOLEObject | Creates an OLE object on the active document. |
| Method | CreateRenderMaterial | Creates an appearance for this model. |
| Method | CreateStackedBalloonOptions | Creates an object that stores options for stacked balloons. |
| Method | CreateStructureSystem | Creates a structure system feature using the specified primary and secondary member arrays. |
| Method | CreateStructureSystemMemberData | Creates the specified structure system member. |
| Method | CreateTexture | Creates a texture. |
| Method | DeleteAllDecals | Deletes all decals on this model. |
| Method | DeleteAttachment | Deletes the specified file in the Attachments folder in the FeatureManager design tree. |
| Method | DeleteDecal | Removes the specified decal from this model. |
| Method | DeleteDisplayStateSpecificRenderMaterial | Deletes the specified appearances, using the IDs of the appearances, from the active configuration. |
| Method | DeleteDraftingStandard | Delete the current custom drafting standard. |
| Method | DeleteFeatureMgrViewx64 | Removes the specified tab in the FeatureManager design tree in 64-bit applications. |
| Method | DeleteRenderMaterial | Not supported in SOLIDWORKS 2011 and later. Superseded by IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial and IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial . |
| Method | DeleteScene | Deletes the scene applied to this model. |
| Method | DeleteSearchData | Deletes the specified SOLIDWORKS Search third-party keywords from the model document. |
| Method | DeleteSelection2 | Deletes the selected items, with the option to delete absorbed features, child features, or both. |
| Method | EditBalloonProperties | Obsolete. Superseded by IModelDocExtension::EditBalloonProperties2 . |
| Method | EditBalloonProperties2 | Edits the selected balloon's properties. |
| Method | EditDimensionProperties | Edits the selected dimension. |
| Method | EditRebuildAll | Rebuilds only those features that need to be rebuilt in all configurations without activating each configuration. |
| Method | FindTrackedObjects | Finds the tracking IDs assigned to entities in this document. |
| Method | FinishRecordingUndoObject | Obsolete. Superseded by IModelDocExtension::FinishRecordingUndoObject2 . |
| Method | FinishRecordingUndoObject2 | Ends recording of a SOLIDWORKS Undo object with the specified name and visibility. |
| Method | ForceRebuildAll | Forces a rebuild of all features in all configurations without activating each configuration. |
| Method | GeodesicSketchOffset | Creates a geodesic sketch offset along the curvature of a surface. |
| Method | Get3DExperienceModelType | Gets the type of 3D EXPERIENCE application that owns this model. |
| Method | Get3DView | Gets the 3D View with the specified name for this part or assembly. |
| Method | Get3DViewCount | Gets the number of 3D Views in this part or assembly. |
| Method | Get3DViewNames | Gets names of the 3D Views in this part or assembly. |
| Method | Get3DViews | Gets the 3D Views for this part or assembly. |
| Method | GetActiveAnnotationView | Gets the active annotation view of this model. |
| Method | GetActivePropertyManagerPage | Gets the name of the active PropertyManager page. |
| Method | GetAdvancedSaveAsOptions | Gets the advanced File > Save As options. |
| Method | GetAdvancedSpotLightProperties | Gets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model. |
| Method | GetAnnotationCount | Gets the number of annotations on this part. |
| Method | GetAnnotations | Gets the annotations on this part. |
| Method | GetAnnotationsByType | Gets the annotations of the specified type in this document. |
| Method | GetAppearanceSetting | Gets the appearance setting for this document. |
| Method | GetAttachmentCount | Gets the number of attachments for this document. |
| Method | GetAttachments | Gets the attachments for this document. |
| Method | GetCalloutVariableString | Gets the string for the specified callout variable. |
| Method | GetCameraById | Gets a camera using the specified camera ID. |
| Method | GetCameraCount | Gets the number of cameras in the document. |
| Method | GetCameraDefinition | Gets a camera, but does not add the newly created camera to the model. |
| Method | GetCommandTabs | Gets all of the SOLIDWORKS CommandManager tab names in this document. |
| Method | GetCoordinateSystemTransformByName | Gets the transform of the specified coordinate system. |
| Method | GetCorresponding | Obsolete. Superseded by IModelDocExtension::GetCorresponding2 . |
| Method | GetCorresponding2 | Gets the object in the underlying part or subassembly document that corresponds to the specified input object in this drawing view or assembly. |
| Method | GetCorrespondingEntity | Obsolete. Superseded by IModelDocExtension::GetCorrespondingEntity2 . |
| Method | GetCorrespondingEntity2 | Gets the entity in the underlying part or subassembly that corresponds to the specified entity in this assembly or drawing view. |
| Method | GetCostingManager | Gets the entry-point interface to the SOLIDWORKS Costing API and gets the CostingManager. |
| Method | GetCSYSDistances | Gets the specified distances between two selected coordinate systems. |
| Method | GetCSYSEulersAngularRotation | Gets the specified Eulers angular rotation values that transform one selected coordinate system into another. |
| Method | GetCSYSXYZAngularRotation | Gets the specified Tait-Bryan angular rotation values that transform one selected coordinate system into another. |
| Method | GetDecal | Gets the specified decal in this model. |
| Method | GetDecals | Gets the decals applied to the model. |
| Method | GetDecalsCount | Gets the number of decals applied to this model. |
| Method | GetDependencies | Gets all of this model's dependencies. |
| Method | GetDisplayStateSetting | Gets the display state setting for the specified scope. |
| Method | GetDraftingStandardNames | Get the names of all currently available drafting standards. |
| Method | GetFlattenSheetMetalPersistReference | Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part. |
| Method | GetGeneralTableAnnotation | Creates a general table annotation for SOLIDWORKS MBD 3D PDF. |
| Method | GetKeepLightInRenderScene | Gets whether a light is kept when the scene changes. |
| Method | GetLastFeatureAdded | Gets the last feature added to the model. |
| Method | GetLicenseType | Gets the type of SOLIDWORKS license used when the model was created. |
| Method | GetLightEnabledInRender | Gets whether a light is on in this model. |
| Method | GetMassProperties | Obsolete. Superseded by IModelDocExtension::GetMassProperties2 . |
| Method | GetMassProperties2 | Obsolete. Superseded by IMassProperty2 . |
| Method | GetMaterial | Gets the appearance for the specified appearance ID in the specified configuration in this model document |
| Method | GetMaterialPropertyValues | Gets the material properties for this model document. |
| Method | GetMBD3DPdfData | Gets the SOLIDWORKS MBD 3D PDF data object. |
| Method | GetModelBreakViewNames | Gets the names and number of the Model Break Views in the current configuration of the active model. |
| Method | GetModelViewCount | Gets the number of model views in this document. |
| Method | GetModelViews | Gets the model views in this document. |
| Method | GetMotionStudyManager | Gets the SOLIDWORKS motion study's MotionManager. |
| Method | GetNamedViewRotation | Gets the specified named view orientation matrix with respect to the Front view. |
| Method | GetObjectByPersistReference | Obsolete. Superseded by IModelDocExtension::GetObjectByPersistReference3 . |
| Method | GetObjectByPersistReference2 | Obsolete. Superseded by IModelDocExtension::GetObjectByPersistReference3 . |
| Method | GetObjectByPersistReference3 | Gets the object assigned to the specified persistent reference ID. |
| Method | GetObjectId | Gets the object ID for the specified annotation. |
| Method | GetOLEObjectCount | Gets the number of OLE objects. |
| Method | GetOLEObjects | Get the OLE objects. |
| Method | GetPackAndGo | Gets a Pack and Go object. |
| Method | GetPersistReference | Obsolete. Superseded IModelDocExtension::GetPersistReference3 . |
| Method | GetPersistReference3 | Gets the persistent reference ID for the specified object in this model document. |
| Method | GetPersistReferenceCount | Obsolete. Superseded by IModelDocExtension::GetPersistReferenceCount3 . |
| Method | GetPersistReferenceCount3 | Gets the size of the persistent reference ID assigned to the selected object in this model document. |
| Method | GetPLMID | Gets the ID of this SOLIDWORKS Connected document. |
| Method | GetPrint3DDialog | Gets the IPrint3DDialog object. |
| Method | GetPrintSpecification | Gets the IPrintSpecification object for this document. |
| Method | GetRenderCustomReferences | Get the custom render references for this model. |
| Method | GetRenderMaterials | Obsolete. Superseded by IModelDocExtension::GetRenderMaterials2 . |
| Method | GetRenderMaterials2 | Gets the appearances applied to this model document in the specified display states. |
| Method | GetRenderMaterialsCount | Obsolete. Superseded by IModelDocExtension::GetRenderMaterialsCount2 . |
| Method | GetRenderMaterialsCount2 | Gets the number of appearances applied to this model document in the specified display states. |
| Method | GetRenderStockReferences | Gets the SOLIDWORKS-supplied (stock) render references for this model. |
| Method | GetRoutingComponentManager | Gets the routing component manager. |
| Method | GetScanto3D | Gets the IScanTo3D object for this document. |
| Method | GetSceneBkgDIBx64 | Gets the background image as DIBSECTION in 64-bit applications. |
| Method | GetSearchData | Gets the SOLIDWORKS Search, third-party, application keywords from the model document. |
| Method | GetSearchDataCount | Gets the number of SOLIDWORKS Search keywords for the specified third-party application previously added to this model document. |
| Method | GetSectionProperties | Obsolete. Superseded by IModelDocExtension::GetSectionProperties2 . |
| Method | GetSectionProperties2 | Gets the section properties for the following types of selected items: Planar model face in any document Face on a section plane Crosshatch section face in a section view in a drawing a sketch Sketch |
| Method | GetSheetMetalObjectsByPersistReference | Gets the objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part. |
| Method | GetSphericalBoxDiameter | Gets the diameter of the spherical bounding box of this model. |
| Method | GetStream | Gets the handle for the specified stream. |
| Method | GetSunLightAdvancedPropertyValues | Gets the specified sunlight advanced properties. |
| Method | GetSunLightSourcePropertyValues | Gets the property values for a sunlight source. |
| Method | GetSustainability | Gets the entry-point interface to the SOLIDWORKS Sustainability API. |
| Method | GetTemplateSheetMetal | Gets the sheet metal folder feature from this sheet metal model created in SOLIDWORKS 2013 or later. |
| Method | GetTexture | Gets the texture applied to the specified configuration. |
| Method | GetUserPreferenceDouble | Gets document default user preference values. This method is intended for user preferences of type double. |
| Method | GetUserPreferenceDoubleValueRange | Gets the current document default user preference value, and the minimum and maximum valid document user preference values. |
| Method | GetUserPreferenceInteger | Sets document default user preference values. This method is intended for user preferences of type integer. |
| Method | GetUserPreferenceString | Gets document default user preference values. This method is intended for user preferences of type string. |
| Method | GetUserPreferenceTextFormat | Gets document default user preference values. This method is intended for getting detailing text formats. |
| Method | GetUserPreferenceToggle | Gets document default user preference values. This method is intended for user preferences that can be toggled. |
| Method | GetVisibleBox | Gets the visible bounding box set by IModelDocExtension::SetVisibleBox for a part or an assembly. |
| Method | GetWhatsWrong | Gets the What's Wrong dialog information for this model document. |
| Method | GetWhatsWrongCount | Gets the number of items in the What's Wrong dialog. |
| Method | HasDesignTable | Gets whether a document has a design table. |
| Method | HasLegacyCThreads | Gets whether this model has legacy cosmetic threads. |
| Method | HasMaterialPropertyValues | Gets whether this model has an appearance. |
| Method | HasRenamedDocuments | Gets whether the document has renamed files. |
| Method | HideDecal | Hides or shows the specified decal applied to this model. |
| Method | HideFeatureManager | Hides or shows the Manager Pane. |
| Method | IAddDisplayStateSpecificRenderMaterial | Adds the specified material to the specified display states in the active configuration and returns the IDs assigned to that material. |
| Method | IChangeSketchPlane | Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations. |
| Method | ICreateOLEObject | Creates an OLE object on the active document. |
| Method | IDeleteDisplayStateSpecificRenderMaterial | Deletes the specified materials, using the IDs of the materials, from the active configuration. |
| Method | IEditDimensionProperties | Edits the selected dimension. |
| Method | IGet3rdPartyStorageStore | Gets the IStorage interface to the specified third-party storage in this SOLIDWORKS document. |
| Method | IGetAnnotations | Gets the annotations on this model. |
| Method | IGetAnnotationViews | Gets the annotation views in this part or assembly document. |
| Method | IGetAttachments | Gets the attachments for this document. |
| Method | IGetDecals | Gets the decals applied to the model. |
| Method | IGetFlattenSheetMetalPersistReference | Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part. |
| Method | IGetMassProperties | Obsolete. Superseded by IModelDocExtension::GetMassProperties2 . |
| Method | IGetMaterialPropertyValues | Gets the material properties for this model. |
| Method | IGetModelViews | Gets the model views in this document. |
| Method | IGetNamedViewRotation | Gets the specified named view orientation matrix with respect to the Front view. |
| Method | IGetObjectByPersistReference | Obsolete. Superseded by IModelDocExtension::IGetObjectByPersistReference3 . |
| Method | IGetObjectByPersistReference2 | Obsolete. Superseded by IModelDocExtension::IGetObjectByPersistReference3 . |
| Method | IGetObjectByPersistReference3 | Gets the object assigned to the specified persistent reference ID. |
| Method | IGetOLEObjects | Get the OLE objects. |
| Method | IGetPersistReference | Obsolete. Superseded by IModelDocExtension::IGetPersistReference3 . |
| Method | IGetPersistReference3 | Gets the persistent reference ID for the specified object in this model document. |
| Method | IGetRenderMaterials | Obsolete. Superseded by IModelDocExtension::GetRenderMaterials2 . |
| Method | IGetSearchData | Gets the SOLIDWORKS Search, third-party, application keywords from the model document. |
| Method | IGetSectionProperties | Obsolete. Superseded by IModelDocExtension::IGetSectionProperties2 . |
| Method | IGetSectionProperties2 | Gets the section properties for the following types of selected items: Planar model face in any document Face on a section plane Crosshatch section face in a section view in a drawing a sketch Sketch |
| Method | IGetSheetMetalObjectsByPersistReference | Gets the object, or objects, in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part. |
| Method | IListExternalFileReferences | Gets the names and statuses of the external file references on this part or assembly. |
| Method | IMultiSelect | Obsolete. Superseded by IModelDocExtension::MultiSelect2 . |
| Method | InsertAnnotationFavorite | Inserts annotations from the specified favorite file at the specified location. |
| Method | InsertAnnotationView | Inserts an annotation view in this part or assembly document. |
| Method | InsertAttachment | Inserts a file as an Attachment to this document. |
| Method | InsertBOMBalloon | Obsolete. Superseded by IModelDocExtension::InsertBomBalloon2 . |
| Method | InsertBOMBalloon2 | Inserts a BOM balloon for the selected item. |
| Method | InsertBomTable | Obsolete. Superseded by IModelDocExtension::InsertBomTable2 . |
| Method | InsertBomTable2 | Obsolete. Superseded by IModelDocExtension::InsertBomTable3 . |
| Method | InsertBomTable3 | Obsolete. Superseded by IModelDocExtension::InsertBomTable4 . |
| Method | InsertBomTable4 | Inserts a bill of materials (BOM) table in a part or assembly document. |
| Method | InsertCamera | Inserts a camera in this document. |
| Method | InsertChainDimensions | Chains dimensions for the specified entities in this drawing or sketch. |
| Method | InsertDatumTargetSymbol2 | Obsolete. Superseded by IModelDocExtension::InsertDatumTargetSymbol3 . |
| Method | InsertDatumTargetSymbol3 | Creates a datum target symbol. |
| Method | InsertDeleteFace | Inserts a DeleteFace feature. |
| Method | InsertGeneralTableAnnotation | Inserts the a general table annotation in this model document. |
| Method | InsertGeneralToleranceTableAnnotation | Inserts a general tolerance table annotation in this model document. |
| Method | InsertObjectFromFile | Inserts an OLE object from a file. |
| Method | InsertScene | Applies the specified scene to the model. |
| Method | InsertStackedBalloon | Obsolete. Superseded by IModelDocExtension::InsertStackedBalloon2 . |
| Method | InsertStackedBalloon2 | Inserts a stack of balloons for selected items. |
| Method | InsertSurfaceFinishSymbol3 | Creates a surface-finish symbol based on the last selection. |
| Method | InsertTitleBlockTable | Inserts a title block table in a part or assembly document. |
| Method | InstallModelColorizer | Installs your implemented interface of the ISwColorContour interface. |
| Method | IPrintOut2 | Obsolete. Superseded by IModelDocExtension::IPrintOut3 . |
| Method | IPrintOut3 | Obsolete. Superseded by IModelDocExtension::PrintOut4 . |
| Method | IRelease3rdPartyStorageStore | Releases the specified third-party storage in this document. |
| Method | IRemoveMaterialProperty | Removes material property values from this model. |
| Method | IsAbbreviatedViewActive | Gets or sets whether the abbreviated view is active. |
| Method | IsConverted | Gets whether the active document was converted to the current release uponing opening but has not yet been saved. |
| Method | IsDisplayPaneVisible | Gets whether the Display Pane is visible in this active document. |
| Method | ISetMaterialPropertyValues | Sets the material property values for this model document. |
| Method | IsExploded | Gets the name of the exploded view currently shown in the model. |
| Method | IsFutureVersion | Gets whether this document is for a future version of SOLIDWORKS. |
| Method | IsSamePersistentID | Gets whether the two specified objects have the same persistent reference IDs. |
| Method | IsVirtualComponent | Obsolete. Superseded by IModelDocExtension::IsVirtualComponent2 . |
| Method | IsVirtualComponent2 | Obsolete. Superseded by IModelDocExtension::IsVirtualComponent3 . |
| Method | IsVirtualComponent3 | Gets the paths to parent assembly components, up to and including the first non-virtual parent, if the model is a virtual component. |
| Method | JogDimension | Gets or sets whether jog points are on or off on an interactively selected linear or ordinate dimension. |
| Method | ListExternalFileReferences | Obsolete. Superseded by IModelDocExtension::ListExternalFileReferences2 . |
| Method | ListExternalFileReferences2 | Gets the specified external file reference information for this part or assembly. |
| Method | ListExternalFileReferencesCount | Gets the number of external references on this part or assembly. |
| Method | LoadDraftingStandard | Loads a custom drafting standard from a file. |
| Method | Make3DExperienceCompatible | Makes the current model compatible with SOLIDWORKS Connected . |
| Method | MoveDecal | Moves the decal up or down in the list of decals applied to the model. |
| Method | MoveOrCopy | Moves and optionally copies the selected sketch entities or annotations. |
| Method | MultiSelect | Obsolete. Superseded by IModelDocExtension::MultiSelect2 . |
| Method | MultiSelect2 | Selects multiple objects and returns the number of objects selected in the model. |
| Method | PrintOut | Obsolete. Superseded by IModelDocExtension::PrintOut2 . |
| Method | PrintOut2 | Obsolete. Superseded by IModelDocExtension::PrintOut3 . |
| Method | PrintOut3 | Obsolete. Superseded by IModelDocExtension::PrintOut4 . |
| Method | PrintOut4 | Prints this document without displaying any dialogs or message boxes. |
| Method | PublishSTEP242File | Exports the SOLIDWORKS MBD 3D part or assembly to a STEP 242 file. |
| Method | PublishTo3DPDF | Creates a 3D PDF for SOLIDWORKS MBD. |
| Method | PurgeDisplayState | Purges identical display states so that only unique display states remain. |
| Method | RayIntersections | Finds the intersections between the specified set of rays and the specified set of bodies. |
| Method | Rebuild | Rebuilds the model in assembly and drawing documents and returns the status of the rebuild. |
| Method | Refresh3DViews | Updates the 3D Views of this part or assembly. |
| Method | ReJogRunningDimension | Applies jogs where extension lines overlap dimension text in an angular running dimension. |
| Method | ReleaseStream | Releases a previously obtained stream. |
| Method | ReloadOrReplace | Reloads or replaces this model document. |
| Method | ReloadWithReferences | Reloads this model document with the specified references. |
| Method | RemoveMaterialProperty | Removes material properties from this model. |
| Method | RemoveModelColorizer | Removes your installed implemented interface of the ISwColorContour interface. |
| Method | RemoveTexture | Obsolete. Superseded by IModelDocExtension::RemoveTexture2 . |
| Method | RemoveTexture2 | Removes the texture from the specified configuration. |
| Method | RemoveTextureByDisplayState | Removes the texture applied to this model in the specified display state. |
| Method | RemoveVisibleBox | Removes the visible bounding box set by IModelDocExtension::SetVisibleBox and resets the size of the bounding box to the size calculated by SOLIDWORKS for a part or an assembly. |
| Method | RenameDocument | Temporarily renames the selected component using the specified name. |
| Method | RenameDraftingStandard | Rename the current custom drafting to the specifed name. |
| Method | ReorderFeature | Obsolete. Superseded by IModelDocExtension::ReorderFeature2 . |
| Method | ReorderFeature2 | Moves the specified feature to another location in the FeatureManager design tree of this part or assembly. |
| Method | ResetStandardViews | Returns all standard model views to their default settings. |
| Method | ReverseDecalsOrder | Reverses the order of the decals on the model. |
| Method | RotateOrCopy | Rotates and optionally copies the selected sketch entities or annotations. |
| Method | RunCommand | Runs the specified SOLIDWORKS command. |
| Method | SaveAs | Obsolete. Superseded by IModelDocExtension::SaveAs2 . |
| Method | SaveAs2 | Obsolete. Superseded by IModelDocExtension::SaveAs3 . |
| Method | SaveAs3 | Saves the active document to the specified name with advanced options. |
| Method | SaveDeFeaturedFile | Removes all CAD data except the outer surface from a loaded part or assembly document and saves the outer surface as a part. |
| Method | SaveDraftingStandard | Saves the current custom drafting standard to a file. |
| Method | SavePackAndGo | Saves the files designated for Pack and Go to either a folder or Zip file. |
| Method | SaveSelection | Creates a new selection set containing the selected entities. |
| Method | SaveTo3DExperience | Saves this document in SOLIDWORKS Connected using the specified save options. |
| Method | SaveViewToSolidworks | Saves the specified named view of this model to SOLIDWORKS. |
| Method | ScaleOrCopy | Scales and optionally copies the selected sketch items or annotations. |
| Method | SelectAll | Selects all edges in a part, all components in an assembly, or all entities (by default, sketch entities, dimensions, and annotations) in a drawing. |
| Method | SelectByID | Obsolete. Superseded by IModelDocExtension::SelectByID2 . |
| Method | SelectByID2 | Selects the specified entity. |
| Method | SelectByRay | Selects the first entity of the specified type that is intersected by a ray that starts at the specified point and runs parallel to the specified direction vector within the specified radius. |
| Method | SetAdvancedSpotLightProperties | Sets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model. |
| Method | SetApiUndoObject | Implements an undo object for an add-in application. |
| Method | SetKeepLightInRenderScene | Sets whether to keep a light when the scene changes. |
| Method | SetLightEnabledInRender | Sets whether a light is on in this model. |
| Method | SetMaterialPropertyValues | Sets the material property values for this model document. |
| Method | SetSceneBkgDIBx64 | Sets the background image in 64-bit applications. |
| Method | SetSunLightAdvancedPropertyValues | Sets the specified sunlight advanced properties. |
| Method | SetSunLightSourcePropertyValues | Sets the property values for a sunlight source. |
| Method | SetTexture | Applies texture to the specified configuration. |
| Method | SetTextureByDisplayState | Sets the texture applied to this model in the specified display state. |
| Method | SetTopLevelTransparency | Sets the transparency of this part or top-level assembly. |
| Method | SetUserPreferenceDouble | Sets document default user preference values. This method is intended for user preferences of type double. |
| Method | SetUserPreferenceInteger | Sets document default user preference values. This method is intended for user preferences of type integer. |
| Method | SetUserPreferenceString | Sets document default user preference values. This method is intended for user preferences of type string. |
| Method | SetUserPreferenceTextFormat | Sets document default user preference values. This method is intended for setting detailing text formats. |
| Method | SetUserPreferenceToggle | Sets document default user preference values. This method is intended for user preferences that can be toggled. |
| Method | SetVisibleBox | Sets the visible bounding box for Zoom to Fit for a part or an assembly. |
| Method | ShowMessageBar | Shows the specified message bar in this document's window. |
| Method | ShowModelBreakView | Gets whether to show or hide the specified Model Break View in the current configuration of the active model. |
| Method | ShowSmartMessage | Displays a SOLIDWORKS-style message as a ToolTip in the graphics area and on the status bar. |
| Method | ShowUserNotification | Displays the specified user notfication for this document. |
| Method | SketchBoxSelect | Box selects all of the entities in a sketch within the specified coordinates of the selection box. |
| Method | SketchOffsetOnSurface | Creates a Euclidean sketch offset from selected edges of a face or surface. |
| Method | StartFormatPainter | Starts the Format Painter. |
| Method | StartRecordingUndoObject | Starts recording the SOLIDWORKS Undo object. |
| Method | StopFormatPainter | Stops the Format Painter. |
| Method | Stretch | Stretch the selected entities. |
| Method | UpdateExternalFileReferences | Updates the external files references on this model. |
| Method | UpdateFrozenFeatures | Updates frozen features of the model. |
| Method | UpdateRenderMaterialsInSceneGraph | Sets whether to update the appearances in the graphics area in the model. |
| Method | UpdateStandardViews | Changes the specified standard view to the current model view. |
| Method | UpdateSunLight | Updates sunlight position, color, and background image. |
| Method | UpgradeLegacyCThreads | Upgrades cosmetic thread features in this legacy model to the latest cosmetic thread architecture. |
| Method | UpgradeLegacyCustomProperties | Upgrades custom properties in this legacy (created prior to SOLIDWORKS 2018) model to the latest custom properties architecture. |
| Method | ViewZoomToSheet | Zooms a drawing sheet to its maximum size within the window. |

[Top](#topBookmark)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
