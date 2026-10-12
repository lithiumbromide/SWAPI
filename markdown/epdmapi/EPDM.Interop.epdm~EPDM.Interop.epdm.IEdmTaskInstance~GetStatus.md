---
title: "GetStatus Method (IEdmTaskInstance)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance"
member: "GetStatus"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetStatus.html"
---

# GetStatus Method (IEdmTaskInstance)

Gets the current status of this task instance.

## Syntax

### Visual Basic

```vb
Function GetStatus() As EdmTaskStatus
```

### C#

```csharp
EdmTaskStatus GetStatus()
```

### C++/CLI

```cpp
EdmTaskStatus GetStatus();
```

### Return Value

Status as defined in [EdmTaskStatus](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskStatus.html)

## Remarks

The add-in calls this method regularly during the processing of [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskRun to see if the task has been canceled or suspended in the task list user interface.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskInstance Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
[IEdmTaskInstance Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html)
[IEdmTaskInstance::SetStatus Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetStatus.html)
[Task Add-in Sample](TaskSample.htm)

## Availability

SOLIDWORKS PDM Professional 2010
