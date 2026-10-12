---
title: "Rollback3 Method (IEdmVersion8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVersion8"
member: "Rollback3"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion8~Rollback3.html"
---

# Rollback3 Method (IEdmVersion8)

Discards all versions of the file after this version.

## Syntax

### Visual Basic

```vb
Sub Rollback3( _
   ByVal bsComment As System.String, _
   ByVal vbRedirectParentRefs As System.Boolean _
)
```

### C#

```csharp
void Rollback3(
   System.string bsComment,
   System.bool vbRedirectParentRefs
)
```

### C++/CLI

```cpp
void Rollback3(
   System.String^ bsComment,
   System.bool vbRedirectParentRefs
)
```

### Parameters

- `bsComment`: Comment for this rollback
- `vbRedirectParentRefs`: True to roll back the file with its parent references, false to roll back the file without its parent references

## Remarks

This method deletes both the file data and the file data card data when it deletes versions. You cannot undo this rollback, unless you restore a complete backup of the database and the file archives.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The user does not have permission to delete files.
- E_EDM_INVALID_REVISION_NUMBER: The version does not exist.

## See Also

[IEdmVersion8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion8.html)
[IEdmVersion8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion8_members.html)
[IEdmRevision7::Rollback3 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision7~Rollback3.html)
[IEdmEnumeratorVersion7::Rollback3 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion7~Rollback3.html)

## Availability

SOLIDWORKS PDM Professional 2017
