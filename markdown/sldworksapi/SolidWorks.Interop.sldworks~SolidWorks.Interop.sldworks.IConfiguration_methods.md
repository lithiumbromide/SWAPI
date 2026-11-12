---
title: "IConfiguration Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IConfiguration_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_methods.html"
---

# IConfiguration Interface Methods

For a list of all members of this type, see [IConfiguration members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html).

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
| Method | Get3DExperienceType | Gets how this configuration is viewed in SOLIDWORKS Design connected to the 3DEXPERIENCE platform . |
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
| Method | Set3DExperienceType | Converts this configuration in SOLIDWORKS Design connected to the 3DEXPERIENCE platform . |
| Method | SetColor | Sets the color for this configuration. |
| Method | SetExpanded | Sets whether to expand this configuration's node in the specified pane of the ConfigurationManager. |
| Method | SetParameters | Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration. |
| Method | UpdateSpeedPak | Updates the SpeedPak configuration for this configuration. |

[Top](#topBookmark)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
