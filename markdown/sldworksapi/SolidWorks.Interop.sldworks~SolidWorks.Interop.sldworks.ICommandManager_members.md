---
title: "ICommandManager Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICommandManager_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html"
---

# ICommandManager Interface Members

The following tables list the members exposed by [ICommandManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | NumberOfFlyoutGroups | Gets the number of flyouts in the CommandManager. |
| Property | NumberOfGroups | Gets the number of CommandGroups. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddCommandTab | Adds a tab to the CommandManager for the specified document type. |
| Method | AddContextMenu | Adds a new context-sensitive menu to the CommandManager. |
| Method | CommandTabs | Gets all of the add-in CommandManager tabs for the specified document type. |
| Method | CreateCommandGroup | Obsolete. Superseded by ICommandManager::CreateCommandGroup2 . |
| Method | CreateCommandGroup2 | Creates a new CommandGroup in the CommandManager. |
| Method | CreateFlyoutGroup | Obsolete. Superseded by ICommandManager::CreateFlyoutGroup2 . |
| Method | CreateFlyoutGroup2 | Creates a new flyout in the CommandManager and context-sensitive menus. |
| Method | GetCommandGroup | Gets the CommandGroup using the specified ID. |
| Method | GetCommandIDsCount | Gets the number of command IDs for the given command group. |
| Method | GetCommandTab | Gets the specified CommandManager tab for the specified document type. |
| Method | GetCommandTabCount | Gets the number of tabs on the CommandManager for the specified document type. |
| Method | GetFlyoutGroup | Gets the flyout with the specified ID. |
| Method | GetFlyoutGroups | Gets the flyouts in the CommandManager. |
| Method | GetGroupDataFromRegistry | Gets the command IDs of the given command group from the registry. |
| Method | GetGroups | Gets the CommandGroups in the CommandManager. |
| Method | IGetCommandTabs | Gets the CommandManager tabs for the specified document type. |
| Method | IGetGroupDataFromRegistry | Gets the command IDs of the given command group from the registry. |
| Method | IGetGroups | Gets the CommandGroups in the CommandManager. |
| Method | RemoveCommandGroup | Obsolete. Superseded by ICommandManager::RemoveCommandGroup2 . |
| Method | RemoveCommandGroup2 | Removes the specified CommandGroup from the CommandManager. |
| Method | RemoveCommandTab | Removes the specified CommandManager tab, including its tab boxes and buttons, from the CommandManager. |
| Method | RemoveFlyoutGroup | Removes the specified flyout from the CommandManager. |

[Top](#topBookmark)

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
