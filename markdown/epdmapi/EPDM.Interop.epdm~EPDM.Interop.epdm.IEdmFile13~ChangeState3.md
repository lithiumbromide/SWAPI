---
title: "ChangeState3 Method (IEdmFile13)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile13"
member: "ChangeState3"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13~ChangeState3.html"
---

# ChangeState3 Method (IEdmFile13)

Changes the workflow state of this file.

## Syntax

### Visual Basic

```vb
Sub ChangeState3( _
   ByRef poStateIdOrName As System.Object, _
   ByRef poTransitionIdOrName As System.Object, _
   ByVal lFolderID As System.Integer, _
   ByVal bsComment As System.String, _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal lEdmStateFlags As System.Integer, _
   Optional ByVal bsPasswd As System.String _
)
```

### C#

```csharp
void ChangeState3(
   ref System.object poStateIdOrName,
   ref System.object poTransitionIdOrName,
   System.int lFolderID,
   System.string bsComment,
   System.int lParentWnd,
   System.int lEdmStateFlags,
   System.string bsPasswd
)
```

### C++/CLI

```cpp
void ChangeState3(
   System.Object^% poStateIdOrName,
   System.Object^% poTransitionIdOrName,
   System.int lFolderID,
   System.String^ bsComment,
   System.int lParentWnd,
   System.int lEdmStateFlags,
   System.String^ bsPasswd
)
```

### Parameters

- `poStateIdOrName`: Workflow state ID or name or

[IEdmState5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html)

to which this file transitions
- `poTransitionIdOrName`: ID or name of the workflow transition to use to change states (see

Remarks

)
- `lFolderID`: ID of the file's active parent folder
- `bsComment`: Comment saved to the transition history
- `lParentWnd`: Parent window handle
- `lEdmStateFlags`: Optional combination of

[EdmStateFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStateFlags.html)

bits; default is EdmStateFlags.EdmState_Simple
- `bsPasswd`: Password of user executing the transition (see

Remarks

)

## Examples

See the

[IEdmFile13](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13.html)

examples.

## Remarks

Specify poTransitionIdOrName to unambiguously specify how to transition to the new state specified by poStateIdOrName.

See[Return Codes](ReturnCodes.htm)for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_TRANSITION_ACTION_FAILED: One of the transition actions set up in the workflow failed.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the

  [EdmCmdType.EdmCmd_PreState](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html)

  hooks did not permit the operation.
- E_EDM_FILE_IS_LOCKED: The file is checked out. Changing state is only permitted on checked-in files.
- E_EDM_PERMISSION_DENIED: The logged-in user lacks permission to change state.
- E_EDM_CONDITIONS_NOT_MET: The conditions set up in the Workflow Editor for this transition were not met.
- E_EDM_STATE_NOT_FOUND: There is no transition going from the file's current state to the specified state.

## See Also

[IEdmFile13 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13.html)

[IEdmFile13 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13_members.html)

[IEdmWorkflow5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5.html)

## Availability

SOLIDWORKS PDM Professional 2018
