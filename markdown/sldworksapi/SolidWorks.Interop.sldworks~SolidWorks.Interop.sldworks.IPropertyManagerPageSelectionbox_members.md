---
title: "IPropertyManagerPageSelectionbox Interface Members"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html"
---

# IPropertyManagerPageSelectionbox Interface Members

The following tables list the members exposed by [IPropertyManagerPageSelectionbox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AllowMultipleSelectOfSameEntity | Gets or sets whether the same entity can be selected multiple times in this selection box. |
| Property | AllowSelectInMultipleBoxes | Gets or sets whether an entity can be selected in this selection box if the entity is selected elsewhere. |
| Property | Callout | Gets or sets a multi-row, editable callout for this selection box. |
| Property | CurrentSelection | Gets or sets the index number of the currently selected item in this selection box. |
| Property | EnableSelectIdenticalComponents | Gets or sets whether to enable Select Identical Components in the context menu of this PropertyManager page selection box. |
| Property | Height | Gets or sets the height of this selection box. |
| Property | ItemCount | Gets the number of items currently in this selection box. |
| Property | ItemText | Gets the specified item in this selection box. |
| Property | Mark | Gets or sets the mark used on selected items in this selection box. |
| Property | SelectionIndex | Gets the index number of the currently selected item in the selection box. |
| Property | SingleEntityOnly | Gets or sets whether this selection box is for single or multiple items. |
| Property | Style | Gets or sets style of this selection box. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddMenuPopupItem | Adds a menu item to the pop-up menu for this selection box of the PropertyManager page. |
| Method | GetSelectedItems | Gets the items selected in a PropertyManager selection box. |
| Method | GetSelectedItemsCount | Gets the number of currently selected items in this PropertyManager selection box. |
| Method | GetSelectionFocus | Gets whether this is the active selection box. |
| Method | IGetSelectedItems | Gets the items selected in a PropertyManager selection box. |
| Method | ISetSelectionFilters | Defines the types of objects the user can select for this selection box. |
| Method | SetCalloutLabel | Sets the default callout label for selections made in this selection box on the PropertyManager page. |
| Method | SetSelectedItem | Sets whether an item is selected or cleared in a selection box enabled for multiple selection . |
| Method | SetSelectionColor | Sets the color for selections made in this selection box on the PropertyManager page. |
| Method | SetSelectionFilters | Defines the types of objects the user can select for this selection box. |
| Method | SetSelectionFocus | Sets this object as the active selection box. |

[Top](#topBookmark)

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
