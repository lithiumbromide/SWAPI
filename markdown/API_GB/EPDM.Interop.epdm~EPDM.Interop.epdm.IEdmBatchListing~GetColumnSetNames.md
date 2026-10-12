---
title: "GetColumnSetNames Method (IEdmBatchListing)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing"
member: "GetColumnSetNames"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetColumnSetNames.html"
---

# GetColumnSetNames Method (IEdmBatchListing)

Gets the names of the column sets that can be used to create listings with this interface.

## Syntax

### Visual Basic

```vb
Function GetColumnSetNames() As EdmStrLst5
```

### C#

```csharp
EdmStrLst5 GetColumnSetNames()
```

### C++/CLI

```cpp
EdmStrLst5^ GetColumnSetNames();
```

### Return Value

[IEdmStrLst5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html); list of column set names that can be used as a parameter in [IEdmBatchListing::CreateList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~CreateList.html)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing.html)
[IEdmBatchListing Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing_members.html)

## Availability

SOLIDWORKS PDM Professional 2007
