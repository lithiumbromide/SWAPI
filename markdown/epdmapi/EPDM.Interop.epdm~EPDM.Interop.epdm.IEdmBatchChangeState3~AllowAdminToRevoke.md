---
title: "AllowAdminToRevoke Method (IEdmBatchChangeState3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState3"
member: "AllowAdminToRevoke"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState3~AllowAdminToRevoke.html"
---

# AllowAdminToRevoke Method (IEdmBatchChangeState3)

Sets whether an administrator is allowed to revoke state transitions of files in this batch.

## Syntax

### Visual Basic

```vb
Sub AllowAdminToRevoke( _
   ByVal bAllowAdminToRevoke As System.Boolean _
)
```

### C#

```csharp
void AllowAdminToRevoke(
   System.bool bAllowAdminToRevoke
)
```

### C++/CLI

```cpp
void AllowAdminToRevoke(
   System.bool bAllowAdminToRevoke
)
```

### Parameters

- `bAllowAdminToRevoke`: True to allow an administrator to revoke state transitions of files, false to not

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
