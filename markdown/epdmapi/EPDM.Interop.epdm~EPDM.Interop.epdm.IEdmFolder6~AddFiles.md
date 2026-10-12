---
title: "AddFiles Method (IEdmFolder6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder6"
member: "AddFiles"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6~AddFiles.html"
---

# AddFiles Method (IEdmFolder6)

Adds one or more files to this folder.

## Syntax

### Visual Basic

```vb
Sub AddFiles( _
   ByVal lParentWnd As System.Integer, _
   ByRef ppoFiles() As EdmAddFileInfo, _
   ByVal poCallback As IEdmCallback6 _
)
```

### C#

```csharp
void AddFiles(
   System.int lParentWnd,
   out EdmAddFileInfo[] ppoFiles,
   IEdmCallback6 poCallback
)
```

### C++/CLI

```cpp
void AddFiles(
   System.int lParentWnd,
   [Out] array<EdmAddFileInfo>^ ppoFiles,
   IEdmCallback6^ poCallback
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `ppoFiles`: Array of [EdmAddFileInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFileInfo.html) structures; one structure for each added file
- `poCallback`: Optional pointer to a class that implements [IEdmCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6.html) to control this add operation and obtain progress information about it

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

This method is more efficient than [IEdmFolder5::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFile.html) when adding many files.

Before calling this method, call [IFolder12::SetFileNameSerNo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder12~SetFileNameSerNo.html) for each new file to specify how to create the name of the new file's data card.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_SN_FILE: The operation needs to generate serial numbers from a file but the end of the file has been reached.
- E_EDM_SN_FILE_NOT_FOUND: The operation needs to generate serial numbers from a file that cannot be found.
- E_EDM_CANCELLED_BY_USER: The operation was cancelled via the optional callback interface.

## See Also

[IEdmFolder6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6.html)
[IEdmFolder6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
