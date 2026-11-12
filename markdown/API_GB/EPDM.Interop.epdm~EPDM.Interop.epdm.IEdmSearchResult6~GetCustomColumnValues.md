---
title: "GetCustomColumnValues Method (IEdmSearchResult6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearchResult6"
member: "GetCustomColumnValues"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~GetCustomColumnValues.html"
---

# GetCustomColumnValues Method (IEdmSearchResult6)

Gets the custom column values returned in this favorite search result.

## Syntax

### Visual Basic

```vb
Sub GetCustomColumnValues( _
   ByRef ppoRetColValues As System.String() _
)
```

### C#

```csharp
void GetCustomColumnValues(
   out System.string[] ppoRetColValues
)
```

### C++/CLI

```cpp
void GetCustomColumnValues(
   [Out] System.array<String^> ppoRetColValues
)
```

### Parameters

- `ppoRetColValues`: Array of string values (see **Remarks**)

## Examples

See the [IEdmSearch10](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10.html) examples.

## Remarks

ppoRetColValues is not null only for favorite search results that show custom columns.

If the favorite search result:

- Does not have custom columns,

- [ISearch10::GetFirstFavoriteResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch10~GetFirstFavoriteResult.html) is called with bGetCustomColumns set to false, or

- [IEdmSearch5::GetFirstResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetFirstResult.html) is called,

then ppoRetColValues is null.

The ppoRetColValues array elements map to the fields in the [EdmListCol](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListCol.html) structures in the array (ppoRetColsInfo) that is returned by [IEdmSearchResult6::GetCustomColumnsInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6~GetCustomColumnsInfo.html) as follows:

size_of_ppoRetColValues = (size_of_ppoRetColsInfo) * (6 EdmListCol fields)

## See Also

[IEdmSearchResult6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6.html)
[IEdmSearchResult6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearchResult6_members.html)

## Availability

SOLIDWORKS PDM Professional 2021
