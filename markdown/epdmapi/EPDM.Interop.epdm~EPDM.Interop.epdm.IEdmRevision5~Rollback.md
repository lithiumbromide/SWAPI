---
title: "Rollback Method (IEdmRevision5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevision5"
member: "Rollback"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5~Rollback.html"
---

# Rollback Method (IEdmRevision5)

Obsolete. Superseded by [IEdmRevision6::Rollback2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision6~Rollback2.html).

## Syntax

### Visual Basic

```vb
Sub Rollback()
```

### C#

```csharp
void Rollback()
```

### C++/CLI

```cpp
void Rollback();
```

## Remarks

This method destroys all versions after this revision number. To undo this rollback operation, you need to restore a backup of the entire database and file archives.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The user lacks permission to delete files.

## See Also

[IEdmRevision5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5.html)
[IEdmRevision5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
