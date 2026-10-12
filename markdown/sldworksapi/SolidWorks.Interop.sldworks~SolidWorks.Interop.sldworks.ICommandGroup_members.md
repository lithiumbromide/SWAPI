---
title: "ICommandGroup Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html"
---

# ICommandGroup Interface Members

The following tables list the members exposed by [ICommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CommandID | Gets the command ID for the specified item in the CommandGroup. |
| Property | CustomNames | Gets or sets the custom names in the CommandGroup. |
| Property | DockingState | Gets or sets the docking state of the toolbar in the CommandGroup. |
| Property | HasEnabledButton | Gets whether any buttons in this CommandGroup are enabled. |
| Property | HasMenu | Gets or sets whether this CommandGroup has a menu. |
| Property | HasToolbar | Gets or sets whether this CommandGroup has a toolbar. |
| Property | IconList | Gets or sets the paths for the icons for the toolbar buttons and separators for this CommandGroup. |
| Property | LargeIconList | Obsolete. Superseded by ICommandGroup::IconList . |
| Property | LargeMainIcon | Obsolete. Superseded by ICommandGroup::MainIconList . |
| Property | MainIconList | Gets or sets the paths for the icons for the buttons for this CommandGroup. |
| Property | MenuPosition | Gets or sets the position of the CommandGroup for the specified document templates. |
| Property | Name | Gets the name of the CommandGroup. |
| Property | NumberOfGroupItems | Gets the number of items in the CommandGroup. |
| Property | SelectType | This property: gets the type of object selected on the context sensitive, pop-up menu. sets the type of object that the user must select to show the context sensitive, pop-up menu. |
| Property | ShowInDocumentType | Gets or sets the types of documents to show this CommandGroup. |
| Property | SmallIconList | Obsolete. Superseded by ICommandGroup::IconList . |
| Property | SmallMainIcon | Obsolete. Superseded by ICommandGroup::MainIconList . |
| Property | ToolbarId | Gets the toolbar ID of this CommandGroup. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Activate | Activates the CommandGroup. |
| Method | AddCommandItem | Obsolete. Superseded by ICommandGroup::AddComandItem2 . |
| Method | AddCommandItem2 | Adds a combination menu item and toolbar item to a CommandGroup. |
| Method | AddSpacer | Obsolete. Superseded by ICommandGroup::AddSpacer2 . |
| Method | AddSpacer2 | Adds a spacer between items in a CommandGroup. |
| Method | GetToolbarVisibility | Gets whether this toolbar is visible. |
| Method | SetToolbarVisibility | Sets the visibility of the toolbar in the CommandGroup. |

[Top](#topBookmark)

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
