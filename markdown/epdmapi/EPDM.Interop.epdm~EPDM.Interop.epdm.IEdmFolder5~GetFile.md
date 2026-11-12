---
title: "GetFile Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "GetFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFile.html"
---

# GetFile Method (IEdmFolder5)

Gets the interface to a file with the specified name in this folder.

## Syntax

### Visual Basic

```vb
Function GetFile( _
   ByVal bsFileName As System.String _
) As IEdmFile5
```

### C#

```csharp
IEdmFile5 GetFile(
   System.string bsFileName
)
```

### C++/CLI

```cpp
IEdmFile5^ GetFile(
   System.String^ bsFileName
)
```

### Parameters

- `bsFileName`: Name of file to get

### Return Value

[IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmFile5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_NAME: A file with the specified name is not found.
- E_EDM_PERMISSION_DENIED: The user lacks permission to read the file.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::GetFirstFilePosition Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstFilePosition.html)
[IEdmFolder5::GetSubFolder Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetSubFolder.html)
[IEdmFolder5::GetFirstSubFolderPosition Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstSubFolderPosition.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
