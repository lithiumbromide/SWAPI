---
title: "Rollback Method (IEdmVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVersion5"
member: "Rollback"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~Rollback.html"
---

# Rollback Method (IEdmVersion5)

Obsolete. Superseded by [IEdmVersion6::Rollback2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion6~Rollback2.html).

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

This method deletes both the file data and the file data card data when it deletes versions. You cannot undo this rollback, unless you restore a complete backup of the database and the file archives.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The user does not have permission to delete files.
- E_EDM_INVALID_REVISION_NUMBER: The version does not exist.

## See Also

[IEdmVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5.html)
[IEdmVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5_members.html)
[IEdmEnumeratorVersion5::Rollback Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~Rollback.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
