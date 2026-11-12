---
title: "IncludeParentsForRevokeTree Method (IEdmBatchChangeState5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState5"
member: "IncludeParentsForRevokeTree"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState5~IncludeParentsForRevokeTree.html"
---

# IncludeParentsForRevokeTree Method (IEdmBatchChangeState5)

Gets or sets whether to include parent files in the [file reference tree to revoke transactions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState2~CreateTreeForRevoke.html).

## Syntax

### Visual Basic

```vb
Sub IncludeParentsForRevokeTree( _
   ByVal bInclude As System.Boolean _
)
```

### C#

```csharp
void IncludeParentsForRevokeTree(
   System.bool bInclude
)
```

### C++/CLI

```cpp
void IncludeParentsForRevokeTree(
   System.bool bInclude
)
```

### Parameters

- `bInclude`: True to include parent files in the file reference tree to revoke transactions, false to not

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The argument is invalid.

## See Also

[IEdmBatchChangeState5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState5.html)
[IEdmBatchChangeState5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState5_members.html)

## Availability

SOLIDWORKS PDM Professional 2015 SP04
