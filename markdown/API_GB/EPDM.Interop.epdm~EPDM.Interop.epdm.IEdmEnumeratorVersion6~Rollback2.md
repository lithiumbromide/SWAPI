---
title: "Rollback2 Method (IEdmEnumeratorVersion6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion6"
member: "Rollback2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion6~Rollback2.html"
---

# Rollback2 Method (IEdmEnumeratorVersion6)

Obsolete. Superseded by [IEdmEnumeratorVersion7::Rollback3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion7~Rollback3.html).

## Syntax

### Visual Basic

```vb
Sub Rollback2( _
   ByVal lVersionNo As System.Integer, _
   ByVal bsComment As System.String _
)
```

### C#

```csharp
void Rollback2(
   System.int lVersionNo,
   System.string bsComment
)
```

### C++/CLI

```cpp
void Rollback2(
   System.int lVersionNo,
   System.String^ bsComment
)
```

### Parameters

- `lVersionNo`: Version number to which to roll this file back (see **Remarks**)
- `bsComment`: Comment for the rollback

## Remarks

This method destroys all versions after the version specified by lVersionNo. There is no undoing of the operation short of restoring a backup of the entire database and file archives.

After this method completes successfully, lVersionNo is the new latest version of the file.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_REVISION_NUMBER: The specified version number is out of bounds.
- E_EDM_PERMISSION_DENIED: The user lacks permission to delete files.

## See Also

[IEdmEnumeratorVersion6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion6.html)
[IEdmEnumeratorVersion6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion6_members.html)
[IEdmVersion6::Rollback2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion6~Rollback2.html)
[IEdmRevision6::Rollback2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision6~Rollback2.html)

## Availability

SOLIDWORKS PDM Professional 2015
