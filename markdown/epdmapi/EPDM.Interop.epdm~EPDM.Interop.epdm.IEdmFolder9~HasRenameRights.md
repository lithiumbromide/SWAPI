---
title: "HasRenameRights Method (IEdmFolder9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder9"
member: "HasRenameRights"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder9~HasRenameRights.html"
---

# HasRenameRights Method (IEdmFolder9)

Gets whether the user has permission to rename the specified file in this folder.

## Syntax

### Visual Basic

```vb
Function HasRenameRights( _
   ByVal lParentWnd As System.Integer, _
   ByVal lFileID As System.Integer, _
   ByVal bsOldFileName As System.String, _
   ByVal bsRenamedFileName As System.String, _
   ByVal pbSilent As System.Boolean _
) As System.Boolean
```

### C#

```csharp
System.bool HasRenameRights(
   System.int lParentWnd,
   System.int lFileID,
   System.string bsOldFileName,
   System.string bsRenamedFileName,
   System.bool pbSilent
)
```

### C++/CLI

```cpp
System.bool HasRenameRights(
   System.int lParentWnd,
   System.int lFileID,
   System.String^ bsOldFileName,
   System.String^ bsRenamedFileName,
   System.bool pbSilent
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `lFileID`: ID of the file to rename
- `bsOldFileName`: Old file name
- `bsRenamedFileName`: New file name
- `pbSilent`: True to silently check for permissions to rename the file (i.e., do not display message box), false to not

### Return Value

True if the user has permission to rename the specified file, false if not

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## See Also

[IEdmFolder9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder9.html)
[IEdmFolder9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder9_members.html)

## Availability

SOLIDWORKS PDM Professional 2016
