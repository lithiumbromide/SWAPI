---
title: "SetProgressPos Method (IEdmTaskInstance)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance"
member: "SetProgressPos"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetProgressPos.html"
---

# SetProgressPos Method (IEdmTaskInstance)

Updates the task list progress bar during execution of this task instance.

## Syntax

### Visual Basic

```vb
Sub SetProgressPos( _
   ByVal lPos As System.Integer, _
   ByVal bsDocStr As System.String _
)
```

### C#

```csharp
void SetProgressPos(
   System.int lPos,
   System.string bsDocStr
)
```

### C++/CLI

```cpp
void SetProgressPos(
   System.int lPos,
   System.String^ bsDocStr
)
```

### Parameters

- `lPos`: Current position of the progress bar
- `bsDocStr`: Description of what the add-in is currently doing

## Examples

See the examples in [IEdmTaskInstance](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html).

## Remarks

The task add-in calls this method periodically during processing of the hook, [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd.TaskRun, to update the progress bar in the task list window of the PDM Administration tool.

Initialize the task list progress bar by calling [IEdmTaskinstance::SetProgressRange](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetProgressRange.html) at the start of processing of the hook, EdmCmdType.EdmCmd.TaskRun.

lPos is between 0 and lMax of IEdmTaskinstance::SetProgressRange.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskInstance Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
[IEdmTaskInstance Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
