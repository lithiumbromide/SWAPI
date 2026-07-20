---
title: "IAssemblyDoc Interface Members"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html"
---

# IAssemblyDoc Interface Members

The following tables list the members exposed by[IAssemblyDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ClearanceVerificationManager | Gets the clearance verification manager. |
| Property | EnableAssemblyRebuild | Gets or sets whether to suspend the rebuild of the assembly. |
| Property | EnablePresentation | Gets or sets whether the assembly is in presentation mode. |
| Property | InterferenceDetectionManager | Gets the Interference Detection manager, which allows you to run interference detection on an assembly to determine whether components interfere with each other. |
| Property | IsSupportedMatesAvailable | Gets whether this assembly contains mates that are supportive of a mate controller. |
| Property | LargeDesignReviewTransparencyLevel | Gets or sets the transparency level of unmodified components in the graphics area of this assembly opened in Large Design Review mode. |
| Property | LargeDesignReviewTransparencyLevelDynamic | Gets or sets whether to dynamically modify the transparency level of unmodified components in the graphics area when the transparency level slider is moved on the Filter Modified Components PropertyManager page. |
| Property | LargeDesignReviewTransparencyLevelEnabled | Gets or sets whether transparency levels are activated for unmodified components in the graphics area for this assembly opened in Large Design Review mode. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ActivateGroundPlane | Activates the ground plane for the specified configurations. |
| Method | AddComponent | Obsolete. Superseded by IAssemblyDoc::AddComponent4 . |
| Method | AddComponent2 | Obsolete. Superseded by IAssemblyDoc::AddComponent4 . |
| Method | AddComponent4 | Obsolete. Superseded by IAssemblyDoc::AddComponent5 . |
| Method | AddComponent5 | Adds the specified component for the specified configuration options to this assembly. |
| Method | AddComponentConfiguration | Adds a new configuration for the last selected assembly component. |
| Method | AddComponents | Obsolete. Superseded by IAssemblyDoc::AddComponents3 . |
| Method | AddComponents3 | Adds multiple components to the assembly. |
| Method | AddConcentricMateWithTolerance | Adds a misaligned concentric mate to this assembly. |
| Method | AddDistanceMate | Adds a distance mate to this assembly. |
| Method | AddMate | Obsolete. Superseded by IAssemblyDoc::AddMate3 . |
| Method | AddMate2 | Obsolete. Superseded by IAssemblyDoc::AddMate3 . |
| Method | AddMate3 | Obsolete. Superseded by IAssemblyDoc::AddMate4 . |
| Method | AddMate4 | Obsolete. Superseded by IAssemblyDoc::AddMate5 . |
| Method | AddMate5 | Obsolete. Superseded by IAssemblyDoc::CreateMate. |
| Method | AddPipePenetration | Penetrates the adjacent fitting or pipe with the pipe that ends at the selected sketch point. |
| Method | AddPipingFitting | Adds a pipe fitting to the current piping assembly. |
| Method | AddPLMComponent | Adds the specified component from a 3DEXPERIENCE collaborative space to the specified location in this assembly in SOLIDWORKS Connected . |
| Method | AddSmartComponent | Adds the specified component at the specified coordinates as a Smart Component to this assembly. |
| Method | AddToFeatureScope | Adds a component to the scope of the currently selected assembly feature. |
| Method | AssemblyPartToggle | Obsolete. Superseded by IAssemblyDoc::EditAssembly and IAssemblyDoc::EditPart2 . |
| Method | AutoAngleAxis | Automatically detect the axis for an angle mate. |
| Method | AutoExplode | Automatically generates an exploded view of the current assembly configuration. |
| Method | AutoMateRepair | Automatically repairs broken mates in this assembly. |
| Method | CollectAllSupportiveMates | Gets all mates supportive of a mate controller in this assembly. |
| Method | CompConfigProperties | Obsolete. Superseded by IAssemblyDoc::CompConfigProperties4 . |
| Method | CompConfigProperties2 | Obsolete. Superseded by IAssemblyDoc::CompConfigProperties4 . |
| Method | CompConfigProperties3 | Obsolete. Superseded by IAssemblyDoc::CompConfigProperties4 . |
| Method | CompConfigProperties4 | Obsolete. Superseded by IAssemblyDoc::CompConfigProperties5 . |
| Method | CompConfigProperties5 | Obsolete. Superseded by IAssemblyDoc::CompConfigProperties6 . |
| Method | CompConfigProperties6 | Sets the properties for the selected component in the specified configuration . |
| Method | ComponentReload | Obsolete. Superseded by IAssemblyDoc::ComponentReload2 . |
| Method | ComponentReload2 | Reloads and/or sets the read-only state of the specified component. |
| Method | CopyWithMates | Obsolete. Superseded by IAssemblyDoc::CopyWithMates2 . |
| Method | CopyWithMates2 | Copies one or more components with mates in this assembly. |
| Method | CreateExplodedView | Creates an explode view of the active assembly configuration. |
| Method | CreateMate | Creates a mate with the specified feature data object. |
| Method | CreateMateData | Creates a mate feature data object for the specified mate type. |
| Method | CreateSmartComponent | Creates a Smart Component. |
| Method | CreateSpeedPak | Creates the specified type of SpeedPak for the active configurations of the selected subassemblies in this assembly. |
| Method | DeleteSelections | Delete either the selected components of a subassembly or the subassembly of the selected component. |
| Method | DissolveComponentPattern | Dissolves the selected component patterns. |
| Method | DissolveSubAssembly | Dissolves the selected subassembly in this assembly. |
| Method | EditAssembly | Switches back to the assembly document for editing. |
| Method | EditConcentricMate | Edits a misaligned concentric mate. |
| Method | EditDistanceMate | Edits a distance mate. |
| Method | EditMate | Obsolete. Superseded by IAssemblyDoc::EditMate2 . |
| Method | EditMate2 | Obsolete. Superseded by IAssemblyDoc::EditMate3 . |
| Method | EditMate3 | Obsolete. Superseded by IAssemblyDoc::EditMate4 . |
| Method | EditMate4 | Obsolete. See the Remarks in each standard, advanced, and mechanical mate's feature data interface. |
| Method | EditPart | Obsolete. Superseded by IAssemblyDoc::EditPart2 . |
| Method | EditPart2 | Edits the selected part within the context of an assembly. |
| Method | EditRebuild | Obsolete. Superseded by IModelDoc2::EditRebuild3 . |
| Method | ExitIsolate | Exits isolating the selected components and returns the assembly to its original display state. |
| Method | FeatureByName | Returns the IFeature object for the named feature in the assembly. |
| Method | FeatureExtrusion | Obsolete. Superseded by IFeatureManager::FeatureExtrusion . |
| Method | FileDeriveComponentPart | Creates a new part document from the currently selected assembly component. |
| Method | FixComponent | Fixes the selected component; i.e., makes it immovable. |
| Method | ForceRebuild | Obsolete. Superseded by IModelDoc2::ForceRebuild3 . |
| Method | ForceRebuild2 | Obsolete. Superseded by IModelDoc2::ForceRebuild3 . |
| Method | ForceUpdateElectricalData | Obsolete. Superseded by IAssemblyDoc::ForceUpdateElectricalData2 . |
| Method | ForceUpdateElectricalData2 | Forces an update of electrical data. |
| Method | GetActiveGroundPlane | Gets the active ground plane for the specified configurations. |
| Method | GetAdvancedSelection | Gets the advanced component selection criteria object for this assembly. |
| Method | GetBox | Gets the bounding box. |
| Method | GetComponentByID | Gets a top-level assembly component using its component ID. |
| Method | GetComponentByName | Gets the specified top-level assembly component. |
| Method | GetComponentCount | Gets the number of components in the active configuration of this assembly. |
| Method | GetComponents | Gets all of the components in the active configuration of this assembly. |
| Method | GetDragOperator | Gets the drag operator for dynamic drag operations in this assembly. |
| Method | GetDroppedAtEntity | Gets a pointer to the entity where a file is dropped into this assembly. |
| Method | GetEditTarget | Gets the model document that is currently being edited. |
| Method | GetEditTargetComponent | Gets the component that is currently being edited. |
| Method | GetExplodedViewConfigurationName | Gets the name of the configuration for the specified exploded view. |
| Method | GetExplodedViewCount | Obsolete. Superseded by IAssemblyDoc::GetExplodedViewCount2 . |
| Method | GetExplodedViewCount2 | Gets the number of exploded views in the specified configuration. |
| Method | GetExplodedViewNames | Obsolete. Superseded by IAssemblyDoc::GetExplodedViewNames2 . |
| Method | GetExplodedViewNames2 | Gets the names of the exploded views in the specified configuration. |
| Method | GetFeatureScope | Gets the components affected by this feature. |
| Method | GetFeatureScopeCount | Gets the number of components affected by this feature. |
| Method | GetFirstMember | Obsolete. Superseded by IComponent2::GetChildren . |
| Method | GetLargeDesignReviewState | Gets the Large Design Review state of this assembly. |
| Method | GetLightWeightComponentCount | Gets the number of lightweight components in the assembly. |
| Method | GetPhysicalSimulationComponents | Obsolete. Not superseded. |
| Method | GetRouteManager | Gets the SOLIDWORKS Routing API. |
| Method | GetSelectedMember | Obsolete. Superseded by ISelectionMgr::GetSelectedObject6 . |
| Method | GetSimulation | Obsolete. Not superseded. |
| Method | GetUnloadedComponentNames | Gets the unloaded components' paths, referenced configuration names, reasons why they are unloaded, document types, and names. |
| Method | GetVisibleComponentsInView | Gets a list of visible components in this assembly to save as solid bodies. |
| Method | GetVisibleComponentsInViewCount | Gets the number of visible components in this assembly. |
| Method | HasUnloadedComponents | Gets whether this assembly has hidden or suppressed unloaded components. |
| Method | HideComponent | Obsolete. Superseded by IModelDoc2::HideComponent2 . |
| Method | IAddComponent2 | Obsolete. Superseded by IAssemblyDoc::AddComponent4 . |
| Method | IAddComponent3 | Obsolete. Superseded by IAssemblyDoc::AddComponent4 . |
| Method | IAddComponents | Obsolete. Superseded by IAssemblyDoc::IAddComponents2 . |
| Method | IAddComponents2 | Obsolete. Superseded by IAssemblyDoc::IAddComponents3 . |
| Method | IAddComponents3 | Adds multiple components to the assembly. |
| Method | IComponentReload2 | Obsolete. Superseded by IAssemblyDoc::ReplaceComponents . |
| Method | IComponentReload3 | Obsolete. Superseded by IAssemblyDoc::ReplaceComponents . |
| Method | IFeatureByName | Returns the IFeature object for the named feature in the assembly. |
| Method | IGetBox | Gets the bounding box. |
| Method | IGetComponents | Gets all of the components in the active configuration of this assembly. |
| Method | IGetDragOperator | Gets the drag operator for dynamic drag operations in this assembly. |
| Method | IGetEditTarget | Obsolete. Superseded by IAssemblyDoc::IGetEditTarget2 . |
| Method | IGetEditTarget2 | Gets the model document that is currently being edited. |
| Method | IGetExplodedViewNames | Obsolete. Superseded by IAssemblyDoc::GetExplodedViewNames2 . |
| Method | IGetFeatureScope | Gets the components affected by this feature. |
| Method | IGetFirstMember | Obsolete. Superseded by IComponent2::GetChildren . |
| Method | IGetSelectedMember | Obsolete. Superseded by SelectionMgr::GetSelectedObject6 . |
| Method | IGetVisibleComponentsInView | Gets a list of visible components in this assembly to save as solid bodies. |
| Method | IMirrorComponents | Obsolete. Superseded by IAssemblyDoc::MirrorComponents2 . |
| Method | InsertCavity | Obsolete. Superseded by IAssemblyDoc::InsertCavity4 . |
| Method | InsertCavity2 | Obsolete. Superseded by IAssemblyDoc::InsertCavity4 . |
| Method | InsertCavity3 | Obsolete. Superseded by IAssemblyDoc::InsertCavity4 . |
| Method | InsertCavity4 | Inserts a cavity to the active part using a selected component. |
| Method | InsertDerivedPattern | Obsolete. See IFeatureManager::CreateFeature and the Remarks in IDerivedPatternFeatureData . |
| Method | InsertEnvelope | Adds an envelope in the specified configuration name in this assembly. |
| Method | InsertImportedComponent | Inserts a third-party native CAD part or assembly into the current configuration of this assembly. |
| Method | InsertJoin | Obsolete. Superseded by IAssemblyDoc::InsertJoin2 . |
| Method | InsertJoin2 | Constructs a feature from merged selected components. |
| Method | InsertLoadReference | Creates a mate load reference to the specified or selected mate. |
| Method | InsertNewAssembly | Creates a new virtual sub-assembly and optionally saves it to the specified file. |
| Method | InsertNewPart | Obsolete. Superseded by IAssemblyDoc::InsertNewPart2 . |
| Method | InsertNewPart2 | Inserts a new part on the specified face or plane. |
| Method | InsertNewVirtualAssembly | Creates a new assembly from this assembly and saves it internally as a virtual component. |
| Method | InsertNewVirtualPart | Creates a new part in the context of an assembly and saves the part internally in the assembly file as a virtual component. |
| Method | InsertWeld | Obsolete. Do not use. Superseded by IFeatureManager::InsertCosmeticWeldBead . |
| Method | InsertWeld2 | Obsolete. Do not use. Superseded by IFeatureManager::InsertCosmeticWeldBead . |
| Method | IReorderComponents | Moves components to a different location in the FeatureManager tree. |
| Method | IReorganizeComponents | Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly. |
| Method | IsComponentTreeValid | Checks the validity of the component tree for this assembly. |
| Method | ISetComponentState | Sets the suppression state for the specified components. |
| Method | ISetComponentVisibility | Hides or shows the selected component in the specified configurations in this assembly document. |
| Method | Isolate | Isolates the selected components. |
| Method | IsRouteAssembly | Gets whether the assembly document is a routing assembly. |
| Method | IToolsCheckInterference2 | Obsolete. See IAssemblyDoc::IToolsCheckInterference3 . |
| Method | IToolsCheckInterference3 | Obsolete. |
| Method | LightweightAllResolved | Sets to lightweight all resolved child components of the selected components. |
| Method | MakeAssemblyFromSelectedComponents | Creates a new assembly comprised of the selected components of this assembly. |
| Method | MakeIndependent | Makes the selected component independent. |
| Method | MakeLightWeight | Sets the selected components to lightweight. |
| Method | MirrorComponents | Obsolete. Superseded by IAssemblyDoc::MirrorComponents2 . |
| Method | MirrorComponents2 | Obsolete. Superseded by IAssemblyDoc::MirrorComponents3 . |
| Method | MirrorComponents3 | Obsolete. Superseded by IFeatureManager::CreateDefinition , IFeatureManager::CreateFeature , and IMirrorComponentFeatureData . |
| Method | OpenCompFile | Obsolete. Superseded by ISldWorks::ActivateDoc2 and ISldWorks::OpenDoc6 . |
| Method | RemoveFromFeatureScope | Removes a component from the scope of the currently selected assembly feature. |
| Method | ReorderComponents | Moves components to a different location in the FeatureManager design tree. |
| Method | ReorganizeComponents | Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly. |
| Method | ReplaceComponents | Obsolete. Superseded by IAssemblyDoc::ReplaceComponents2 . |
| Method | ReplaceComponents2 | Replaces one or more selected components with another model. |
| Method | ReplacePLMComponents | Replaces a selected SOLIDWORKS Connected component in this assembly with the specified component from a 3DEXPERIENCE collaborative space. |
| Method | ResolveAllLightweight | Resolves all lightweight child components of the selected components |
| Method | ResolveAllLightWeightComponents | Resolves the lightweight components in this assembly. |
| Method | ResolveOutOfDateLightWeightComponents | Resolves the selected out-of-date lightweight component, and any out-of-date lightweight sub-components, in the assembly. |
| Method | RotateComponent | Displays the Rotate Component PropertyManager page. |
| Method | RotateComponentAxis | Rotates the component axis by a fixed amount. |
| Method | SaveIsolate | Saves the display characteristics of the isolated components to a new display state. |
| Method | SelectComponentsBySize | Selects assembly components by percent of assembly size. |
| Method | SelectiveOpen | Selectively opens the components of an assembly that is opened in Large Design Review mode. |
| Method | SetComponentState | Sets the suppression state for the specified components. |
| Method | SetComponentSuppression | Suppresses, resolves, or sets to lightweight selected components of this assembly in the active configuration only. |
| Method | SetComponentTransparent | Enables or disables transparency on the selected components. |
| Method | SetComponentVisibility | Hides or shows the selected component in the specified configurations in this assembly document. |
| Method | SetDroppedFileConfigName | Sets the configuration name for the recently dropped file. |
| Method | SetDroppedFileFeatureName | Sets the name of the feature for the recently dropped file. |
| Method | SetDroppedFileName | Sets the new file name for a recently dropped file. |
| Method | SetIsolateVisibility | Sets the display characteristics of all of the components not selected to isolate . |
| Method | SetSpeedPakConfigurations | Sets the configurations in the selected subassemblies to which to apply SpeedPak in this assembly. |
| Method | SetSpeedPakToParent | Switches the selected subassemblies from the SpeedPak configuration to the parent configuration of the SpeedPak configuration. |
| Method | ShowExploded | Obsolete. Superseded by IAssemblyDoc::ShowExploded2 . |
| Method | ShowExploded2 | Displays the specified exploded view for the current assembly configuration. |
| Method | TemporaryFixGroup | Temporarily fix or group selected components during such operations as drag, move, rotate, etc. |
| Method | TemporaryFixGroupExit | Changes components that were temporarily fixed or grouped back to floating or ungrouped after such operations as drag, move, rotate, etc. |
| Method | ToolsCheckInterference | Obsolete. Superseded by IAssemblyDoc::ToolsCheckInterference2 . |
| Method | ToolsCheckInterference2 | Checks for interference between parts in this assembly. |
| Method | TranslateComponent | Displays the Move Component PropertyManager page. |
| Method | UnfixComponent | Floats the selected component; i.e., makes it movable. |
| Method | UngroupComponents | Ungroups the grouped components in the selected folder in the FeatureManager design tree. |
| Method | UpdateBox | Updates the bounding box for this assembly. |
| Method | UpdateFeatureScope | Updates the feature scope and rebuilds the currently selected assembly feature. |
| Method | UpdateSpeedPak | Updates out-of-date SpeedPak configurations for the selected subassemblies. |
| Method | UpdateToolboxComponent | Updates SOLIDWORKS Toolbox components in the specified assembly level using the current information in Toolbox settings. |
| Method | UseSpeedPak | Sets whether to switch the selected subassemblies whose active configuration is the parent configuration of a SpeedPak configuration to the SpeedPak configuration. |
| Method | ViewCollapseAssembly | Collapses the selected exploded view on the Configuration tab of the FeatureManager design tree. |
| Method | ViewExplodeAssembly | Explodes the selected exploded view on the Configuration tab of the FeatureManager design tree. |
| Method | ViewFeatureManagerByDependencies | Obsolete. Superseded by IFeatureManager::ViewDependencies . |
| Method | ViewFeatureManagerByFeatures | Obsolete. Superseded by IFeatureManager::ViewFeatures . |
| Method | ViewFeatureManagerFeatureDetail | Obsolete. Superseded by IFeatureManager::ShowFeatureDetails . |

[Top](#topBookmark)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
