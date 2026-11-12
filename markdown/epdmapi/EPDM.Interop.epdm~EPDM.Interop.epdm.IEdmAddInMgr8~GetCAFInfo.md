---
title: "GetCAFInfo Method (IEdmAddInMgr8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr8"
member: "GetCAFInfo"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8~GetCAFInfo.html"
---

# GetCAFInfo Method (IEdmAddInMgr8)

Extracts files and information from an add-in that is stored in a *.CAF that pre-dates SOLIDWORKS PDM Professional 2010.

## Syntax

### Visual Basic

```vb
Sub GetCAFInfo( _
   ByVal bsCAFPath As System.String, _
   ByVal bsExtractPath As System.String, _
   ByRef poAddIn As EdmAddInInfo2, _
   ByRef ppoFiles() As EdmAddInFileInfo, _
   ByRef ppoCmds() As EdmAddInMenuInfo _
)
```

### C#

```csharp
void GetCAFInfo(
   System.string bsCAFPath,
   System.string bsExtractPath,
   out EdmAddInInfo2 poAddIn,
   out EdmAddInFileInfo[] ppoFiles,
   out EdmAddInMenuInfo[] ppoCmds
)
```

### C++/CLI

```cpp
void GetCAFInfo(
   System.String^ bsCAFPath,
   System.String^ bsExtractPath,
   [Out] EdmAddInInfo2 poAddIn,
   [Out] array<EdmAddInFileInfo>^ ppoFiles,
   [Out] array<EdmAddInMenuInfo>^ ppoCmds
)
```

### Parameters

- `bsCAFPath`: Path to the *.CAF from which to get information
- `bsExtractPath`: Path to the folder to which to extract files; ignored if empty
- `poAddIn`: [EdmAddInInfo2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo2.html) structure; information about the add-in
- `ppoFiles`: Array of [EdmAddInFileInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo.html) structures, one for each file extracted from the add-in
- `ppoCmds`: Array of [EdmAddInMenuInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInMenuInfo.html) structures, one for each menu command implemented by the add-in

## Examples

See the [IEdmAddInMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_FOUND: The specified *.CAF file was not found.

## See Also

[IEdmAddInMgr8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8.html)
[IEdmAddInMgr8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr8_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
