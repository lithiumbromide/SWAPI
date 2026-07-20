---
title: "IConfiguration Interface Members"
project: "SOLIDWORKS API Help"
interface: "IConfiguration_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html"
---

# IConfiguration Interface Members

The following tables list the members exposed by[IConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AddRebuildSaveMark | Adds or removes the mark indicating whether the configuration needs to be rebuilt and its configuration data saved every time you save the model document. |
| Property | AlternateName | Gets or sets the configuration's alternate name (i.e., user-specified name). |
| Property | BOMPartNoSource | Gets or sets the source of the part number used in the BOM table. |
| Property | ChildComponentDisplayInBOM | Gets or sets the child component display option of this configuration in the Bill of Materials (BOM) for an assembly or for a cutlist part (weldment and/or sheet metal). |
| Property | Comment | Gets or sets the configuration comment. |
| Property | CustomPropertyManager | Gets the custom property information for this configuration. |
| Property | Description | Gets or sets the description of the configuration. |
| Property | DimXpertManager | Gets the DimXpert schema for this configuration. |
| Property | HideNewComponentModels | Gets or sets whether new components are hidden in this inactive configuration. |
| Property | LargeDesignReviewMark | Gets or sets whether to add display data to this configuration when the document is saved. |
| Property | Lock | Gets or sets whether the configuration is locked. |
| Property | Name | Gets or sets the configuration name. |
| Property | NeedsRebuild | Gets whether the configuration needs to be rebuilt. |
| Property | RepresentationShared | Gets or sets whether this SOLIDWORKS Connected Representation configuration is shared. |
| Property | ShowChildComponentsInBOM | Obsolete. Superseded by IConfiguration::ChildComponentDisplayInBOM . |
| Property | SuppressNewComponentModels | Gets or sets whether new components are suppressed in this configuration. |
| Property | SuppressNewFeatures | Gets or sets whether to suppress new features in this configuration. |
| Property | Type | Gets the type of configuration. |
| Property | UseAlternateNameInBOM | Gets or sets whether the alternate name (i.e., user-specified name) is displayed in the bill of materials for this configuration. |
| Property | UseDescriptionInBOM | Gets or sets whether the description of the configuration is displayed in the bill of materials. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddExplodeStep | Obsolete. Superseded by IConfiguration::AddExplodeStep2 . |
| Method | AddExplodeStep2 | Adds a regular (translate and rotate) explode step to the explode view of the active configuration. |
| Method | AddPartExplodeStep | Adds an explode step to the specified explode view of a multibody part. |
| Method | AddRadialExplodeStep | Adds a radial explode step to the explode view of the active configuration. |
| Method | ApplyDisplayState | Applies the specified display state to this configuration. |
| Method | CopyDisplayStateFromConfiguration | Copies the specified display state from the specified configuration to this configuration. |
| Method | CreateDisplayState | Creates a display state for this configuration. |
| Method | DeleteDisplayState | Deletes the specified display state from this configuration. |
| Method | DeleteExplodeStep | Deletes the specified explode step. |
| Method | Get3DExperienceType | Gets how this configuration is viewed in SOLIDWORKS Connected . |
| Method | GetChildren | Gets all of the children configurations of this derived configuration. |
| Method | GetChildrenCount | Gets the number of children for this configuration. |
| Method | GetComponentConfigName | Gets the referenced configuration name of the specified component in this configuration. |
| Method | GetComponentSuppressionState | Gets the suppression state of the specified component in this configuration. |
| Method | GetCurrentPartExplodeViewName | Gets the explode view name in the current configuration. |
| Method | GetCustomProperties | Obsolete. Superseded by IConfiguration::CustomPropertyManager . |
| Method | GetCustomPropertiesCount | Obsolete. Superseded by IConfiguration::CustomPropertyManager . |
| Method | GetCutListItems | Gets the cut list folders in this active or non-active configuration. |
| Method | GetDisplayStateBodyProperties | Gets the bodies and their material properties in the specified display state. |
| Method | GetDisplayStateComponentProperties | Gets the components and their material properties in the specified display state. |
| Method | GetDisplayStateComponentVisibility | Gets the components and their visibilities in the specified display state. |
| Method | GetDisplayStateFaceProperties | Gets the faces and their material properties in the specified display state. |
| Method | GetDisplayStateFeatureProperties | Gets the features and their material properties in the specified display state. |
| Method | GetDisplayStateProperties | Gets the material properties of the specified display state. |
| Method | GetDisplayStates | Gets the names of the display states for this configuration. |
| Method | GetDisplayStatesCount | Gets the number of display states for this configuration. |
| Method | GetExpanded | Gets whether this configuration's node is expanded in the specified pane of the ConfigurationManager. |
| Method | GetExplodeStep | Gets the specified explode step in this configuration's explode step sequence. |
| Method | GetID | Gets the configuration ID of this configuration. |
| Method | GetNumberOfExplodeSteps | Gets the number of explode steps for this configuration. |
| Method | GetNumberOfPartExplodeSteps | Gets the number of explode steps in the explode view of a multibody part. |
| Method | GetParameterCount | Gets the number of parameters for this configuration. |
| Method | GetParameters | Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration. |
| Method | GetParent | Gets the parent configuration of this derived configuration. |
| Method | GetPartExplodeStep | Gets the specified explode step of an explode view of a multibody part. |
| Method | GetRepresentationParent | Gets the Physical Product represented by this configuration. |
| Method | GetRootComponent | Obsolete. Superseded by IConfiguration::GetRootComponent3 . |
| Method | GetRootComponent3 | Gets the root component for this assembly configuration. |
| Method | GetScene | Gets the ISwScene object for this configuration. |
| Method | GetStreamName | Gets the name of the stream for the current configuration. |
| Method | IAddExplodeStep | Adds a new explode step to the configuration. |
| Method | IGetChildren | Gets all of the children configurations of this derived configuration. |
| Method | IGetCustomProperties | Obsolete. Superseded by IConfiguration::CustomPropertyManager . |
| Method | IGetDisplayStates | Gets the names of the display states for this configuration. |
| Method | IGetExplodeStep | Gets a pointer to the specified explode step in the configuration explode step sequence. |
| Method | IGetParameters | Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration. |
| Method | IGetRootComponent | Obsolete. Superseded by IConfiguration::IGetRootComponent2 . |
| Method | IGetRootComponent2 | Obsolete. Superseded by IConfiguration::GetRootComponent3 . |
| Method | IsDefeature | Gets whether this configuration is a defeature configuration. |
| Method | IsDerived | Gets whether this configuration is a derived configuration. |
| Method | IsDirty | Gets whether this configuration is dirty (i.e., needs to be updated). |
| Method | ISetParameters | Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration. |
| Method | IsLoaded | Gets whether a configuration is loaded. |
| Method | IsSpeedPak | Gets whether the configuration is a SpeedPak. |
| Method | RenameDisplayState | Renames a display state of this configuration. |
| Method | Select | Obsolete. Superseded by IConfiguration::Select2 . |
| Method | Select2 | Selects the configuration. |
| Method | Set3DExperienceType | Converts this configuration in SOLIDWORKS Connected . |
| Method | SetColor | Sets the color for this configuration. |
| Method | SetExpanded | Sets whether to expand this configuration's node in the specified pane of the ConfigurationManager. |
| Method | SetParameters | Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration. |
| Method | UpdateSpeedPak | Updates the SpeedPak configuration for this configuration. |

[Top](#topBookmark)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
