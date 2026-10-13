---
title: "Rollback Method (IEdmEnumeratorVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5"
member: "Rollback"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~Rollback.html"
---

# Rollback Method (IEdmEnumeratorVersion5)

Obsolete. Superseded by [IEdmEnumeratorVersion6::Rollback2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion6~Rollback2.html).

## Syntax

### Visual Basic

```vb
Sub Rollback( _
   ByVal lVersionNo As System.Integer _
)
```

### C#

```csharp
void Rollback(
   System.int lVersionNo
)
```

### C++/CLI

```cpp
void Rollback(
   System.int lVersionNo
)
```

### Parameters

- `lVersionNo`: Version number to which to roll this file back (see **Remarks**)

## Remarks

This method destroys all versions after the version specified by lVersionNo. There is no undoing of the operation short of restoring a backup of the entire database and file archives.

After this method completes successfully, lVersionNo is the new latest version of the file.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_REVISION_NUMBER: The specified version number is out of bounds.
- E_EDM_PERMISSION_DENIED: The user lacks permission to delete files.

## See Also

[IEdmEnumeratorVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html)
[IEdmEnumeratorVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html)
[IEdmVersion5::Rollback Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~Rollback.html)
[IEdmRevision5::Rollback Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5~Rollback.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
