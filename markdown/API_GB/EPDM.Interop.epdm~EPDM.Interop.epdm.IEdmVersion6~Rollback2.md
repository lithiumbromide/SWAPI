---
title: "Rollback2 Method (IEdmVersion6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVersion6"
member: "Rollback2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion6~Rollback2.html"
---

# Rollback2 Method (IEdmVersion6)

Obsolete. Superseded by [IEdmVersion8::Rollback3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion8~Rollback3.html).

## Syntax

### Visual Basic

```vb
Sub Rollback2( _
   ByVal bsComment As System.String _
)
```

### C#

```csharp
void Rollback2(
   System.string bsComment
)
```

### C++/CLI

```cpp
void Rollback2(
   System.String^ bsComment
)
```

### Parameters

- `bsComment`: Comment for this rollback

## Remarks

This method deletes both the file data and the file data card data when it deletes versions. You cannot undo this rollback, unless you restore a complete backup of the database and the file archives.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The user does not have permission to delete files.
- E_EDM_INVALID_REVISION_NUMBER: The version does not exist.

## See Also

[IEdmVersion6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion6.html)
[IEdmVersion6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion6_members.html)
[IEdmEnumeratorVersion6::Rollback2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion6~Rollback2.html)
[IEdmRevision6::Rollback2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision6~Rollback2.html)

## Availability

SOLIDWORKS PDM Professional 2015
