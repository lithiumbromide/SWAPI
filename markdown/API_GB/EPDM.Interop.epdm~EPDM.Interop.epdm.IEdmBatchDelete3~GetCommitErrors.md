---
title: "GetCommitErrors Method (IEdmBatchDelete3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchDelete3"
member: "GetCommitErrors"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3~GetCommitErrors.html"
---

# GetCommitErrors Method (IEdmBatchDelete3)

Shows the errors that occurred during [IEdmBatchDelete::CommitDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete~CommitDelete.html).

## Syntax

### Visual Basic

```vb
Sub GetCommitErrors( _
   ByRef ppoDelErrors As EdmBatchDelErrInfo() _
)
```

### C#

```csharp
void GetCommitErrors(
   out EdmBatchDelErrInfo[] ppoDelErrors
)
```

### C++/CLI

```cpp
void GetCommitErrors(
   [Out] array<EdmBatchDelErrInfo> ppoDelErrors
)
```

### Parameters

- `ppoDelErrors`: Array of [EdmBatchDelErrInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchDelErrInfo.html) structures; one for each error that occurred during IEdmBatchDelete::CommitDelete

## Examples

See the [IEdmBatchDelete](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete.html) examples.

## Remarks

Call this method after calling IEdmBatchDelete::CommitDelete.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_NOT_INITIALIZED: IEdmBatchDelete::CommitDelete has not been called.

## See Also

[IEdmBatchDelete3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3.html)
[IEdmBatchDelete3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchDelete3_members.html)

## Availability

SOLIDWORKS PDM Professional 2012
