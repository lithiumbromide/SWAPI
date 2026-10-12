---
title: "ExtractInstalledAddIn Method (IEdmAddInMgr8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr8"
member: "ExtractInstalledAddIn"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8~ExtractInstalledAddIn.html"
---

# ExtractInstalledAddIn Method (IEdmAddInMgr8)

Extracts files from the specified add-in and places them in the specified folder.

## Syntax

### Visual Basic

```vb
Sub ExtractInstalledAddIn( _
   ByVal oNameOrID As System.Object, _
   ByVal bsExtractPath As System.String, _
   ByRef ppoFiles As EdmAddInFileInfo() _
)
```

### C#

```csharp
void ExtractInstalledAddIn(
   System.object oNameOrID,
   System.string bsExtractPath,
   out EdmAddInFileInfo[] ppoFiles
)
```

### C++/CLI

```cpp
void ExtractInstalledAddIn(
   System.Object^ oNameOrID,
   System.String^ bsExtractPath,
   [Out] array<EdmAddInFileInfo> ppoFiles
)
```

### Parameters

- `oNameOrID`: ID or name of the add-in from which to extract files
- `bsExtractPath`: Path to the folder to which to extract files; ignored if empty
- `ppoFiles`: Array of [EdmAddInFileInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo.html) structures, one structure for each extracted file

## Remarks

This method performs a subset of the functionality of [IEdmAddInMgr8::GetInstalledAddIn](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8~GetInstalledAddIn.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_ID: oNameOrID specified an ID that was not found.
- E_EDM_INVALID_NAME: oNameOrID specified a name that was not found.
- E_EDM_FOLDER_NOT_FOUND: bsExtractPath contained a path to a missing folder.

## See Also

[IEdmAddInMgr8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8.html)
[IEdmAddInMgr8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
