---
title: "GetNextFile Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "GetNextFile"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextFile.html"
---

# GetNextFile Method (IEdmFolder5)

Gets the next file in the enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextFile( _
   ByVal poPosition As IEdmPos5 _
) As IEdmFile5
```

### C#

```csharp
IEdmFile5 GetNextFile(
   IEdmPos5 poPosition
)
```

### C++/CLI

```cpp
IEdmFile5^ GetNextFile(
   IEdmPos5^ poPosition
)
```

### Parameters

- `poPosition`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of file to retrieve (see **Remarks**)

### Return Value

[IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)

## Examples

[Traverse Folders and Files in Vault (C#)](Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm)
[Traverse Folders and Files in Vault (VB.NET)](Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm)

## Remarks

Before calling this method the first time, you must populate poPosition with the interface to the position of the first file, IEdmPos5. Call [IEdmFolder5::GetFirstFilePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstFilePosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the files.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers not using smart-pointer wrapper functions must release the returned interface.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
