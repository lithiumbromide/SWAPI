---
title: "Rollback3 Method (IEdmRevision7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevision7"
member: "Rollback3"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision7~Rollback3.html"
---

# Rollback3 Method (IEdmRevision7)

Rolls this file back to the version of this revision.

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

- `bsComment`: Comment for this revision
- `vbRedirectParentRefs`: True to roll back the file with its parent references, false to roll back the file without its parent references

## Examples

[Roll Back Revisions (C#)](Roll_Back_Revisions_Example_CSharp.htm)
[Roll Back Revisions (VB.NET)](Roll_Back_Revisions_Example_VBNET.htm)

## Remarks

This method destroys all versions after this revision number. To undo this rollback operation, you need to restore a backup of the entire database and file archives.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The user lacks permission to delete files.

## See Also

[IEdmRevision7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision7.html)
[IEdmRevision7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision7_members.html)
[IEdmEnumeratorVersion7::Rollback3 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion7~Rollback3.html)
[IEdmVersion8::Rollback3 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion8~Rollback3.html)

## Availability

SOLIDWORKS PDM Professional 2017
