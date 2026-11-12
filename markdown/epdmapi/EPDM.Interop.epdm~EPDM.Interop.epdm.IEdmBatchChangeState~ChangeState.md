---
title: "ChangeState Method (IEdmBatchChangeState)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState"
member: "ChangeState"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ChangeState.html"
---

# ChangeState Method (IEdmBatchChangeState)

Obsolete. Superseded by [IEdmBatchChangeState4::ChangeState2.](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4~ChangeState2.html)

## Syntax

### Visual Basic

```vb
Sub ChangeState( _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal poCallback As EdmCallback _
)
```

### C#

```csharp
void ChangeState(
   System.int lParentWnd,
   EdmCallback poCallback
)
```

### C++/CLI

```cpp
void ChangeState(
   System.int lParentWnd,
   EdmCallback^ poCallback
)
```

### Parameters

- `lParentWnd`: Parent window handle that is passed to add-ins that are notified about file state changes in the vault
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to receive progress information about the operation

## Remarks

Before calling this method, you must call [IEdmBatchChangeState::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~CreateTree.html) if changing states or [IEdmBatchChangeState2::CreateTreeForRevoke](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2~CreateTreeForRevoke.html) if revoking transitions.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchChangeState Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.html)
[IEdmBatchChangeState Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState_members.html)

## Availability

SOLIDWORKS PDM Professional 2009; for revoking a transition, SOLIDWORKS PDM Professional 2013
