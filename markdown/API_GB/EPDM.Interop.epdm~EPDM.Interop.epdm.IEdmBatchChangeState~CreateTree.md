---
title: "CreateTree Method (IEdmBatchChangeState)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState"
member: "CreateTree"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~CreateTree.html"
---

# CreateTree Method (IEdmBatchChangeState)

Computes the file reference tree and checks that the specified state transition can be performed for the files added to this batch using [IEdmBatchChangeState::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~AddFile.html).

## Syntax

### Visual Basic

```vb
Function CreateTree( _
   ByVal bsTransition As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool CreateTree(
   System.string bsTransition
)
```

### C++/CLI

```cpp
System.bool CreateTree(
   System.String^ bsTransition
)
```

### Parameters

- `bsTransition`: Name of the workflow state transition to perform

### Return Value

True if there are any valid state changes, false if not

## Examples

See the [IEdmBatchChangeState4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4.html) examples.

## Remarks

If you are revoking transitions, instead of calling this method, call [IEdmBatchChangeState2::CreateTreeForRevoke](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2~CreateTreeForRevoke.html).

After calling this method, call [IEdmBatchChangeState::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ShowDlg.html) and/or [IEdmBatchChangeState::ChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ChangeState.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchChangeState Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.html)
[IEdmBatchChangeState Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
