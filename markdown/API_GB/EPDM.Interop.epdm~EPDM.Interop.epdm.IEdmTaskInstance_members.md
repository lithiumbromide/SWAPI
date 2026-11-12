---
title: "IEdmTaskInstance Interface Members"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance_members"
member: ""
kind: "members"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html"
---

# IEdmTaskInstance Interface Members

The following tables list the members exposed by [IEdmTaskInstance](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ID | Gets the database ID of this task instance. |
| Property | InstanceGUID | Gets the task instance GUID. |
| Property | TaskGUID | Gets the task definition GUID. |
| Property | TaskName | Gets the name of this task. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetStatus | Gets the current status of this task instance. |
| Method | GetValEx | Gets the value of the specified user-defined variable. |
| Method | GetVar | Gets the value of a card variable created in the administration tool. |
| Method | SetProgressPos | Updates the task list progress bar during execution of this task instance. |
| Method | SetProgressRange | Sets the range of the progress bar for the execution of this task instance. |
| Method | SetStatus | Sets the specified status of this task instance. |
| Method | SetValEx | Sets a value for the specified user-defined variable. |
| Method | SetVar | Sets the value of a card variable created in the administration tool. |

[Top](#topBookmark)

## See Also

[IEdmTaskInstance Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Task Add-in Sample](TaskSample.htm)
[Standard Task Add-in](StandardTaskAddIn.htm)
[IEdmTaskMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr.html)
