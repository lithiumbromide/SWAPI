---
title: "GetFolders Method (IEdmBatchListing)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing"
member: "GetFolders"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetFolders.html"
---

# GetFolders Method (IEdmBatchListing)

Gets all the folders in this listing.

## Syntax

### Visual Basic

```vb
Sub GetFolders( _
   ByRef ppoFolders() As EdmListFolder _
)
```

### C#

```csharp
void GetFolders(
   out EdmListFolder[] ppoFolders
)
```

### C++/CLI

```cpp
void GetFolders(
   [Out] array<EdmListFolder>^ ppoFolders
)
```

### Parameters

- `ppoFolders`: Array of [EdmListFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFolder.html) structures; one structure for each folder in the listing

## Remarks

Before calling this method, call [IEdmBatchListing::CreateList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~CreateList.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing.html)
[IEdmBatchListing Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
