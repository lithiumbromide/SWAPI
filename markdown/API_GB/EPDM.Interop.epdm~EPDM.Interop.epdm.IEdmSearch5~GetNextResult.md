---
title: "GetNextResult Method (IEdmSearch5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch5"
member: "GetNextResult"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetNextResult.html"
---

# GetNextResult Method (IEdmSearch5)

Gets the next file or folder that matches the search criteria.

## Syntax

### Visual Basic

```vb
Function GetNextResult() As IEdmSearchResult5
```

### C#

```csharp
IEdmSearchResult5 GetNextResult()
```

### C++/CLI

```cpp
IEdmSearchResult5^ GetNextResult();
```

### Return Value

[IEdmSearchResult5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult5.html); Nothing or null if no more files or folders match the search criteria

## Examples

See the examples for [IEdmSearch5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html) and [IEdmSearch10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10.html).

## Remarks

Before calling this method, call [IEdmSearch5::GetFirstResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetFirstResult.html) or [IEdmSearch10::GetFirstFavoriteResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10~GetFirstFavoriteResult.html) to retrieve the first file or folder that matches the search criteria.

C++ users must release the returned interface, IEdmSearchResult5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The method successfully executed, but no files or folders match the search criteria.

## See Also

[IEdmSearch5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html)
[IEdmSearch5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
