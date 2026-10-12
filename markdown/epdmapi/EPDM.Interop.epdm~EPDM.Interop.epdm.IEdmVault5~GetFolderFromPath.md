---
title: "GetFolderFromPath Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "GetFolderFromPath"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFolderFromPath.html"
---

# GetFolderFromPath Method (IEdmVault5)

Gets an interface to a folder on the specified file system path.

## Syntax

### Visual Basic

```vb
Function GetFolderFromPath( _
   ByVal bsFolderPath As System.String _
) As IEdmFolder5
```

### C#

```csharp
IEdmFolder5 GetFolderFromPath(
   System.string bsFolderPath
)
```

### C++/CLI

```cpp
IEdmFolder5^ GetFolderFromPath(
   System.String^ bsFolderPath
)
```

### Parameters

- `bsFolderPath`: File system path to the folder

### Return Value

[IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html); Null if the folder in bsFolderPath is not found

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

C++ users must release the returned interface, IEdmFolder5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The folder was not found.
- E_EDM_NOT_LOGGED_IN: You must call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) before calling this method.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)
[IEdmVault5::GetFileFromPath Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFileFromPath.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
