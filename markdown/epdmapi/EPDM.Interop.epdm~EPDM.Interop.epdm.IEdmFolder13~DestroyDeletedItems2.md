---
title: "DestroyDeletedItems2 Method (IEdmFolder13)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder13"
member: "DestroyDeletedItems2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder13~DestroyDeletedItems2.html"
---

# DestroyDeletedItems2 Method (IEdmFolder13)

Destroys the specified deleted items in this folder.

## Syntax

### Visual Basic

```vb
Sub DestroyDeletedItems2( _
   ByVal poDeletedItems() As EdmDeletedItems, _
   ByRef ppoFiles() As EdmFileInfo, _
   ByRef poErrors() As EdmBatchDelErrInfo _
)
```

### C#

```csharp
void DestroyDeletedItems2(
   EdmDeletedItems[] poDeletedItems,
   out EdmFileInfo[] ppoFiles,
   out EdmBatchDelErrInfo[] poErrors
)
```

### C++/CLI

```cpp
void DestroyDeletedItems2(
   array<EdmDeletedItems>^ poDeletedItems,
   [Out] array<EdmFileInfo>^ ppoFiles,
   [Out] array<EdmBatchDelErrInfo>^ poErrors
)
```

### Parameters

- `poDeletedItems`: Array of [EdmDeletedItems](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems.html) structures; one structure for each deleted file
- `ppoFiles`: Array of [EdmFileInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo.html) structures; one structure for each destroyed file containing information about the file
- `poErrors`: Array of [EdmBatchDelErrInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchDelErrInfo.html) structures; one structure for each destroyed file containing information about errors that occurred during this operation

## Examples

[Destroy Deleted Files in Vault (VB.NET)](Destroy_Deleted_Files_in_Vault_Example_VBNET.htm)
[Destroy Deleted Files in Vault (C#)](Destroy_Deleted_Files_in_Vault_Example_CSharp.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFolder13 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder13.html)
[IEdmFolder13 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder13_members.html)
[IEdmFolder11::RecoverDeletedItems Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11~RecoverDeletedItems.html)

## Availability

SOLIDWORKS PDM Professional 2022
