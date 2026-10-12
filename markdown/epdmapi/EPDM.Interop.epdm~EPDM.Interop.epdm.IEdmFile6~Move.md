---
title: "Move Method (IEdmFile6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile6"
member: "Move"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6~Move.html"
---

# Move Method (IEdmFile6)

Moves this file to another location in the vault.

## Syntax

### Visual Basic

```vb
Sub Move( _
   ByVal lParentWnd As System.Integer, _
   ByVal lParentID As System.Integer, _
   ByVal lNewParentID As System.Integer, _
   ByVal lFlags As System.Integer _
)
```

### C#

```csharp
void Move(
   System.int lParentWnd,
   System.int lParentID,
   System.int lNewParentID,
   System.int lFlags
)
```

### C++/CLI

```cpp
void Move(
   System.int lParentWnd,
   System.int lParentID,
   System.int lNewParentID,
   System.int lFlags
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `lParentID`: ID of the source folder
- `lNewParentID`: ID of the destination folder
- `lFlags`: 0; reserved

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

If the file has references, the paths of those references are updated to match the new location. If the file is being referenced by other files, the referencing files are updated to point to the new location.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.
- E_EDM_MOVE_FILE_PERMISSION_DENIED: The user does not have permission to move the file.

## See Also

[IEdmFile6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6.html)
[IEdmFile6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
