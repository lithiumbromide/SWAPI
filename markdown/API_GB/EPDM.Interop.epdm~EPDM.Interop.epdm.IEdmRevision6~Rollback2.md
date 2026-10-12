---
title: "Rollback2 Method (IEdmRevision6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevision6"
member: "Rollback2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision6~Rollback2.html"
---

# Rollback2 Method (IEdmRevision6)

Obsolete. Superseded by [IEdmRevision7::Rollback3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision7~Rollback3.html).

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

- `bsComment`: Comment for this revision

## Remarks

This method destroys all versions after this revision number. To undo this rollback operation, you need to restore a backup of the entire database and file archives.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The user lacks permission to delete files.

## See Also

[IEdmRevision6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision6.html)
[IEdmRevision6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision6_members.html)
[IEdmEnumeratorVersion6::Rollback2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion6~Rollback2.html)
[IEdmVersion6::Rollback2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion6~Rollback2.html)

## Availability

SOLIDWORKS PDM Professional 2015
