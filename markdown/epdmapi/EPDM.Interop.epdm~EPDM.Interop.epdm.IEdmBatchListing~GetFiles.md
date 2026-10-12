---
title: "GetFiles Method (IEdmBatchListing)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing"
member: "GetFiles"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetFiles.html"
---

# GetFiles Method (IEdmBatchListing)

Obsolete. Superseded by [IEdmBatchListing4::GetFiles2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing4~GetFiles2.html).

## Syntax

### Visual Basic

```vb
Sub GetFiles( _
   ByRef ppoFiles() As EdmListFile _
)
```

### C#

```csharp
void GetFiles(
   out EdmListFile[] ppoFiles
)
```

### C++/CLI

```cpp
void GetFiles(
   [Out] array<EdmListFile>^ ppoFiles
)
```

### Parameters

- `ppoFiles`: Array of [EdmListFile](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile.html) structures; one structure for each file in the listing

## Remarks

Before calling this method, call [IEdmBatchListing::CreateList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~CreateList.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing.html)
[IEdmBatchListing Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
