---
title: "GetInstalledAddIn Method (IEdmAddInMgr8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr8"
member: "GetInstalledAddIn"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8~GetInstalledAddIn.html"
---

# GetInstalledAddIn Method (IEdmAddInMgr8)

Extracts files and information from the specified add-in.

## Syntax

### Visual Basic

```vb
Sub GetInstalledAddIn( _
   ByVal oNameOrID As System.Object, _
   ByVal bsExtractPath As System.String, _
   ByRef poAddIn As EdmAddInInfo2, _
   ByRef ppoFiles() As EdmAddInFileInfo, _
   ByRef ppoCmds() As EdmAddInMenuInfo _
)
```

### C#

```csharp
void GetInstalledAddIn(
   System.object oNameOrID,
   System.string bsExtractPath,
   out EdmAddInInfo2 poAddIn,
   out EdmAddInFileInfo[] ppoFiles,
   out EdmAddInMenuInfo[] ppoCmds
)
```

### C++/CLI

```cpp
void GetInstalledAddIn(
   System.Object^ oNameOrID,
   System.String^ bsExtractPath,
   [Out] EdmAddInInfo2 poAddIn,
   [Out] array<EdmAddInFileInfo>^ ppoFiles,
   [Out] array<EdmAddInMenuInfo>^ ppoCmds
)
```

### Parameters

- `oNameOrID`: ID or name of the add-in
- `bsExtractPath`: Path to the folder to which to extract files; ignored if empty
- `poAddIn`: [EdmAddInInfo2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2.html) structure; information about the add-in
- `ppoFiles`: Array of [EdmAddInFileInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo.html) structures, one for each file extracted from the add-in
- `ppoCmds`: Array of [EdmAddInMenuInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo.html) structures, one for each menu command implemented by the add-in

## Examples

See the [IEdmAddInMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_ID: oNameOrID specified an ID that was not found.
- E_EDM_INVALID_NAME: oNameOrID specified a name that was not found.
- E_EDM_FOLDER_NOT_FOUND: bsExtractPath contained a path to a missing folder.

## See Also

[IEdmAddInMgr8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8.html)
[IEdmAddInMgr8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8_members.html)
[IEdmAddInMgr8::ExtractInstalledAddIn Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8~ExtractInstalledAddIn.html)
[IEdmAddInMgr7::GetInstalledAddIns Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr7~GetInstalledAddIns.html)

## Availability

SOLIDWORKS PDM Professional 2010
