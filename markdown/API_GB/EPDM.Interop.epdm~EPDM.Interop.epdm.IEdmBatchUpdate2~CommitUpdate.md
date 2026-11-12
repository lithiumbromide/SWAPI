---
title: "CommitUpdate Method (IEdmBatchUpdate2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUpdate2"
member: "CommitUpdate"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~CommitUpdate.html"
---

# CommitUpdate Method (IEdmBatchUpdate2)

Commits all of the file and folder card variable updates in this batch.

## Syntax

### Visual Basic

```vb
Function CommitUpdate( _
   ByRef ppoRetErrors As EdmBatchError2(), _
   Optional ByVal poCallback As EdmCallback _
) As System.Integer
```

### C#

```csharp
System.int CommitUpdate(
   out EdmBatchError2[] ppoRetErrors,
   EdmCallback poCallback
)
```

### C++/CLI

```cpp
System.int CommitUpdate(
   [Out] array<EdmBatchError2> ppoRetErrors,
   EdmCallback^ poCallback
)
```

### Parameters

- `ppoRetErrors`: Array of [EdmBatchError2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError2.html) structures; one structure for each non-critical error that occurred during the update
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to get more information during the operation

### Return Value

Size of ppoRetErrors array; 0 if no errors

## Examples

See the [IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchUpdate2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html)
[IEdmBatchUpdate2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
