---
title: "ChangeState2 Method (IEdmBatchChangeState4)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState4"
member: "ChangeState2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4~ChangeState2.html"
---

# ChangeState2 Method (IEdmBatchChangeState4)

Changes states or revokes transitions of all the files added to this batch using [IEdmBatchChangeState::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~AddFile.html).

## Syntax

### Visual Basic

```vb
Sub ChangeState2( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsPasswd As System.String, _
   Optional ByVal poCallback As EdmCallback _
)
```

### C#

```csharp
void ChangeState2(
   System.int lParentWnd,
   System.string bsPasswd,
   EdmCallback poCallback
)
```

### C++/CLI

```cpp
void ChangeState2(
   System.int lParentWnd,
   System.String^ bsPasswd,
   EdmCallback^ poCallback
)
```

### Parameters

- `lParentWnd`: Parent window handle that is passed to add-ins that are notified about file state changes in the vault
- `bsPasswd`: Password of user executing the transition
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to receive progress information about the operation

## Examples

See the [IEdmBatchChangeState4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4.html) examples.

## Remarks

The difference between this method and the now obsolete [IEdmBatchChangeState::ChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ChangeState.html) is that this method specifies a user password that allows the file to change state if the transition requires authentication ([IEdmTransition10::Authentication](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition10~Authentication.html)).

Before calling this method, you must call [IEdmBatchChangeState::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~CreateTree.html) if changing states or [IEdmBatchChangeState2::CreateTreeForRevoke](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2~CreateTreeForRevoke.html) if revoking transitions.

[Return codes](ReturnCodes.htm):

- E_EDM_STATECHANGE_FAILED: The password is invalid.
- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchChangeState4 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4.html)
[IEdmBatchChangeState4 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4_members.html)

## Availability

SOLIDWORKS PDM Professional 2015 SP02
