---
title: "RunTask Method (IEdmTaskMgr)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskMgr"
member: "RunTask"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr~RunTask.html"
---

# RunTask Method (IEdmTaskMgr)

Runs the specified task add-in.

## Syntax

### Visual Basic

```vb
Sub RunTask( _
   ByVal oTask As EdmTaskInfo, _
   ByVal poSelections() As EdmSelItem2, _
   ByVal lParentWnd As System.Integer _
)
```

### C#

```csharp
void RunTask(
   EdmTaskInfo oTask,
   EdmSelItem2[] poSelections,
   System.int lParentWnd
)
```

### C++/CLI

```cpp
void RunTask(
   EdmTaskInfo oTask,
   array<EdmSelItem2>^ poSelections,
   System.int lParentWnd
)
```

### Parameters

- `oTask`: Task add-in to run as defined by [EdmTaskInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskInfo.html)
- `poSelections`: Array of [EdmSelItem2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem2.html)
- `lParentWnd`: Parent window

## Examples

See the [IEdmTaskMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr.html) example.

## See Also

[IEdmTaskMgr Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr.html)
[IEdmTaskMgr Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskMgr_members.html)

## Availability

SOLIDWORKS PDM Professional 2018 SP04
