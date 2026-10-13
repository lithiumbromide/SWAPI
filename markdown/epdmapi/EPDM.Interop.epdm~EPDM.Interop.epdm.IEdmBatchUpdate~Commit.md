---
title: "Commit Method (IEdmBatchUpdate)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUpdate"
member: "Commit"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate~Commit.html"
---

# Commit Method (IEdmBatchUpdate)

Obsolete. Superseded by [IEdmBatchUpdate2::CommitUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~CommitUpdate.html).

## Syntax

### Visual Basic

```vb
Sub Commit( _
   ByRef ppoRetErrors() As EdmBatchError, _
   Optional ByVal poCallback As EdmCallback _
)
```

### C#

```csharp
void Commit(
   out EdmBatchError[] ppoRetErrors,
   EdmCallback poCallback
)
```

### C++/CLI

```cpp
void Commit(
   [Out] array<EdmBatchError>^ ppoRetErrors,
   EdmCallback^ poCallback
)
```

### Parameters

- `ppoRetErrors`: Array of [EdmBatchError](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError.html) structures; one structure for each error that occurred during the save operation
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to get more information during the operation

## Remarks

Non-fatal errors are returned in the ppoRetErrors array. Examine the contents of the returned array to determine whether the operation is successful.

See the [IEdmBatchUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate.html) remarks for information about using this method.

## See Also

[IEdmBatchUpdate Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate.html)
[IEdmBatchUpdate Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.2
