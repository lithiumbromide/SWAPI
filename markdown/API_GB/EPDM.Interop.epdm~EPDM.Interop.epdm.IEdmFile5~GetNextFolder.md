---
title: "GetNextFolder Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetNextFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetNextFolder.html"
---

# GetNextFolder Method (IEdmFile5)

Gets the next parent folder of this file.

## Syntax

### Visual Basic

```vb
Function GetNextFolder( _
   ByVal poPosition As IEdmPos5 _
) As IEdmFolder5
```

### C#

```csharp
IEdmFolder5 GetNextFolder(
   IEdmPos5 poPosition
)
```

### C++/CLI

```cpp
IEdmFolder5^ GetNextFolder(
   IEdmPos5^ poPosition
)
```

### Parameters

- `poPosition`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of next parent folder of this file

### Return Value

[IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)

## Examples

[Batch Add Files and Folders to Vault (VB.NET)](Batch_Add_Files_and_Folders_Example_VBNET.htm)
[Batch Add Files and Folders to Vault (C#)](Batch_Add_Files_and_Folders_Example_CSharp.htm)

## Remarks

Before calling this method the first time, you must populate poPosition with the interface to the position of the first parent folder, IEdmPos5. Call [IEdmFile5::GetFirstFolderPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFirstFolderPosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the folders.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmFolder5.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
