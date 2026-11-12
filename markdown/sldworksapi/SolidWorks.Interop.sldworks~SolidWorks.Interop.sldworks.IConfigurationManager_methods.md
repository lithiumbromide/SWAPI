---
title: "IConfigurationManager Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_methods.html"
---

# IConfigurationManager Interface Methods

For a list of all members of this type, see [IConfigurationManager members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html).

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
