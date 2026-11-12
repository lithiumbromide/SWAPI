---
title: "StoreValuesFromDatabase Method (IEdmEnumeratorVariable5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable5"
member: "StoreValuesFromDatabase"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~StoreValuesFromDatabase.html"
---

# StoreValuesFromDatabase Method (IEdmEnumeratorVariable5)

Copies file data card data from the SOLIDWORKS PDM Professional database to the file.

## Syntax

### Visual Basic

```vb
Sub StoreValuesFromDatabase( _
   ByVal lFolderID As System.Integer, _
   ByVal bOnlyMissingValues As System.Boolean, _
   Optional ByVal poProgressCb As EdmCallback _
)
```

### C#

```csharp
void StoreValuesFromDatabase(
   System.int lFolderID,
   System.bool bOnlyMissingValues,
   EdmCallback poProgressCb
)
```

### C++/CLI

```cpp
void StoreValuesFromDatabase(
   System.int lFolderID,
   System.bool bOnlyMissingValues,
   EdmCallback^ poProgressCb
)
```

### Parameters

- `lFolderID`: ID of the file's parent folder
- `bOnlyMissingValues`: True to only copy variables without a value, false to copy all variables
- `poProgressCb`: Not used

## Remarks

This method corresponds to the SOLIDWORKS PDM Professional user interface right-click menu command, Update File Attributes from Database.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_FILE: The file format is not recognized.
- E_EDM_FILE_SHARE_ERROR: The file is exclusively opened in another application.
- E_EDM_IO_ERROR: Error writing data to the file.

## See Also

[IEdmEnumeratorVariable5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)
[IEdmEnumeratorVariable5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
