---
title: "SetProgressRange Method (IEdmTaskInstance)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskInstance"
member: "SetProgressRange"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetProgressRange.html"
---

# SetProgressRange Method (IEdmTaskInstance)

Sets the range of the progress bar for the execution of this task instance.

## Syntax

### Visual Basic

```vb
Sub SetProgressRange( _
   ByVal lMax As System.Integer, _
   ByVal lPos As System.Integer, _
   ByVal bsDocStr As System.String _
)
```

### C#

```csharp
void SetProgressRange(
   System.int lMax,
   System.int lPos,
   System.string bsDocStr
)
```

### C++/CLI

```cpp
void SetProgressRange(
   System.int lMax,
   System.int lPos,
   System.String^ bsDocStr
)
```

### Parameters

- `lMax`: Maximum position in the progress bar
- `lPos`: 0 <= Current position in the progress bar <= lMax
- `bsDocStr`: Description of what the add-in is currently doing

## Examples

See the examples in [IEdmTaskInstance](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html).

## Remarks

The task add-in calls this method at the start of processing of the hook, [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd.TaskRun, to initialize the task list progress bar in the task list window of the PDM Administration tool.

The task add-in calls [IEdmTaskInstance::SetProgressPos](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetProgressPos.html) periodically during processing of the hook, EdmCmdType.EdmCmd.TaskRun, to update the progress bar.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskInstance Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)
[IEdmTaskInstance Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
