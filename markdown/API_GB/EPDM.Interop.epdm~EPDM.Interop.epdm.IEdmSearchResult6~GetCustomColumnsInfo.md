---
title: "GetCustomColumnsInfo Method (IEdmSearchResult6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearchResult6"
member: "GetCustomColumnsInfo"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~GetCustomColumnsInfo.html"
---

# GetCustomColumnsInfo Method (IEdmSearchResult6)

Gets the custom column headers for this favorite search result.

## Syntax

### Visual Basic

```vb
Sub GetCustomColumnsInfo( _
   ByRef ppoRetColsInfo As EdmListCol() _
)
```

### C#

```csharp
void GetCustomColumnsInfo(
   out EdmListCol[] ppoRetColsInfo
)
```

### C++/CLI

```cpp
void GetCustomColumnsInfo(
   [Out] array<EdmListCol> ppoRetColsInfo
)
```

### Parameters

- `ppoRetColsInfo`: Array of [EdmListCol](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListCol.html) structures (see **Remarks**)

## Examples

See the [IEdmSearch10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10.html) examples.

## Remarks

ppoRetColsInfo is not null only for favorite search results that show custom columns.

If the favorite search result:

- Does not have custom columns,

- [ISearch10::GetFirstFavoriteResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10~GetFirstFavoriteResult.html) is called with bGetCustomColumns set to false, or

- [IEdmSearch5::GetFirstResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetFirstResult.html) is called,

then ppoRetColsInfo is null.

The six fields in each structure returned in the ppoRetColsInfo array map to the elements in the array (ppoRetColValues) returned by [IEdmSearchResult6::GetCustomColumnValues](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~GetCustomColumnValues.html) as follows:

size_of_ppoRetColValues = (size_of_ppoRetColsInfo) * (6 EdmListCol fields)

## See Also

[IEdmSearchResult6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6.html)
[IEdmSearchResult6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6_members.html)

## Availability

SOLIDWORKS PDM Professional 2021
