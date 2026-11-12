---
title: "GetFirstFilePosition Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "GetFirstFilePosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstFilePosition.html"
---

# GetFirstFilePosition Method (IEdmFolder5)

Starts an enumeration of the files in this folder.

## Syntax

### Visual Basic

```vb
Function GetFirstFilePosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstFilePosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstFilePosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first file in this folder

## Examples

[Traverse Folders and Files in Vault (C#)](Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm)
[Traverse Folders and Files in Vault (VB.NET)](Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm)

## Remarks

After calling this method, pass the returned first file position to [IEdmFolder5::GetNextFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextFile.html) to get the first file in the list. Then call IEdmFolder5::GetNextFile repeatedly to get the rest of the files in the list.

C++ users not using smart-pointer wrapper functions must release the returned pointer, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::GetFirstSubFolderPosition Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstSubFolderPosition.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
