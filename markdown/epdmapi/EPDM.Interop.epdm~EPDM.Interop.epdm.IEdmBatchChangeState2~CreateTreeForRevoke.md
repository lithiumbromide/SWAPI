---
title: "CreateTreeForRevoke Method (IEdmBatchChangeState2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState2"
member: "CreateTreeForRevoke"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2~CreateTreeForRevoke.html"
---

# CreateTreeForRevoke Method (IEdmBatchChangeState2)

Computes the file reference tree and checks that the specified transition revocation can be performed for the files added to this batch using [IEdmBatchChangeState::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~AddFile.html).

## Syntax

### Visual Basic

```vb
Function CreateTreeForRevoke( _
   ByVal bsTransition As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool CreateTreeForRevoke(
   System.string bsTransition
)
```

### C++/CLI

```cpp
System.bool CreateTreeForRevoke(
   System.String^ bsTransition
)
```

### Parameters

- `bsTransition`: Name of the workflow state transition to revoke

### Return Value

True if there are any valid files on which to revoke transitions, false if there are no valid files

## Examples

See the [IEdmBatchChangeState2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2.html) examples.

## Remarks

To include parent files in the file reference tree, call [IEdmBatchChangeState5::IncludeParentsForRevokeTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState5~IncludeParentsForRevokeTree.html).

After calling this method, call [IEdmBatchChangeState::ShowDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ShowDlg.html) and/or [IEdmBatchChangeState::ChangeState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~ChangeState.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchChangeState2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2.html)
[IEdmBatchChangeState2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
