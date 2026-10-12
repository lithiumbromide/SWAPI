---
title: "SetStatus Method (IEdmTaskInstance)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance"
member: "SetStatus"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetStatus.html"
---

# SetStatus Method (IEdmTaskInstance)

Sets the specified status of this task instance.

## Syntax

### Visual Basic

```vb
Sub SetStatus( _
   ByVal eStatus As EdmTaskStatus, _
   Optional ByVal lHRESULT As System.Integer, _
   Optional ByVal bsCustomMsg As System.String, _
   Optional ByVal oNotificationAttachments As System.Object, _
   Optional ByVal bsExtraNotificationMsg As System.String _
)
```

### C#

```csharp
void SetStatus(
   EdmTaskStatus eStatus,
   System.int lHRESULT,
   System.string bsCustomMsg,
   System.object oNotificationAttachments,
   System.string bsExtraNotificationMsg
)
```

### C++/CLI

```cpp
void SetStatus(
   EdmTaskStatus eStatus,
   System.int lHRESULT,
   System.String^ bsCustomMsg,
   System.Object^ oNotificationAttachments,
   System.String^ bsExtraNotificationMsg
)
```

### Parameters

- `eStatus`: Status of this task as defined in [EdmTaskStatus](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskStatus.html)
- `lHRESULT`: Optional error code to display in the properties window when terminating the task; valid only if eStatus is EdmTaskStatus.EdmTaskStat_DoneFailed
- `bsCustomMsg`: Optional error message to display when terminating the task; valid only if eStatus is EdmTaskStatus.EdmTaskStat_DoneFailed
- `oNotificationAttachments`: Optional array of [EdmSelItem2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem2.html) structures; one structure for each file link to add to the notification message that is sent when the task completes
- `bsExtraNotificationMsg`: Optional message to append to the notification message that is sent when the task completes

## Examples

See the examples in [IEdmTaskInstance](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html).

## Remarks

The task add-in calls this method to inform the framework about the current status of the task.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskInstance Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
[IEdmTaskInstance Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html)
[IEdmTaskInstance::GetStatus Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetStatus.html)

## Availability

SOLIDWORKS PDM Professional 2010
