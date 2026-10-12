---
title: "GetFirstFolderPosition Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetFirstFolderPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFirstFolderPosition.html"
---

# GetFirstFolderPosition Method (IEdmFile5)

Starts an enumeration of the parent folders of this file.

## Syntax

### Visual Basic

```vb
Function GetFirstFolderPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstFolderPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstFolderPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first parent folder

## Examples

[Batch Add Files and Folders to Vault (VB.NET)](Batch_Add_Files_and_Folders_Example_VBNET.htm)
[Batch Add Files and Folders to Vault (C#)](Batch_Add_Files_and_Folders_Example_CSharp.htm)

## Remarks

Files can be shared between several folders in SOLIDWORKS PDM Professional. Call [IEdmFolder5::AddFileShared](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFileShared.html) to share a file between several folders.

After calling this method to get the postion of the first parent folder in the list, call [IEdmFile5::GetNextFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetNextFolder.html) to get the parent folders.

C++ programmers not using smart-pointer wrapper functions must release the returned pointer to IEdmPos5.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
