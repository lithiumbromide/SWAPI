---
title: "IConfigurationManager Interface Members"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html"
---

# IConfigurationManager Interface Members

The following tables list the members exposed by [IConfigurationManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ActiveConfiguration | Gets the active configuration. |
| Property | Document | Gets the related model document. |
| Property | EnableConfigurationTree | Gets or sets whether to update the ConfigurationManager tree. |
| Property | LinkDisplayStatesToConfigurations | Gets or sets whether to link or unlink display states to or from the active configuration. |
| Property | ShowConfigurationDescriptions | Gets or sets whether to display configuration descriptions in ConfigurationManager. |
| Property | ShowConfigurationNames | Gets or sets whether to display configuration names in ConfigurationManager. |
| Property | ShowPreview | Gets or sets whether to display the preview of a selected configuration. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddCADFamilyConfiguration | Adds the specified configuration to SOLIDWORKS Design connected to the 3DEXPERIENCE platform . |
| Method | AddConfiguration | Obsolete. Superseded by IConfigurationManager::AddConfiguration2 . |
| Method | AddConfiguration2 | Creates a new configuration. |
| Method | AddRebuildSaveMark | Adds marks indicating whether the specified configurations need to be rebuilt and their configuration data saved every time the model document is saved. |
| Method | AddSpeedPak | Obsolete. Superseded by IConfigurationManager::AddSpeedPak2 . |
| Method | AddSpeedPak2 | Creates a SpeedPak configuration that includes all faces and the specified threshold of parts or bodies for the active assembly configuration. |
| Method | GetConfigurationParams | Gets the parameters for this configuration. |
| Method | GetConfigurationParamsCount | Gets the number of parameters for this configuration. |
| Method | IGetConfigurationParams | Gets the parameters for this configuration. |
| Method | ISetConfigurationParams | Sets the parameters for this configuration. |
| Method | RemoveMarkForAllConfigurations | Remove all marks indicating whether configurations need to be rebuilt and their configuration data saved every time the model document is saved. |
| Method | SetConfigurationParams | Sets the parameters for this configuration. |
| Method | SetExpanded | Sets whether to display and expand all of the configuration nodes in the specified pane of the ConfigurationManager. |
| Method | SortConfigurationTree | Specifies the order in which to list configurations in the ConfigurationManager. |

[Top](#topBookmark)

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
