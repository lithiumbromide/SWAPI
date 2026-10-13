---
title: "CreateList Method (IEdmBatchListing)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing"
member: "CreateList"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~CreateList.html"
---

# CreateList Method (IEdmBatchListing)

Obsolete. Superseded by [IEdmBatchListing2::CreateListEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2~CreateListEx.html).

## Syntax

### Visual Basic

```vb
Sub CreateList( _
   ByVal bsColumnSetName As System.String, _
   ByRef ppoColumns As EdmListCol() _
)
```

### C#

```csharp
void CreateList(
   System.string bsColumnSetName,
   out EdmListCol[] ppoColumns
)
```

### C++/CLI

```cpp
void CreateList(
   System.String^ bsColumnSetName,
   [Out] array<EdmListCol> ppoColumns
)
```

### Parameters

- `bsColumnSetName`: Empty string, column set name returned by [IEdmBatchListing::GetColumnSetNames](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetColumnSetNames.html), or a list of variable names separated by a newline character and starting with a newline character (e.g., "\nAuthor\nProject\nDate")
- `ppoColumns`: Array of [EdmListCol](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListCol.html) structures; one structure for each column in the column set; empty array if bsColumnSetName is an empty string

## Remarks

After calling this method, call [IEdmBatchListing::GetFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetFiles.html) and [IEdmBatchListing::GetFolders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetFolders.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing.html)
[IEdmBatchListing Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
