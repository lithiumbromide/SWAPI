---
title: "DestroyDeletedItems Method (IEdmFolder7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder7"
member: "DestroyDeletedItems"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder7~DestroyDeletedItems.html"
---

# DestroyDeletedItems Method (IEdmFolder7)

Obsolete. Superseded by [IEdmFolder13::DestroyDeletedItems2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder13~DestroyDeletedItems2.html).

## Syntax

### Visual Basic

```vb
Sub DestroyDeletedItems( _
   ByVal bRecursive As System.Boolean, _
   ByVal vDeleteDate As System.Object, _
   ByRef ppoFiles() As EdmFileInfo, _
   ByRef poErrors() As EdmBatchDelErrInfo _
)
```

### C#

```csharp
void DestroyDeletedItems(
   System.bool bRecursive,
   System.object vDeleteDate,
   out EdmFileInfo[] ppoFiles,
   out EdmBatchDelErrInfo[] poErrors
)
```

### C++/CLI

```cpp
void DestroyDeletedItems(
   System.bool bRecursive,
   System.Object^ vDeleteDate,
   [Out] array<EdmFileInfo>^ ppoFiles,
   [Out] array<EdmBatchDelErrInfo>^ poErrors
)
```

### Parameters

- `bRecursive`: True to return a list containing all of the sub-items, false to return just the root items
- `vDeleteDate`: Latest delete date of items to destroy; items deleted after this date are not destroyed
- `ppoFiles`: Array of [EdmFileInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmFileInfo.html) structures; one structure for each destroyed file containing information about the file
- `poErrors`: Array of [EdmBatchDelErrInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchDelErrInfo.html) structures; one structure for each destroyed file containing information about errors that occurred during this operation

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFolder7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder7.html)
[IEdmFolder7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder7_members.html)
[IEdmFolder11::RecoverDeletedItems Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11~RecoverDeletedItems.html)

## Availability

SOLIDWORKS PDM Professional Version 12.0
