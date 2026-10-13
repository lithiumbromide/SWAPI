---
title: "Rollback3 Method (IEdmEnumeratorVersion7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion7"
member: "Rollback3"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion7~Rollback3.html"
---

# Rollback3 Method (IEdmEnumeratorVersion7)

Rolls this file back to the specified version.

## Syntax

### Visual Basic

```vb
Sub Rollback3( _
   ByVal lVersionNo As System.Integer, _
   ByVal bsComment As System.String, _
   ByVal vbRedirectParentRefs As System.Boolean _
)
```

### C#

```csharp
void Rollback3(
   System.int lVersionNo,
   System.string bsComment,
   System.bool vbRedirectParentRefs
)
```

### C++/CLI

```cpp
void Rollback3(
   System.int lVersionNo,
   System.String^ bsComment,
   System.bool vbRedirectParentRefs
)
```

### Parameters

- `lVersionNo`: Version number to which to roll this file back (see **Remarks**)
- `bsComment`: Comment for the rollback
- `vbRedirectParentRefs`: True to roll back the file with parent references, false to roll back the file without parent references

## Remarks

This method destroys all versions after the version specified by lVersionNo. There is no undoing of the operation short of restoring a backup of the entire database and file archives.

After this method completes successfully, lVersionNo is the new latest version of the file.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_REVISION_NUMBER: The specified version number is out of bounds.
- E_EDM_PERMISSION_DENIED: The user lacks permission to delete files.

## See Also

[IEdmEnumeratorVersion7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion7.html)
[IEdmEnumeratorVersion7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion7_members.html)
[IEdmRevision7::Rollback3 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision7~Rollback3.html)
[IEdmVersion8::Rollback3 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion8~Rollback3.html)

## Availability

SOLIDWORKS PDM Professional 2017
