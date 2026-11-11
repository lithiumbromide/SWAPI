---
title: "ISelectionManager Interface Members"
project: ""
interface: "ISelectionManager_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html"
---

# ISelectionManager Interface Members

The following tables list the members exposed by [ISelectionManager](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | PaperSpaceSelectionEnabled | Gets or sets whether paper-space selection is enabled. |
| Property | RemoveOptions | Gets or sets whether to allow or disallow the selection of an entity. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ClearSelections | Clears the specified command from the selection set. |
| Method | GetPickPoints | Gets the pick points for the selection. |
| Method | GetSelectedObject | Gets the selected entity. |
| Method | GetSelectedObjectCount | Gets the number of selected entities in the current selection set. |
| Method | GetSelectedObjects | Gets the selected entities of the specified entity types. |
| Method | GetSelectionFilter | Gets the selection filter. |
| Method | SelectByCrossline | Selects the entities that intersect the specified line. |
| Method | SelectByPoint | Selects an entity at the specified point. |
| Method | SelectByPolygon | Selects only the entities within a polygon or selects the entities within and that intersect the polygon. |
| Method | SelectByWindow | Selects only the entities within the selection window or selects all of the entities within and that intersect the selection window. |

[Top](#topBookmark)

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ISelectionManager Event SelectionChangedNotify](Interop.dsAutomation~Interop.dsAutomation._ISelectionManagerEvents_SelectionChangedNotifyEventHandler.html)
[ISelectionManager Event SelectionPreNotifyEventHandler Delegate](Interop.dsAutomation~Interop.dsAutomation._ISelectionManagerEvents_SelectionPreNotifyEventHandler.html)
