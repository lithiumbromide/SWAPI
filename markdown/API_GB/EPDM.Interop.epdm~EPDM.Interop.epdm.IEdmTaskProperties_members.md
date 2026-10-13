---
title: "IEdmTaskProperties Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties_members"
member: ""
kind: "members"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html"
---

# IEdmTaskProperties Interface Members

The following tables list the members exposed by [IEdmTaskProperties](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AddInName | Gets the name of the add-in that is used to execute this task. |
| Property | FormName | Gets the name of the data card to show when the task is launched. |
| Property | IsScheduled | Gets whether this task is scheduled. |
| Property | RetryCount | Gets the number of times to retry the task on failure. |
| Property | TaskFlags | Gets or sets task-specific options. |
| Property | TaskGUID | Gets the unique ID of this task definition. |
| Property | TaskID | Gets the database ID of this task definition. |
| Property | TaskName | Gets the name of this task. |
| Property | TimeoutInSeconds | Gets the number of seconds to wait until failing the task. |
| Property | UserName | Gets the name of the user as whom to execute this task. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetMenuCmds | Gets the menu commands set with IEdmTaskProperties::SetMenuCmds . |
| Method | GetSel | Gets the selection of objects on which to execute this task. |
| Method | GetSetupPages | Gets the setup pages added to the task property dialog box using IEdmTaskProperties::SetSetupPages . |
| Method | GetValEx | Gets the value of a user-defined variable created with IEdmTaskProperties::SetValEx . |
| Method | GetVar | Gets the value of a card variable created in the administration tool and set by IEdmTaskProperties::SetVar . |
| Method | SetMenuCmds | Adds the specified menu commands to File Explorer context menus. |
| Method | SetSel | Sets the selection of objects on which to execute this task. |
| Method | SetSetupPages | Adds setup pages to the task property dialog box for this task definition. |
| Method | SetValEx | Sets a value for the specified user-defined variable. |
| Method | SetVar | Sets the value of a card variable created in the administration tool. |

[Top](#topBookmark)

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Task Add-in Sample](TaskSample.htm)
[Standard Task Add-in](StandardTaskAddIn.htm)
[IEdmTaskMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr.html)
