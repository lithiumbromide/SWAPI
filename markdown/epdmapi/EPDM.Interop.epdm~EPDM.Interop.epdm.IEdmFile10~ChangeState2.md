---
title: "ChangeState2 Method (IEdmFile10)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile10"
member: "ChangeState2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile10~ChangeState2.html"
---

# ChangeState2 Method (IEdmFile10)

Obsolete. Superseded by

[IEdmFile13::ChangeState3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13~ChangeState3.html)

.

## Syntax

### Visual Basic

```vb
Sub ChangeState2( _
   ByRef poStateIdOrName As System.Object, _
   ByVal lFolderID As System.Integer, _
   ByVal bsComment As System.String, _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal lEdmStateFlags As System.Integer, _
   Optional ByVal bsPasswd As System.String _
)
```

### C#

```csharp
void ChangeState2(
   ref System.object poStateIdOrName,
   System.int lFolderID,
   System.string bsComment,
   System.int lParentWnd,
   System.int lEdmStateFlags,
   System.string bsPasswd
)
```

### C++/CLI

```cpp
void ChangeState2(
   System.Object^% poStateIdOrName,
   System.int lFolderID,
   System.String^ bsComment,
   System.int lParentWnd,
   System.int lEdmStateFlags,
   System.String^ bsPasswd
)
```

### Parameters

- `poStateIdOrName`: Workflow state ID or name or[IEdmState5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html)to which this file transitions (see**Remarks**)
- `lFolderID`: ID of the file's active parent folder
- `bsComment`: Comment saved to the transition history
- `lParentWnd`: Parent window handle
- `lEdmStateFlags`: Optional combination of

[EdmStateFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStateFlags.html)

bits; default is EdmStateFlags.EdmState_Simple
- `bsPasswd`: Optional password of user executing the transition

## Remarks

The difference between this method and the now obsolete[IEdmFile5::ChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~ChangeState.html)is that this method requires a user password.

There must be a transition between the current state and poStateIdOrName, or this method fails.

It is possible to create multiple workflows with two or more states having the same name. If poStateIdOrName contains the name of the destination state instead of its ID, and if several transitions from the file’s current state lead to new states all having the same name, SOLIDWORKS PDM Professional randomly selects one of them. To be sure to which state the file transitions, specify a state ID in poStateIdOrName.

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

[IEdmFile10 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile10.html)

[IEdmFile10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile10_members.html)

[IEdmWorkflow5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5.html)

[IEdmTransition5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5.html)

## Availability

SOLIDWORKS PDM Professional 2015 SP02
