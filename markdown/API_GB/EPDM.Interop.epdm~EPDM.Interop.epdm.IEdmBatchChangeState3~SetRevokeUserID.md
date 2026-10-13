---
title: "SetRevokeUserID Method (IEdmBatchChangeState3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState3"
member: "SetRevokeUserID"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState3~SetRevokeUserID.html"
---

# SetRevokeUserID Method (IEdmBatchChangeState3)

Sets the ID of the user allowed to revoke state transitions of files in this batch.

## Syntax

### Visual Basic

```vb
Sub SetRevokeUserID( _
   ByVal lUserID As System.Integer _
)
```

### C#

```csharp
void SetRevokeUserID(
   System.int lUserID
)
```

### C++/CLI

```cpp
void SetRevokeUserID(
   System.int lUserID
)
```

### Parameters

- `lUserID`: ID of user allowed to revoke state transitions of files

## Examples

See the [IEdmBatchChangeState3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState3.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchChangeState3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState3.html)
[IEdmBatchChangeState3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState3_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
